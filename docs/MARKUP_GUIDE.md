# Markup Guideline for TOR Evidence

แนวทางมาร์คเอกสารประกอบให้ reviewer ไล่ตรวจตามเลข TOR ได้เร็ว โดยยึด **หมายเลขข้อที่ไฮไลต์สีเขียวใน TOR** เป็นตัวตั้ง

## 1. รูปแบบการมาร์คที่แนะนำ

บนเอกสารประกอบแต่ละหน้า ให้ใส่กรอบหรือ callout แบบนี้:

**[TOR 4.1.7.2.x.x] — keyword สั้น ๆ**

ตัวอย่าง:
- [TOR 4.1.7.2.1.5.1] Unlimited Signals
- [TOR 4.1.7.2.1.5.2] Vissig / VisVAP
- [TOR 4.1.7.2.3.6.3] Queue Spillback
- [TOR 4.1.7.2.3.10.2] HCM Edition 7 compatibility

อย่าใส่คำว่า “ผ่าน” บน evidence ถ้าเอกสารนั้นรองรับเพียงบางส่วน ให้ใช้คำว่า **PARTIAL** แทน

## 2. Legend

| Mark | ใช้เมื่อ |
|---|---|
| FOUND | ข้อความในเอกสารตรงหรือรองรับข้อ TOR ได้ชัด |
| PARTIAL | เอกสารตอบได้บางส่วน แต่ยังมี wording/จำนวน/feature บางตัวไม่ครบ |
| VENDOR DOC | ต้องใช้ quotation, license schedule, authorization หรือ subscription/update terms |

---

# 3. ภาพ PTV Vissim package matrix

ให้มาร์คบนภาพต้นฉบับตามนี้:

| ตำแหน่งในภาพ | Callout |
|---|---|
| แถว GUI | **[TOR 4.1.7.2.1.1] GUI** |
| หัวคอลัมน์ PTV Vissim Advanced ที่เขียน “unlimited” | **[TOR 4.1.7.2.1.5.1] Unlimited Signals** |
| แถว Signals (Vissig + VisVAP + RBC Level 3) — ส่วน Vissig/VisVAP | **[TOR 4.1.7.2.1.5.2] Vissig / VisVAP** |
| แถวเดียวกัน — RBC Level 3 | **[TOR 4.1.7.2.1.5.3] RBC Level 3** |

ถ้าจะใช้ภาพเดียวอธิบายข้อที่ไม่ได้เป็นสีเขียวด้วย สามารถมาร์คเพิ่ม:
- Managed Lanes → 4.1.7.2.1.5.4
- Dynamic Assignment → 4.1.7.2.1.5.5
- Public Transport → 4.1.7.2.1.5.6
- COM → 4.1.7.2.1.5.7
- Meso → 4.1.7.2.1.5.8

ดู transcription ที่ [PTV_VISSIM_MATRIX_MARKED.md](../evidence/PTV_VISSIM_MATRIX_MARKED.md)

---

# 4. ภาพ Academic License Package Inclusions

## บริเวณ PTV Vissim

| ตำแหน่ง | Callout |
|---|---|
| หัวคอลัมน์ PTV Vissim | **[TOR 4.1.7.2.2.1] Microscopic Traffic Simulation** |
| รายการ model capability | **[TOR 4.1.7.2.2.1.1] Road / junction / lane / vehicle / signal model** |
| Network Size 1.5 km × 1.5 km + 3 signalized intersections | Context: 4.1.7.2.2.1.2 |
| Viswalk 1,000 pedestrians | Context: 4.1.7.2.2.2.3 |

สำหรับ **4.1.7.2.2.1.5** ให้มาร์คหัว package แล้วแนบ PTV Academia page เพิ่ม เพราะข้อ TOR พูดถึง “ใช้ประกอบการเรียนการสอน”

## บริเวณ PTV Visum

| ตำแหน่ง | Callout |
|---|---|
| หัวคอลัมน์ PTV Visum / 100 zones | **[TOR 4.1.7.2.2.1.9] Transport planning / demand / assignment** + official Visum source |
| 100 zones | Context: 4.1.7.2.2.1.8 |

## บริเวณ PTV Vistro

| ตำแหน่ง | Callout |
|---|---|
| หัวคอลัมน์ PTV Vistro | **[TOR 4.1.7.2.2.3] Traffic engineering analysis/design** |
| 400 zones / 10,000 nodes / 24,000 links | Context: 4.1.7.2.2.3.1 |

ข้อ 4.1.7.2.2.3.2 ถึง .3.5 ต้องแนบ official Vistro UI/Menu/Report pages เพิ่ม ไม่ควรใช้ตัวเลข network size อย่างเดียวไปตอบ

## แถวล่างสุด 25 users / 36 months

มาร์ค **สองเลขพร้อมกัน**:

- **[TOR 4.1.7.2.2] 25-seat Academic Package**
- **[TOR 4.1.7.2.2.5] 25 users / 36 months — PARTIAL: ต้องยืนยัน subscription model จาก quotation/license schedule**

ดู transcription ที่ [PTV_ACADEMIC_PACKAGE_MARKED.md](../evidence/PTV_ACADEMIC_PACKAGE_MARKED.md)

---

# 5. SIDRA evidence — วิธีมาร์คหน้าเว็บ/คู่มือ

แนะนำ print-to-PDF หน้า official แล้วใส่ callout ตาม section ต่อไปนี้

## SIDRA Network Model page

มาร์ค:
- [TOR 4.1.7.2.3.1] Lane-Based Analysis
- [TOR 4.1.7.2.3.2] Integrated analytical framework / all site types
- [TOR 4.1.7.2.3.3] 12 Movement Classes
- [TOR 4.1.7.2.3.6.1] Up to 50 Sites
- [TOR 4.1.7.2.3.6.2] Lane-based network model
- [TOR 4.1.7.2.3.6.3] Queue Spillback / backward spread
- [TOR 4.1.7.2.3.6.4] Site / Network templates
- [TOR 4.1.7.2.3.8.3] Lane-based platoons / midblock lane changes
- [TOR 4.1.7.2.3.9.1] Fuel / emissions / operating cost
- [TOR 4.1.7.2.3.9.2] Four-mode elemental model
- [TOR 4.1.7.2.3.9.3] CO2 / CO / HC / NOx

## SIDRA Getting Started page

มาร์ค:
- [TOR 4.1.7.2.3.4] Full User Guide
- [TOR 4.1.7.2.3.5.1.2] Up to 8 legs
- [TOR 4.1.7.2.3.6.1] Up to 50 Sites / mixed intersections

## SIDRA facilities page

มาร์ค:
- [TOR 4.1.7.2.3.5.1.1] Fixed-time / actuated
- [TOR 4.1.7.2.3.5.2.1] Two-Way Stop
- [TOR 4.1.7.2.3.5.2.2] All-Way Stop
- [TOR 4.1.7.2.3.5.2.3] Give-Way / Yield
- [TOR 4.1.7.2.3.5.4] Signalised/unsignalised pedestrian crossings
- [TOR 4.1.7.2.3.7.3] Unsignalised / metering / fully-signalised roundabouts

## SIDRA HCM page

มาร์ค:
- [TOR 4.1.7.2.3.5.1.3] Variable phasing / multiple sequences
- [TOR 4.1.7.2.3.5.1.4] Turn On Red
- [TOR 4.1.7.2.3.8.1] Critical Movement Identification
- [TOR 4.1.7.2.3.8.2] Advanced signal phasing
- [TOR 4.1.7.2.3.8.3] Platoon progression
- [TOR 4.1.7.2.3.8.4] Common Control Groups
- [TOR 4.1.7.2.3.8.5] Interactive Offsets / Time-Distance
- [TOR 4.1.7.2.3.10.1] HCM calibration + Metric / US units
- [TOR 4.1.7.2.3.10.2] HCM Edition 7 compatibility
- [TOR 4.1.7.2.3.10.3] HCM research / NCHRP involvement
- [TOR 4.1.7.2.3.10.4] Extensions beyond HCM
- [TOR 4.1.7.2.3.10.5] HCM / NCHRP / international references

## SIDRA Where is INPUT? page

มาร์ค:
- [TOR 4.1.7.2.3.5.1.4] Turn On Red
- [TOR 4.1.7.2.3.5.4] Diagonal Crossing / Slip-Bypass Lane Crossing
- [TOR 4.1.7.2.3.8.5] Interactive Offsets / Time-Distance Display

## SIDRA ASSIGN page

มาร์ค:
- [TOR 4.1.7.2.3.6.5] SIDRA ASSIGN integration — **PARTIAL**
- เพิ่ม note: “technical integration found; no-extra-license-fee wording requires quotation/license schedule”

---

# 6. ข้อที่ไม่ควรมาร์คเป็น FOUND ด้วย webpage อย่างเดียว

ให้คงสถานะ **VENDOR DOC** จนกว่าจะมีเอกสารเชิงพาณิชย์:

- 4.1.7.2.1.4
- 4.1.7.2.1.5.9
- 4.1.7.2.1.5.10
- 4.1.7.2.2.6
- 4.1.7.2.3.11
- 4.1.7.2.3.12

และคง **PARTIAL** สำหรับ:
- 4.1.7.2.2.5 — exact users/duration พบแล้ว แต่ subscription wording ยังต้องยืนยัน
- 4.1.7.2.3.5.3 — ยังไม่พบ exact support ครบทุก named innovative design โดยเฉพาะ P-Turn
- 4.1.7.2.3.6.5 — integration พบ แต่ “ไม่มีค่า license เพิ่ม” ต้องยืนยัน
- 4.1.7.2.3.7.1 — official source ที่พบระบุ 4 roundabout capacity model options ชัด ยังไม่พบหลักฐาน ≥5

---

# 7. Naming convention ตอนจัดไฟล์ส่ง

แนะนำชื่อไฟล์:

- E01_PTV_Vissim_Advanced_Package_Marked.pdf
- E02_PTV_Vissim_Signals_Advanced_Marked.pdf
- E03_PTV_Academic_Package_Marked.pdf
- E04_PTV_Academia_Official_Marked.pdf
- E05_PTV_Viswalk_Official_Marked.pdf
- E06_PTV_Vistro_UI_Report_Marked.pdf
- E07_SIDRA_Network_Model_Marked.pdf
- E08_SIDRA_Facilities_Marked.pdf
- E09_SIDRA_Signal_Timing_Marked.pdf
- E10_SIDRA_HCM_Marked.pdf
- E11_SIDRA_ASSIGN_Marked.pdf
- E12_Vendor_Authorization_and_License_Schedule.pdf

เลข E01–E12 ใช้อ้างใน cover sheet หรือ evidence matrix ได้ทันที
