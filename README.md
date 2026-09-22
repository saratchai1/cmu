# CMU TOR 4.1.7 – Traffic Analysis Software Evidence Pack

ชุดนี้ใช้เป็น **evidence / markup guideline** สำหรับข้อกำหนด 4.1.7 ใน TOR ชุดโปรแกรมวิเคราะห์การจราจรและออกแบบสัญญาณไฟ โดยอ้างอิงจากไฟล์ TOR และภาพคุณสมบัติ PTV ที่ส่งมา รวมกับเอกสารทางการของ PTV และ SIDRA

## สถานะ ณ วันที่ 22 กันยายน 2026

จากหมายเลขข้อที่ไฮไลต์สีเขียวใน TOR พบทั้งหมด **76 ข้อ**

| สถานะหลักฐาน | จำนวน | ความหมาย |
|---|---:|---|
| FOUND | 66 | พบหลักฐานทางเทคนิคที่รองรับข้อกำหนดโดยตรงหรือค่อนข้างตรง |
| PARTIAL | 4 | พบหลักฐานบางส่วน แต่ยังขาดข้อความ/รายการยืนยันบางจุด |
| VENDOR DOC | 6 | ควรใช้เอกสารจากผู้ผลิต/ตัวแทน เช่น quotation, license schedule, authorization หรือ subscription/update terms |

> สถานะนี้เป็นการประเมินว่า “มีหลักฐานรองรับมากน้อยเพียงใด” ไม่ใช่คำตัดสินผลการตรวจรับหรือผลการจัดซื้อ

## เอกสารใน repo

- [TOR Evidence Matrix](docs/TOR_EVIDENCE_MATRIX.md) — ตารางครบทุกข้อที่ไฮไลต์สีเขียว พร้อมหลักฐานและสิ่งที่ยังต้องขอ
- [Markup Guideline](docs/MARKUP_GUIDE.md) — บอกว่าภาพที่ส่งมาควรมาร์คเลขข้อใดตรงตำแหน่งใด
- [Official Source Register](docs/SOURCE_REGISTER.md) — รายการเอกสาร/หน้าเว็บทางการและเลขอ้างอิงที่ใช้ใน matrix
- [Vendor Document Checklist](docs/VENDOR_DOCUMENT_CHECKLIST.md) — รายการเอกสารที่ควรขอเพิ่มเพื่อปิดข้อที่ยังไม่ครบ
- [PTV Vissim Matrix – marked transcription](evidence/PTV_VISSIM_MATRIX_MARKED.md) — ถอดข้อมูลจากภาพตาราง Vissim พร้อมเลข TOR
- [PTV Academic Package – marked transcription](evidence/PTV_ACADEMIC_PACKAGE_MARKED.md) — ถอดข้อมูลจากภาพ Academic Package พร้อมเลข TOR
- [Highlighted Clause Register](evidence/TOR_HIGHLIGHTED_CLAUSES.md) — รายการ 76 หมายเลขข้อที่ถูกไฮไลต์

## วิธีใช้

1. เปิด [TOR Evidence Matrix](docs/TOR_EVIDENCE_MATRIX.md) เป็นเอกสารหลัก
2. เวลามาร์คเอกสารประกอบ ให้ใส่เลข TOR ตาม [Markup Guideline](docs/MARKUP_GUIDE.md)
3. ข้อที่เป็น **FOUND** ใช้แหล่งอ้างอิงใน [Official Source Register](docs/SOURCE_REGISTER.md) ประกอบ
4. ข้อ **PARTIAL** และ **VENDOR DOC** ให้ขอเอกสารเพิ่มตาม [Vendor Document Checklist](docs/VENDOR_DOCUMENT_CHECKLIST.md)
5. ก่อนส่งจริง ควรบันทึกหน้าเว็บทางการเป็น PDF พร้อมวันที่เข้าถึง และแนบ quotation/license schedule ที่ระบุรุ่น จำนวนสิทธิ์ ระยะเวลา และสิทธิ์อัปเดตให้ชัดเจน

## Scope

ชุดนี้ครอบคลุมเฉพาะข้อ 4.1.7.2 ที่อยู่ในไฟล์ TOR ที่ส่งมา และเน้นข้อที่ถูกไฮไลต์สีเขียวเป็นลำดับแรก
