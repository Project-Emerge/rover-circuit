# Component value/package/design-fit audit - 2026-05-28

Project: `rover-circuit`

Scope: current KiCad schematic/PCB, current BOM fields, local datasheets in `datasheets/`, live LCSC metadata, and the component requirements written in `README.md`.

## Summary

- Current BOM has 59 active LCSC lines and no missing LCSC codes.
- Most LCSC selections match the current KiCad value and footprint.
- The simple LCSC resolution check passes 58/59 lines; `DWM1` is the one live-stock failure.
- Deeper value/package/design checks found 4 items that need attention and 4 documentation/intent differences to confirm.

## Needs attention

| Ref | Current selection | What differs | Why it matters | Suggested LCSC action |
|---|---|---|---|---|
| R5 | `FRC2512F10R0TS`, LCSC `C2934046`, 10 ohm, 2512 | Datasheet rates this FOJAN 2512 resistor at 1 W. README/BQ balancing requirement calls for 10 ohm, 3 W, 1%; expected dissipation is about 1.46 W during balancing. | Current part is under the stated power requirement and can overheat during cell balancing. | Use a 3 W 2512 10 ohm part. Preferred exact README part `TRL251230F10R0E04Z / C2992634` is currently out of stock. Available alternatives found: `CHP2512AFX-10R0ELF / C1870255`, 10 ohm, 1%, 3 W, 2512, stock 10; or `352210RJT / C2076046`, 10 ohm, 5%, 3 W, 2512, stock 637 if 5% is acceptable. |
| R2 | `0603WAF1101T5E`, LCSC `C22764`, 1.1 k, 0603 | README/BQ table calls for 383 ohm on ILIM for about 2.9 A input limit. Current 1.1 k changes the hardware input-current limit to roughly one third of that. | This changes charger behavior, not just sourcing. If the design expects ~2.9 A input, the current part is wrong. | If the 2.9 A limit is desired, replace with a 383 ohm 0603, e.g. Panasonic `ERJ-S03F3830V / C2111592`. If the lower current limit is intentional, update the README requirement. |
| R9, R10 | `PT1206FR-7W0R2L`, LCSC `C309533`, 0.2 ohm, 1206, 0.5 W class | README motor-driver table calls for 0.20 ohm, >=1 W, 2512. Current PCB footprint is 1206, not 2512. | Electrically, 0.2 ohm sets DRV8833 chopping around 1 A and 0.2 W at 1 A RMS, so it can work. It does not meet the documented >=1 W / 2512 margin. | For a same-footprint improvement, use a 1206 1 W current-sense part such as `HoLRT1206-1W-200mR-1% / C5127778` or `HoYH1206-1W-200mR-1% / C2932839`. For the README package, change the PCB to 2512 and use the originally intended 2512 class part. |
| DWM1 | DecaWave `DWM1000`, LCSC `C95238`, footprint `RF_Module:DWM1000` | LCSC resolves the part but live stock is 0. | The component is not orderable from LCSC for the current build. | For new builds consider Qorvo `DWM3000TR13 / C5299931`, but treat it as a design/firmware change, not a blind BOM substitution. |

## Documentation / intent mismatches to confirm

These are not necessarily wrong in the current schematic, but they differ from the README component table.

| Area | README requirement | Current schematic/LCSC | Assessment |
|---|---|---|---|
| BQ25887 PMID capacitance | Two 22 uF, 25 V, 1206 capacitors on PMID | One 10 uF 1206 on PMID: `CL31A106KBHNNNE / C13585` | BQ25887 datasheet typical test condition uses `CPMID = 10 uF`, so current schematic may be OK. README is stale if 10 uF is intentional. |
| BQ25887 BAT capacitance | One 22 uF, 25 V, 1206 capacitor on BAT | Four 10 uF 0805 capacitors on `+BATT`: `GRM21BR61E106KA73L / C84416` | More nominal capacitance than README, smaller package. Likely OK if DC-bias derating still leaves enough effective capacitance. |
| BQ25887 REGN capacitor package | 4.7 uF, 10 V, 0402 | 4.7 uF, 0603: `CL10A475KA8NQNC / C69335` | Electrically OK; package differs but current KiCad/LCSC match each other. |
| Motor connectors J7/J8 | JST-XH SMD 2.54 mm, `HX-2.54-2PWT / C5142098` | JST-PH horizontal 2.00 mm, `S2B-PH-SM4-TB(LF)(SN) / C295747` | Current LCSC part matches current PCB footprint. If the mechanical harness expects JST-XH 2.54 mm, the PCB footprint and BOM are wrong. |

## Checked OK

- BQ25887 IC: `BQ25887RGER / C2761614` matches QFN-24-EP 4x4 footprint.
- BQ25887 SNS capacitors: `C3,C12`, 22 uF 1206 25 V class, total 44 uF nominal, match datasheet requirement.
- BQ25887 VBUS capacitors: `C16,C2`, 1 uF 0603, match required at least 1 uF at VBUS.
- BQ25887 BTST capacitor: `C4`, 47 nF 0603, matches datasheet requirement.
- BQ25887 MID resistor: `R4`, 300 ohm, matches value; package is larger than README.
- BQ25887 TS divider: `R6=5.23 k`, `R7=30.1 k`, values match the README/datasheet target network.
- DRV8833 IC: `DRV8833PWPR / C50506` matches HTSSOP-16-EP footprint.
- DRV8833 support caps: VM 10 uF + 100 uF bulk, VCP 10 nF, VINT 2.2 uF all match the datasheet functional requirements.
- AP63200/AP63205 buck parts: package and key external values are coherent. `U5` feedback `64.9 k / 10 k` gives about 5.99 V; `U7` is fixed 5 V. Inductors are in the datasheet's 2.2 uH to 10 uH recommended range.
- TPS62162 3.3 V regulator: `TPS62162DSGR / C40256`, WSON-8-EP package, `L2=2.2 uH`, and output capacitors are coherent for the rail.
- Sensor/module packages: `MMC5983MA / C404329` and `BMI270 / C2836813` match the current LGA footprints.

## Verification basis

- Current KiCad BOM export from `bom_manager.py`.
- Current schematic/PCB analyzer outputs under `analysis/current-lcsc-check/2026-05-28_2049/`.
- Local datasheets: `BQ25887.pdf`, `DRV8833.pdf`, `AP63200_AP63205.pdf`, resistor/capacitor datasheets in `datasheets/`.
- Live/web LCSC metadata for the replacement candidates named above.
