# PTV Vissim Package Matrix — Marked Transcription

Source: ภาพตาราง **PTV Vissim Junction / PTV Vissim Corridor / PTV Vissim Advanced** ที่ส่งมาในชุดเอกสาร

ไฟล์นี้ถอดเฉพาะข้อมูลที่อ่านได้ชัดจากภาพ และใส่เลข TOR ที่ควรมาร์คกำกับเพื่อใช้เป็นไกด์

## จุดที่ควรมาร์คบนภาพต้นฉบับ

| ตำแหน่ง/ข้อความในภาพ | PTV Vissim Junction | PTV Vissim Corridor | PTV Vissim Advanced | เลข TOR ที่ควรมาร์ค |
|---|---:|---:|---:|---|
| Package signal count | 10 Signals | 20 Signals | **unlimited** | **4.1.7.2.1.5.1** |
| GUI | ✓ | ✓ | ✓ | **4.1.7.2.1.1** |
| Signals unlimited size | — | — | ✓ | **4.1.7.2.1.5.1** |
| Signals (Vissig + VisVAP + RBC Level 3) | — | ✓ | ✓ | **4.1.7.2.1.5.2**, **4.1.7.2.1.5.3** |
| Public Transport | — | ✓ | ✓ | ใช้เสริม 4.1.7.2.1.5.6 |
| COM (Event Based Scripts etc.) | — | ✓ | ✓ | ใช้เสริม 4.1.7.2.1.5.7 |
| Meso | — | — | ✓ | ใช้เสริม 4.1.7.2.1.5.8 |
| Dynamic Assignment | — | — | ✓ | ใช้เสริม 4.1.7.2.1.5.5 |
| Managed Lanes | — | ✓ | ✓ | ใช้เสริม 4.1.7.2.1.5.4 |

> เครื่องหมาย “—” หมายถึงช่องที่ไม่เห็นเครื่องหมายรองรับในภาพที่ส่งมา ไม่ได้หมายถึงการยืนยันว่า product ไม่มี feature นั้นในทุก configuration

## Markup recommendation

ให้ใส่ callout สั้น ๆ บนภาพดังนี้:

1. ข้างคำว่า **GUI** → [4.1.7.2.1.1]
2. ข้างหัวคอลัมน์ **PTV Vissim Advanced – unlimited** → [4.1.7.2.1.5.1]
3. ข้างแถว **Signals (Vissig + VisVAP + RBC Level 3)**:
   - [4.1.7.2.1.5.2] Vissig / VisVAP
   - [4.1.7.2.1.5.3] RBC Level 3
4. ถ้าต้องการใช้ภาพเดียวช่วยตอบ feature อื่นที่ไม่ได้ไฮไลต์ ให้ใส่เลขข้อเล็ก ๆ ข้าง Public Transport, COM, Meso, Dynamic Assignment และ Managed Lanes ตามตารางด้านบน

## Supporting official documents

ใช้ไฟล์นี้คู่กับ:
- PTV-01 — PTV Vissim product page
- PTV-02 — PTV Vissim Pricing & Licensing
- PTV-03 — Vissim Help: Overview of add-on modules

ดู URL เต็มใน [SOURCE_REGISTER.md](../docs/SOURCE_REGISTER.md)

## ข้อควรระวัง

ภาพนี้ **ไม่เพียงพอ** สำหรับ:
- 4.1.7.2.1.4 การยืนยันลิขสิทธิ์ถูกต้อง/ตัวแทนได้รับอนุญาต
- 4.1.7.2.1.5.9 subscription อย่างน้อย 3 ปี / อย่างน้อย 1 สิทธิ์
- 4.1.7.2.1.5.10 สิทธิ์อัปเดตเป็นรุ่นล่าสุดตลอดสัญญา

สามประเด็นนี้ควรมีหนังสือจากผู้ผลิต/ตัวแทนหรือ quotation/license schedule
