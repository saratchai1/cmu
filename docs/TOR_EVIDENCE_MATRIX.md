# TOR 4.1.7 Evidence Matrix

ตารางนี้ map **ทุกหมายเลขข้อที่ไฮไลต์สีเขียวใน TOR** กับเอกสารที่พบและ action ที่ต้องทำต่อ

## Status summary

| Status | Count | Definition |
|---|---:|---|
| FOUND | 66 | พบ technical/official evidence รองรับสาระสำคัญของข้อ |
| PARTIAL | 4 | พบเพียงบางส่วน ยังต้องหา exact evidence เพิ่ม |
| VENDOR DOC | 6 | ต้องใช้เอกสารเชิงพาณิชย์/สิทธิ์ใช้งาน/หนังสือจากผู้ผลิตหรือตัวแทน |
| **Total** | **76** | |

> การระบุ FOUND หมายถึง “พบหลักฐานรองรับสำหรับทำ evidence pack” ไม่ใช่การตัดสินผลการจัดซื้อหรือรับรอง compliance ขั้นสุดท้าย

Source ID ดูรายละเอียดและ URL ได้ใน [SOURCE_REGISTER.md](SOURCE_REGISTER.md)

---

# A. 4.1.7.2.1 — Microscopic Traffic Simulation / PTV Vissim

| TOR | Requirement summary | Status | Evidence / explanation | Source |
|---|---|---|---|---|
| 4.1.7.2.1. | ซอฟต์แวร์สร้าง/จำลองการจราจรระดับจุลภาค | FOUND | PTV Vissim official ระบุ microscopic, multimodal traffic simulation | PTV-01, PTV-05 |
| 4.1.7.2.1.1. | GUI ครบถ้วน | FOUND | ภาพ package มีแถว GUI และ PTV official ระบุ intuitive graphical user interface | U-PTV-01, PTV-01, PTV-05 |
| 4.1.7.2.1.4. | License ถูกกฎหมายและได้รับสิทธิ์จากเจ้าของ/ตัวแทน | VENDOR DOC | Webpage ยืนยัน feature ไม่แทน authorization/license certificate | ขอ Manufacturer Authorization / Reseller Letter / License Certificate |
| 4.1.7.2.1.5. | คุณลักษณะไม่น้อยกว่ารายการที่กำหนด | FOUND | Vissim Advanced เป็น full-feature package และมี feature หลักตาม TOR | U-PTV-01, PTV-02 |
| 4.1.7.2.1.5.1. | Unlimited Signals | FOUND | ภาพระบุ Vissim Advanced = unlimited; official pricing ระบุ unlimited traffic signal control | U-PTV-01, PTV-02 |
| 4.1.7.2.1.5.2. | Vissig + VisVAP หรือเทียบเท่า | FOUND | Signals Advanced official help ระบุ Vissig, VAP, VisVAP | U-PTV-01, PTV-03 |
| 4.1.7.2.1.5.3. | RBC Level 3 หรือสูงกว่า | FOUND | ภาพ package ระบุ RBC Level 3; official help ระบุ RBC Level 3 ใน Signals Advanced สำหรับ North American market | U-PTV-01, PTV-03 |
| 4.1.7.2.1.5.9. | Subscription ≥ 3 ปี, ≥ 1 สิทธิ์ | VENDOR DOC | ต้องยืนยัน configuration ที่เสนอจริง จำนวนสิทธิ์ และ term จาก quotation/license schedule | Vendor quotation / license schedule |
| 4.1.7.2.1.5.10. | Update เป็นรุ่นล่าสุดตลอดสัญญา | VENDOR DOC | ต้องมี update/upgrade entitlement ที่ผูกกับ subscription term | Vendor subscription/update terms |

### Marking note
ภาพ PTV Vissim ที่ส่งมาควรมาร์คเลข **4.1.7.2.1.1, 4.1.7.2.1.5.1, 4.1.7.2.1.5.2, 4.1.7.2.1.5.3** โดยตรง  
ดู [PTV_VISSIM_MATRIX_MARKED.md](../evidence/PTV_VISSIM_MATRIX_MARKED.md)

---

# B. 4.1.7.2.2 — Academic License Package

| TOR | Requirement summary | Status | Evidence / explanation | Source |
|---|---|---|---|---|
| 4.1.7.2.2. | Academic Package สำหรับสอน, 25 ที่นั่ง | FOUND | ภาพระบุ Academic License Package, 25 users, 36 months; PTV Academia ระบุ suite สำหรับ teaching/classroom/student projects | U-PTV-02, PTV-04 |
| 4.1.7.2.2.1. | โปรแกรม microscopic traffic simulation | FOUND | Academic Package มี PTV Vissim; official Vissim เป็น microscopic simulation | U-PTV-02, PTV-01, PTV-04 |
| 4.1.7.2.2.1.1. | สร้าง road/junction/lane/vehicle/signal model | FOUND | PTV Vissim เป็น network-based microscopic traffic simulator และรองรับ road users/signals | PTV-01, PTV-05 |
| 4.1.7.2.2.1.5. | ใช้สอน intersection/control/capacity/traffic impact | FOUND | PTV Academia ระบุใช้ teaching/classroom/student projects; Vissim ใช้ traffic performance และ signal planning | PTV-04, PTV-05 |
| 4.1.7.2.2.1.9. | ใช้สอน transport planning/demand/distribution/assignment | FOUND | Academic Package มี Visum; Visum official help มี transport demand, OD matrices, assignment | U-PTV-02, PTV-04, PTV-10 |
| 4.1.7.2.2.2.2. | Pedestrian simulation ในทางเดิน/อาคาร/สถานี/พื้นที่สาธารณะ | FOUND | Vissim/Viswalk official material ระบุ station, airport, large buildings, event/crowd environments | PTV-05, PTV-06 |
| 4.1.7.2.2.2.4. | กำหนดพื้นที่เดิน, origin, destination, route, flow | FOUND | Official Viswalk/Vissim help มี pedestrian inputs, area, routes, origins/destinations และ OD demand | PTV-07, PTV-08, PTV-09 |
| 4.1.7.2.2.2.5. | แสดง movement/density/distribution ของคนเดินเท้า | FOUND | Viswalk มี simulation/evaluation/visualisation และ route-choice/density tools | PTV-06, PTV-08 |
| 4.1.7.2.2.2.6. | ใช้สอน pedestrian design/density/evacuation/crowd/transit | FOUND | PTV Viswalk material ระบุ crowd/evacuation; PTV Academia ระบุ academic teaching use | PTV-04, PTV-06 |
| 4.1.7.2.2.3. | โปรแกรมวิเคราะห์/ออกแบบวิศวกรรมจราจร | FOUND | Academic Package ระบุ PTV Vistro พร้อม network limits; Vistro official help เป็น network/intersection analysis interface | U-PTV-02, PTV-11 |
| 4.1.7.2.2.3.2. | GUI สำหรับ create/edit/process/display | FOUND | Vistro UI มี network window, graphical build/edit, workflow/data/display panes | PTV-11 |
| 4.1.7.2.2.3.3. | ใช้สร้าง model สำหรับ classroom/lab | FOUND | Vistro อยู่ใน Academic Package ซึ่ง PTV ระบุใช้ teaching/classroom/student projects | U-PTV-02, PTV-04 |
| 4.1.7.2.2.3.4. | Save/Open/Edit/Process model files | FOUND | Vistro Menu Bar มี New, Open, Save, Save As และ workflow processing | PTV-12 |
| 4.1.7.2.2.3.5. | แสดงผลภาพ/ตาราง/กราฟ/แผนผัง/animation ตาม software | FOUND | Vistro Report Layout รองรับ tabular/graphical reports และ network/map figures; Vissim/Viswalk มี simulation visualisation | PTV-13, PTV-05, PTV-06 |
| 4.1.7.2.2.4. | ติดตั้ง/เข้าใช้ตาม license model และจำนวนสิทธิ์ที่ซื้อ | FOUND | ภาพ package ระบุ 25 users; official Academic Package เป็น license/access offering ของ PTV | U-PTV-02, PTV-04 |
| 4.1.7.2.2.5. | Subscription ≥ 3 ปี, ≥ 25 สิทธิ์ | PARTIAL | พบ **25 users / 36 months** และ official page ระบุ three-year access แต่ภาพ/หน้า academia ไม่ยืนยันคำว่า annual Subscription ของ configuration ที่จะเสนอ | U-PTV-02, PTV-04 + ต้องมี quotation/license schedule |
| 4.1.7.2.2.6. | Update เป็นรุ่นล่าสุดตลอดสัญญา | VENDOR DOC | ต้องมี statement/update entitlement สำหรับ Academic Package ที่เสนอจริง | Vendor subscription/maintenance terms |

### Marking note
ตรง **25 users / 36 months** ในภาพ Academic Package ให้มาร์ค:
- 4.1.7.2.2
- 4.1.7.2.2.5 (PARTIAL — ต้องแนบ commercial license document เพิ่ม)

ดู [PTV_ACADEMIC_PACKAGE_MARKED.md](../evidence/PTV_ACADEMIC_PACKAGE_MARKED.md)

---

# C. 4.1.7.2.3 — SIDRA / Intersection & Network Analysis

## C1. Core model, movement classes, manual

| TOR | Requirement summary | Status | Evidence / explanation | Source |
|---|---|---|---|---|
| 4.1.7.2.3. | ออกแบบ/ประเมิน intersection และ network หลายจุด | FOUND | SIDRA official ระบุ single intersections และ networks, up to 50 sites | SIDRA-01, SIDRA-02 |
| 4.1.7.2.3.1. | Lane-Based Analysis | FOUND | SIDRA Network Model ระบุ unique lane-based micro-analytical model | SIDRA-01 |
| 4.1.7.2.3.2. | วิเคราะห์หลาย intersection types ภายใต้ framework เดียว | FOUND | SIDRA ระบุ all site types/network configurations และ integrated performance framework | SIDRA-01, SIDRA-05 |
| 4.1.7.2.3.3. | Movement Classes ≥ 12; standard + ≥6 user-defined | FOUND | Official Network Model ระบุ Light, Heavy, Buses, Bicycles, Large Trucks, Light Rail/Trams + 6 user-configured classes | SIDRA-01 |
| 4.1.7.2.3.4. | User Guide/Help + Metric/US Customary | FOUND | Full User Guide อยู่ใน software; HCM setup รองรับ US Customary และ Metric | SIDRA-02, SIDRA-01, SIDRA-05 |

## C2. Signalised and sign-controlled intersections

| TOR | Requirement summary | Status | Evidence / explanation | Source |
|---|---|---|---|---|
| 4.1.7.2.3.5. | Intersection Analysis | FOUND | Official SIDRA facility/model pages ครอบคลุม signals, roundabouts, sign control, pedestrian crossings, interchanges | SIDRA-01, SIDRA-13 |
| 4.1.7.2.3.5.1. | Signalised Intersections | FOUND | Official facilities page ระบุ signalised intersections and networks | SIDRA-13 |
| 4.1.7.2.3.5.1.1. | Fixed-Time + Actuated Control | FOUND | Official facilities/HCM pages ระบุ fixed-time/pretimed และ actuated | SIDRA-13, SIDRA-05 |
| 4.1.7.2.3.5.1.2. | ≥ 8 legs | FOUND | Getting Started ระบุ configure geometry ได้ up to 8 legs | SIDRA-02 |
| 4.1.7.2.3.5.1.3. | Variable Phasing + Multiple Phase Sequences | FOUND | HCM page ระบุ variable phasing, multiple green periods และ multiple phase sequences | SIDRA-05 |
| 4.1.7.2.3.5.1.4. | Turn On Red | FOUND | HCM page และ Where is INPUT? ระบุ Turn On Red | SIDRA-03, SIDRA-05 |
| 4.1.7.2.3.5.1.5. | Permitted-Protected Turns | FOUND | Signal timing/HCM framework รองรับ permitted/filter turns และ advanced phasing; ใช้ current User Guide เป็นหลักฐานประกอบเมื่อจัดชุดส่ง | SIDRA-05, SIDRA-06 |
| 4.1.7.2.3.5.2. | Sign-Controlled Intersections | FOUND | Official facilities page มี Sign control | SIDRA-13 |
| 4.1.7.2.3.5.2.1. | Two-Way Stop | FOUND | Official facilities page ระบุ two-way stop sign control | SIDRA-13 |
| 4.1.7.2.3.5.2.2. | All-Way Stop | FOUND | Official facilities page ระบุ all-way stop; version history/updates รองรับ model | SIDRA-13 |
| 4.1.7.2.3.5.2.3. | Give-Way/Yield Control | FOUND | Official facilities page ระบุ two-way give-way/yield; HCM extension page ระบุ Two-Way Yield modelling | SIDRA-13, SIDRA-09 |
| 4.1.7.2.3.5.3. | Innovative designs: DDI, RCUT, CFI, DLT, MUT, P-Turn, Divergabout | PARTIAL | Official page ยืนยัน DDI, Divergabout, CFI, RCUT และ other variations แต่รอบนี้ยังไม่พบหน้า official ที่ enumerate ครบทุกชื่อใน TOR โดยเฉพาะ P-Turn | SIDRA-13 + ขอ current template list/User Guide screenshot |
| 4.1.7.2.3.5.4. | Pedestrian crossings: signal/no-signal, midblock, staged, slip, diagonal | FOUND | Facilities page มี signalised/unsignalised, staged, slip/bypass, midblock; official input index มี Diagonal Crossing | SIDRA-03, SIDRA-13 |

## C3. Network Model

| TOR | Requirement summary | Status | Evidence / explanation | Source |
|---|---|---|---|---|
| 4.1.7.2.3.6. | Network Model | FOUND | SIDRA official มี lane-based Network Model โดยตรง | SIDRA-01 |
| 4.1.7.2.3.6.1. | ≥ 50 sites; mixed intersection types | FOUND | Network Model/Getting Started ระบุ up to 50 Sites และผสม signal/roundabout/sign control ได้ | SIDRA-01, SIDRA-02, SIDRA-13 |
| 4.1.7.2.3.6.2. | คง lane-based detail ไม่ใช่ link/lane-group aggregate | FOUND | Official Network Model เปรียบเทียบชัดว่าเป็น lane-based micro-analytical ต่างจาก link/lane-group/approach models | SIDRA-01 |
| 4.1.7.2.3.6.3. | Queue Spillback / Backward Spread of Congestion | FOUND | Official Network Model ระบุ queue spillback และ backward spread of congestion | SIDRA-01 |
| 4.1.7.2.3.6.4. | Templates สำหรับโครงสร้างซับซ้อน | FOUND | Official Network Model/Get Started ระบุ Site and Network Templates / pre-configured templates | SIDRA-01, SIDRA-02 |
| 4.1.7.2.3.6.5. | Network analysis + Traffic Assignment engine เดียว, no export/conversion, no extra license fee | PARTIAL | SIDRA ASSIGN official ยืนยัน integration กับ detailed lane-based Network Model; แต่ข้อความ “ไม่มีค่าใช้จ่าย license เพิ่ม” ต้องยืนยันด้วย commercial document | SIDRA-07, SIDRA-08 + vendor license schedule |

## C4. Roundabouts

| TOR | Requirement summary | Status | Evidence / explanation | Source |
|---|---|---|---|---|
| 4.1.7.2.3.7. | Roundabout Analysis | FOUND | SIDRA มี dedicated roundabout models and extensions | SIDRA-05, SIDRA-09, SIDRA-13 |
| 4.1.7.2.3.7.1. | Capacity Models ≥ 5; รวม SIDRA Standard, HCM 6, HCM 6 Extended, HCM 2010 | PARTIAL | Official HCM page enumerate 4 options ตรงชื่อดังกล่าว; HCM Edition 7 ใช้ model เดียวกับ HCM 6 จึงไม่ควรนับเป็นตัวที่ 5 โดยไม่มีหลักฐานเพิ่ม | SIDRA-05 + ขอ User Guide/dialog screenshot ที่ยืนยัน ≥5 |
| 4.1.7.2.3.7.2. | Geometry-sensitive capacity | FOUND | Official HCM page ระบุ SIDRA Standard model sensitive ต่อ roundabout size, circulating road width, entry radius/angle, short lanes ฯลฯ | SIDRA-05, SIDRA-09 |
| 4.1.7.2.3.7.3. | Unsignalised / Metering / Fully Signalised Roundabouts | FOUND | Official facilities pageระบุทั้ง unsignalised, metering signals และ fully-signalised roundabouts | SIDRA-13 |
| 4.1.7.2.3.7.4. | ≥ 18 Roundabout Site Templates | FOUND | Official HCM page ระบุ Site Templates มี 18 different roundabouts | SIDRA-05 |
| 4.1.7.2.3.7.5. | Multi-lane / bypass-slip / turbo / roundabout corridor + spillback | FOUND | HCM/roundabout/network pages รองรับ bypass lanes, turbo roundabout, corridors/network และ queue spillback | SIDRA-01, SIDRA-05, SIDRA-09 |
| 4.1.7.2.3.7.6. | Capacity Constraint / Unbalanced Flow / Upstream Signal Effects | FOUND | Official HCM extension pageระบุทั้งสาม capability | SIDRA-05, SIDRA-09 |

## C5. Signal Timing & Coordination

| TOR | Requirement summary | Status | Evidence / explanation | Source |
|---|---|---|---|---|
| 4.1.7.2.3.8. | Signal Timing & Coordination | FOUND | SIDRA มี dedicated network signal timing/coordination facilities | SIDRA-04, SIDRA-05 |
| 4.1.7.2.3.8.1. | Critical Movement Identification; complex/overlap phasing | FOUND | HCM page ระบุ Unique Critical Movement Identification และ advanced phase/sequence methods; glossary มี Overlap Movement | SIDRA-05, SIDRA-06 |
| 4.1.7.2.3.8.2. | Variable phasing, multiple sequences/greens, TOR, permitted-protected, pedestrian actuation | FOUND | HCM page ระบุ variable phasing, multiple phase sequences, multiple green periods, Turn On Red และ pedestrian actuation | SIDRA-05 |
| 4.1.7.2.3.8.3. | Network Cycle Time, Site Phase Times, Offsets, lane platoons, midblock lane changes | FOUND | Signal Timing page ระบุ Network Cycle Time/Site Phase Times/Offsets; HCM/Network Model ระบุ lane-based platoons และ midblock lane changes | SIDRA-01, SIDRA-04, SIDRA-05 |
| 4.1.7.2.3.8.4. | Common Control Groups | FOUND | Signal Timing/HCM pages ระบุ CCG สำหรับหลาย signalised intersections ภายใต้ controller เดียว | SIDRA-04, SIDRA-05 |
| 4.1.7.2.3.8.5. | Interactive Offsets + two-way Time-Distance + visual feedback | FOUND | Official Signal Timing และ Where is INPUT? มี Interactive Offsets, desired two-way progression และ Time-Distance Display options | SIDRA-03, SIDRA-04, SIDRA-05 |

## C6. Environmental Analysis

| TOR | Requirement summary | Status | Evidence / explanation | Source |
|---|---|---|---|---|
| 4.1.7.2.3.9. | Environmental Analysis | FOUND | SIDRA Network/feature pages ระบุ environmental assessment | SIDRA-01, SIDRA-11 |
| 4.1.7.2.3.9.1. | Fuel / emissions / operating cost เชื่อมกับ delay/stop/travel time model | FOUND | Official material ระบุ capacity/performance, operating cost, fuel/emissions ใน integrated analytical model | SIDRA-01, SIDRA-05, SIDRA-11 |
| 4.1.7.2.3.9.2. | Four-Mode Drive Cycle: cruise/accel/decel/idle | FOUND | Official Network Model ระบุ four-mode elemental model exact | SIDRA-01 |
| 4.1.7.2.3.9.3. | CO2, CO, HC, NOx | FOUND | Official Network Model ระบุ pollutant list exact | SIDRA-01 |
| 4.1.7.2.3.9.4. | Signal timing optimisation โดยอิง environmental measure | FOUND | Current SIDRA ระบุ signal-timing optimisation; technical SIDRA publication อธิบายการเลือก signal settings เพื่อ minimize fuel/cost/pollutant emissions | SIDRA-11, SIDRA-12 |

## C7. Highway Capacity Manual (HCM)

| TOR | Requirement summary | Status | Evidence / explanation | Source |
|---|---|---|---|---|
| 4.1.7.2.3.10. | HCM compatibility | FOUND | Dedicated official HCM page ระบุ compatibility and extensions | SIDRA-05 |
| 4.1.7.2.3.10.1. | HCM calibration + Metric / US Customary | FOUND | HCM setup calibrates model parameters using HCM defaults และรองรับ US Customary / Metric | SIDRA-01, SIDRA-05 |
| 4.1.7.2.3.10.2. | Compatible with latest HCM | FOUND | Official HCM page ระบุ continued compatibility with HCM Edition 7 | SIDRA-05 |
| 4.1.7.2.3.10.3. | Delay/queue model สอดคล้อง HCM และมี involvement ของผู้พัฒนา HCM | FOUND | HCM page ระบุ SIDRA/HCM model compatibility, HCM queue/delay research, actuated method joint work และ NCHRP 3-48 contributions | SIDRA-05, SIDRA-10 |
| 4.1.7.2.3.10.4. | Extensions beyond HCM | FOUND | Official HCM page ระบุ lane-based network, queue spillback, multiple roundabout models, CCG, environmental models ฯลฯ | SIDRA-05, SIDRA-09 |
| 4.1.7.2.3.10.5. | อ้างอิง/ยอมรับโดย HCM, NCHRP, FHWA, Austroads หรือแหล่งสากล | FOUND | Official HCM/Projects pages มี HCM research contributions, NCHRP Project 3-48 และ Austroads-funded/revision work | SIDRA-05, SIDRA-10 |

## C8. SIDRA licensing

| TOR | Requirement summary | Status | Evidence / explanation | Source |
|---|---|---|---|---|
| 4.1.7.2.3.11. | Subscription ≥ 3 ปี, ≥ 1 สิทธิ์ | VENDOR DOC | ต้องยืนยัน configuration/quantity/term ที่เสนอจริง | Vendor quotation / license schedule |
| 4.1.7.2.3.12. | Update เป็นรุ่นล่าสุดตลอดสัญญา | VENDOR DOC | Version 11 material แสดง upgrade mechanism แต่ entitlement ตลอดสัญญาที่เสนอจริงต้องมาจาก subscription/COVER terms | SIDRA-08 + vendor subscription/COVER terms |

---

# D. Open points that must not be overclaimed

## PARTIAL — 4 clauses

### 4.1.7.2.2.5
พบ 25 users / 36 months และ three-year academic access แล้ว แต่ต้องมีเอกสารที่ยืนยัน license/subscription model ของ configuration ที่เสนอ

### 4.1.7.2.3.5.3
พบ official support สำหรับ alternative intersections หลายชนิด แต่ยังไม่พบหลักฐาน official ที่ enumerate รายชื่อใน TOR ครบทุกตัว โดยเฉพาะ P-Turn

### 4.1.7.2.3.6.5
พบ technical integration ของ SIDRA ASSIGN + lane-based Network Model แล้ว แต่ “no additional licence fee” เป็นข้อเชิงพาณิชย์ ต้องยืนยันจาก quotation/license schedule

### 4.1.7.2.3.7.1
official HCM page ที่ตรวจพบระบุ roundabout capacity model options ชัด 4 แบบ:
- SIDRA Standard (HCM)
- HCM 6
- HCM 6 Extended
- HCM 2010

TOR ต้องการ **ไม่น้อยกว่า 5 แบบ** จึงต้องขอหลักฐานเพิ่มจาก current User Guide/software dialog หรือ manufacturer declaration

---

# E. VENDOR DOC — 6 clauses

1. 4.1.7.2.1.4 — authorization/legal license
2. 4.1.7.2.1.5.9 — Vissim 3-year subscription / seat
3. 4.1.7.2.1.5.10 — Vissim update entitlement
4. 4.1.7.2.2.6 — Academic Package update entitlement
5. 4.1.7.2.3.11 — SIDRA 3-year subscription / seat
6. 4.1.7.2.3.12 — SIDRA update entitlement

ดู [VENDOR_DOCUMENT_CHECKLIST.md](VENDOR_DOCUMENT_CHECKLIST.md)

---

# F. Submission recommendation

เพื่อให้ชุด evidence ใช้งานได้จริงในการตรวจ TOR:

1. ใช้ matrix นี้เป็น cover/index
2. print-to-PDF official webpages ตาม Source ID
3. มาร์คเลข TOR ในแต่ละหน้า evidence
4. แนบ screenshot package ที่ส่งมาเป็น E01/E03
5. แนบ quotation/license schedule/authorization เป็นเอกสารท้ายชุด
6. ข้อ PARTIAL ให้ปิด gap ก่อนเปลี่ยนสถานะเป็น FOUND
7. ตรวจว่ารุ่น software ใน evidence ตรงกับรุ่นที่เสนอจริง
