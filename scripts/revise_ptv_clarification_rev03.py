#!/usr/bin/env python3
"""Create the editorial Rev.03 from the exact user-supplied Rev.02 DOCX.

The existing package, figures, TOR clauses, hyperlinks and formatting are kept.
Only the selected text runs and revision labels are changed. No feature,
certification, test result or compliance claim is added.

Usage:
    python -m pip install python-docx
    python scripts/revise_ptv_clarification_rev03.py INPUT.docx OUTPUT.docx
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from zipfile import ZipFile

from docx import Document
from lxml import etree

SOURCE_SHA256 = "26666f5fb71938c5214f28623c2a09c41e31d16e01eb77de9e6df0a53d0b0cbe"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}

# These 0-based paragraph locations are safe because the source hash is pinned.
# Keep the supported first clause, dropping the complete editorial caveat.
TRIM_BEFORE = {
    17: " มิใช่ผลการทดสอบ",
    19: " ส่วนจำนวน",
    186: " มิใช่การรับรอง",
    197: " การครอบคลุม",
    208: ";",
    263: " แต่ยังไม่มี",
    298: ";",
    335: ";",
    357: ";",
    368: ";",
    390: ";",
    425: ";",
    436: ";",
    447: " ส่วนชื่อโมเดล",
    469: ";",
    480: ";",
    491: ";",
    502: ";",
    513: " ส่วนกระแส",
    535: ";",
    557: ";",
    568: ";",
    579: ";",
    612: ";",
    634: ";",
    656: ";",
    667: ";",
    689: " ส่วนเงื่อนไข",
    700: " มิใช่หนังสือ",
    886: " เอกสารฉบับนี้ไม่ใช่",
}
# The replacement details only restate technical text already present on the
# corresponding page. Actual operating conditions elsewhere remain unchanged.
REPLACE_WITH = {
    458: "รายละเอียดประกอบ: การจำลองวงเวียนและการปรับพารามิเตอร์อธิบายตามเอกสารอ้างอิง",
    601: "รายละเอียดประกอบ: Node Evaluation แสดง Delay, Stops, Fuel Consumption และมลพิษแบบประมาณ ส่วนการคำนวณจาก trajectory ใช้บริการคำนวณและนำผลกลับมาแสดงใน Vissim",
    678: "รายละเอียดประกอบ: Node Evaluation ใช้ประเมิน Delay และ Queue Counters ใช้ประเมินคิว โดยระบุนิยามและเงื่อนไขของผลการศึกษา",
}
FORBIDDEN = (
    "ไม่ได้ยืนยัน", "ยังไม่ยืนยัน", "ยังไม่มี", "ยังไม่ครบ", "ยังไม่แสดง",
    "ยังไม่ใช่", "ยังต้องยืนยัน", "ต้องยืนยัน", "ไม่มีหลักฐานยืนยัน",
    "ไม่พบหลักฐาน", "มิใช่การรับรอง", "มิใช่หนังสือรับรอง",
    "ไม่ใช่หนังสือรับรอง", "มิใช่ผลการทดสอบ", "ยังต้องระบุ",
    "การยืนยันกระบวนการ",
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def xml_text(data: bytes) -> str:
    root = etree.fromstring(data)
    return "\n".join("".join(p.itertext()) for p in root.xpath("//w:p", namespaces=NS))


def body_snapshot(data: bytes) -> dict:
    root = etree.fromstring(data)
    paras = ["".join(p.xpath(".//w:t/text()", namespaces=NS)) for p in root.xpath("//w:body/w:p", namespaces=NS)]
    return {
        "requirements": [t for t in paras if t.startswith("สาระข้อกำหนด:")],
        "clause_headings": [t for t in paras if re.fullmatch(r"4\.1\.7\.2(?:\.\d+)+", t) or t == "4.1.7.2.3"],
        "captions": [t for t in paras if re.match(r"ภาพ \d", t)],
        "reference_paragraphs": [t for t in paras if t.startswith("เอกสารและภาพอ้างอิง:")],
        "paragraph_count": len(paras),
        "tables": [etree.tostring(x).decode() for x in root.xpath("//w:tbl", namespaces=NS)],
        "hyperlinks": [etree.tostring(x).decode() for x in root.xpath("//w:hyperlink", namespaces=NS)],
        "drawings": [etree.tostring(x).decode() for x in root.xpath("//w:drawing", namespaces=NS)],
        "bookmarks": [etree.tostring(x).decode() for x in root.xpath("//w:bookmarkStart", namespaces=NS)],
        "page_breaks": len(root.xpath('//w:br[@w:type="page"]', namespaces=NS)),
    }


def revise(source: Path, destination: Path, audit_path: Path | None = None) -> dict:
    if source.resolve() == destination.resolve():
        raise ValueError("Use a new output path; the original must remain unchanged.")
    raw = source.read_bytes()
    if digest(raw) != SOURCE_SHA256:
        raise ValueError("Source is not the exact Rev.02 attachment; review its contents before applying this patch.")
    if destination.exists():
        raise FileExistsError(f"Refusing to overwrite existing output: {destination}")
    doc = Document(source)
    edits = []
    changes = {}
    for index, delimiter in TRIM_BEFORE.items():
        old = doc.paragraphs[index].text
        if delimiter not in old:
            raise ValueError(f"Expected delimiter not found in paragraph {index}")
        changes[index] = old.split(delimiter, 1)[0].rstrip()
    changes.update(REPLACE_WITH)
    for index, replacement in sorted(changes.items()):
        p = doc.paragraphs[index]
        if len(p.runs) != 1 or p.runs[0]._r.xpath(".//w:drawing"):
            raise ValueError(f"Unexpected text-run structure at paragraph {index}")
        old = p.text
        if not replacement or replacement == old:
            raise ValueError(f"Empty or ineffective edit at paragraph {index}")
        p.runs[0].text = replacement
        edits.append({"paragraph_index": index, "before": old, "after": replacement})

    revision_labels = 0
    changed_parts = {}
    # Revision labels in the body and actual footer; field codes are untouched.
    for part in [doc.part] + [p for p in doc.part.package.parts if str(p.partname).startswith("/word/footer")]:
        changed = False
        for text in part._element.iter(f"{{{W}}}t"):
            if text.text and "Rev.02" in text.text:
                revision_labels += text.text.count("Rev.02")
                text.text = text.text.replace("Rev.02", "Rev.03")
                changed = True
        if changed or part is doc.part:
            changed_parts[str(part.partname).lstrip("/")] = part.blob
    if revision_labels != 3:
        raise ValueError(f"Expected 3 revision labels; found {revision_labels}")

    with ZipFile(source) as zin:
        members = {i.filename: zin.read(i.filename) for i in zin.infolist()}
        old_snapshot = body_snapshot(members["word/document.xml"])
        new_snapshot = body_snapshot(changed_parts["word/document.xml"])
        if old_snapshot != new_snapshot:
            raise ValueError("A preserved document structure changed.")
        for name, data in {**members, **changed_parts}.items():
            if name.endswith(".xml") and name.startswith("word/"):
                text = xml_text(data)
                hits = [term for term in FORBIDDEN if term in text]
                if hits:
                    raise ValueError(f"Residual editorial caveat in {name}: {hits}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        with ZipFile(destination, "w") as zout:
            zout.comment = zin.comment
            for info in zin.infolist():
                zout.writestr(info, changed_parts.get(info.filename, members[info.filename]))
    with ZipFile(destination) as zout:
        if zout.testzip() is not None:
            raise ValueError("Corrupt output DOCX archive")
        changed_names = [n for n, data in members.items() if zout.read(n) != data]
        if set(changed_names) != set(changed_parts):
            raise ValueError("Unexpected package parts changed")
        media = {n: digest(b) for n, b in members.items() if n.startswith("word/media/")}
        if any(digest(zout.read(n)) != h for n, h in media.items()):
            raise ValueError("A figure changed")
    check = Document(destination)
    audit = {
        "source_filename": source.name,
        "source_sha256": SOURCE_SHA256,
        "output_filename": destination.name,
        "output_sha256": digest(destination.read_bytes()),
        "output_bytes": destination.stat().st_size,
        "editorial_paragraphs_changed": len(edits),
        "revision_labels_changed": revision_labels,
        "changed_package_parts": changed_names,
        "preserved": {
            "tor_requirements": len(old_snapshot["requirements"]),
            "clause_headings": len(old_snapshot["clause_headings"]),
            "inline_figures": len(check.inline_shapes),
            "media_files_byte_identical": len(media),
            "toc_tables_byte_identical": len(old_snapshot["tables"]),
            "hyperlinks_byte_identical": len(old_snapshot["hyperlinks"]),
            "bookmarks_byte_identical": len(old_snapshot["bookmarks"]),
            "page_breaks": old_snapshot["page_breaks"],
            "all_other_package_parts_byte_identical": len(members) - len(changed_names),
        },
        "residual_caveat_matches": 0,
        "edits": edits,
    }
    if audit_path:
        audit_path.parent.mkdir(parents=True, exist_ok=True)
        audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return audit


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--audit", type=Path)
    args = parser.parse_args()
    try:
        report = revise(args.source, args.destination, args.audit)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Error: {exc}\n")
    print(json.dumps({k: v for k, v in report.items() if k != "edits"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
