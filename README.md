# Rover Circuit

## Requirements

---

### General Requirements

### Mechanical Requirements

### Electrical Requirements

### Functional Requirements


### 2. General Board Overview

* **Application**: Robot rover controller with battery charging and motor driving capabilities.
* **Target Enclosure**: Custom 3D-printed case with mounting points for motors, battery, and sensors.
* **Operating Temperature Range**: -20 °C to +60 °C.

---

### 3. Mechanical Requirements

* **Board Dimensions**: ?? mm × ?? mm (to fit within the enclosure).
* **Mounting Holes**: 4 holes for M2 screws, located at the two sides of the board.
* **Thickness**: Standard 1.6 mm PCB thickness.
* **Keep-out Zones**: 5 mm from the edges for mounting clearance; No components in the center bottom side (battery slot). No components closer than 3 mm to the mounting holes.

---

### 4. Electrical Requirements

#### 4.1 Power Domains
* **Input Voltage**: Two-cell Li-ion battery (7.4 V nominal) with USB-C charging support.
* **Internal Voltage Rails**: 3.3 V for logic and sensors, 6 V for motors, and regulated 5 V for external Raspberry Pi connection.
* **Current Requirements**: Up to 2 A for motors, 1 A for sensors and logic.

#### 4.2 Interfaces
* **I2C**: For communication with sensors and battery management.
* **GPIO**: For motor control signals and status LEDs.
* **USB-C**: For charging and potential data communication with a host computer.
* **Motor Outputs**: Two H-bridge outputs for controlling two DC motors.

# Components BOM


### BQ25887 -- Charger 2S boost + Cell Balancing

| Rif.     | Qtà | Funzione                             | Specifica / valore da montare                                       | Package          | Codice JLCPCB/LCSC                     |
| -------- | --: | ------------------------------------ | ------------------------------------------------------------------- | ---------------- | -------------------------------------- |
| U1       |   1 | Charger 2S boost + bilanciamento     | TI **BQ25887RGER**, QFN-24-EP 4×4                                   | QFN-24-EP(4×4)   | **C2761614** ([LCSC Electronics][1])   |
| L1       |   1 | Induttore boost | **1 µH**, molded/shielded, **Irms 12 A**, **Isat 15 A**, **DCR 7.4 mΩ**, ±20%            | **SMD 7×6.6 mm** | **C167216**                            |
| C_VBUS   |   1 | Capacitore ingresso VBUS             | **1 µF**, 25 V, X5R/X7R, ≥1 µF vicino al pin VBUS                   | 0603             | **C5673**                              |
| C_PMID   |   2 | Capacitori nodo PMID                 | **22 µF ciascuno**, 25 V, X5R, ±10%; totale nominale 44 µF          | 1206             | **C12891**                             |
| C_SNS    |   2 | Capacitori uscita SNS                | **22 µF ciascuno**, 25 V, X5R, ±10%; totale nominale 44 µF          | 1206             | **C12891**                             |
| C_BAT    |   1 | Capacitore BAT                       | **22 µF**, 25 V, X5R, ±10%; ≥10 µF effettivi dopo derating          | 1206             | **C12891**                             |
| C_REGN   |   1 | Bypass REGN                          | **4.7 µF**, 10 V, X5R                                               | 0402             | **C23733**                             |
| C_BTST   |   1 | Bootstrap BTST–SW                    | **47 nF**, 50 V, X7R, ±10%                                          | 0603             | **C1622**                              |
| R_ILIM   |   1 | Limite corrente ingresso hardware    | **383 Ω**, 1%, 62.5 mW; IINMAX ≈2.9 A tipico                        | 0402             | **C276269**                            |
| R_MID    |   1 | Protezione pin MID                   | **300 Ω**, ±5% o migliore, 62.5 mW                                  | 0402             | **C4089106**                           |
| R_CBSET  |   1 | Corrente bilanciamento celle         | **10 Ω**, 3 W, ±1%; ICB ≈382 mA @ VCELL=4.2 V e RDSON≈1 Ω; P≈1.46 W | 2512 / 6432      | **C2992634**                           |
| R_TS_TOP |   1 | Rete TS verso REGN                   | **5.23 kΩ**, 1%, 62.5 mW; valore vicino a RT1=5.24 kΩ da datasheet  | 0402             | **C477746** ([Texas Instruments][3])   |
| R_TS_BOT |   1 | Rete TS verso GND                    | **30.1 kΩ**, 1%, 62.5 mW; valore vicino a RT2=30.31 kΩ da datasheet | 0402             | **C138009** ([Texas Instruments][3])   |
| NTC_TS   |   1 | Termistore batteria TS               | **NTC 10 kΩ @25 °C**, famiglia Semitec 103AT, B25/85≈3435 K, ±1%    | Probe / batteria | **C20481054** ([Texas Instruments][3]) |
| R_PULLUP |   5 | Pull-up SDA, SCL, INT, PG, STAT      | **10 kΩ**, 1%, verso rail logico host                               | 0402             | **C25744**                             |
| R_CFG    | 1–2 | Strap PSEL/CD se non pilotati da MCU | **0 Ω**, 62.5 mW; usare per fissare PSEL/CD secondo progetto        | 0402             | **C17168**                             |

[1]: https://www.lcsc.com/product-detail/C2761614.html?utm_source=chatgpt.com "BQ25887RGER | TI | Price | In Stock"
[2]: https://www.lcsc.com/product-detail/C435392.html?utm_source=chatgpt.com "DFE252012F-1R0M=P2 | muRata | Price | In Stock"
[3]: https://www.ti.com/lit/ds/symlink/bq25887.pdf "BQ25887 I2C Controlled 2-Cell, 2-A Boost-Mode Battery	 Charger With Cell	 Balancing For USB	 Input datasheet (Rev. B)"

### DRV8833 -- Motor Driver

| Rif.    | Qtà | Funzione                         | Specifica / valore da montare                                      | Package           | Codice JLCPCB/LCSC                   |
| ------- | --: | -------------------------------- | ------------------------------------------------------------------ | ----------------- | ------------------------------------ |
| U1      |   1 | Driver dual H-bridge             | DRV8833, versione 1.5 A RMS per ponte                              | HTSSOP-16 / PWP   | **DRV8833PWPR / C50506**             |
| C_VM1   |   1 | Decoupling alimentazione motori  | 10 µF, 25 V, X5R/X7R                                               | 0805              | **CL21A106KAYNNNE / C15850**         |
| C_VM2   |   1 | Bulk alimentazione motori        | 100 µF, 16 V, low ESR                                              | SMD elettrolitico | **RVE1C101M0605 – C88658**           |
| C_VINT  |   1 | Condensatore regolatore interno  | 2.2 µF, 16 V                                                       | 0603              | **CL10A225KO8NNNC / C23630**         |
| C_VCP   |   1 | Condensatore charge pump         | 10 nF, 50 V, X7R, tra VCP e VM                                     | 0603              | **CL10B103KB8NNNC / C1589**          |
| C_LOGIC |   1 | Decoupling logica                | 100 nF, 50 V, X7R                                                  | 0603              | **CC0603KRX7R9BB104 / C14663**       |
| R_AISEN |   1 | Sense corrente motore A          | 0.20 Ω, 1%, ≥1 W; limite corrente circa 1 A                        | 2512              | **HoYLR2512-3W-200mR-1% / C5375488** |
| R_BISEN |   1 | Sense corrente motore B          | 0.20 Ω, 1%, ≥1 W; limite corrente circa 1 A                        | 2512              | **HoYLR2512-3W-200mR-1% / C5375488** |
| R_FAULT |   1 | Pull-up uscita nFAULT            | 10 kΩ, 1%, verso VCC logica                                        | 0603              | **0603WAF1002T5E / C25804**          |
| R_SLEEP |   1 | Pull-up nSLEEP                   | 10 kΩ, 1%, verso VCC logica; abilita driver di default             | 0603              | **0603WAF1002T5E / C25804**          |
| R_AIN1  |   1 | Resistenza serie ingresso logico | 100 Ω, opzionale                                                   | 0603              | **0603WAF1000T5E / C22775**          |
| R_AIN2  |   1 | Resistenza serie ingresso logico | 100 Ω, opzionale                                                   | 0603              | **0603WAF1000T5E / C22775**          |
| R_BIN1  |   1 | Resistenza serie ingresso logico | 100 Ω, opzionale                                                   | 0603              | **0603WAF1000T5E / C22775**          |
| R_BIN2  |   1 | Resistenza serie ingresso logico | 100 Ω, opzionale                                                   | 0603              | **0603WAF1000T5E / C22775**          |
| D_TVS   |   1 | Protezione transitori su VM      | TVS 7 V, opzionale; utile con cavi lunghi o alimentazione rumorosa | SMB               | **SMBJ7.0A / C151864**               |
| J_M1    |   1 | Connettore motore A              | 2 pin per motore N20                                               | JST-XH SMD 2.54   | **HX-2.54-2PWT / C5142098**          |
| J_M2    |   1 | Connettore motore B              | 2 pin per motore N20                                               | JST-XH SMD 2.54   | **HX-2.54-2PWT / C5142098**          |

---

## License

MIT License - see LICENSE file for details.
