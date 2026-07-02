# Rover Circuit Design Review

**Project:** `rover-circuit.kicad_pro`  
**Date:** 2026-05-20  
**KiCad:** 10.0.1  
**Design:** 10-sheet hierarchical schematic, 2-layer PCB, 78.0 mm x 75.271 mm current board outline  
**Analyzers run:** KiCad ERC, KiCad DRC, schematic analyzer, full PCB analyzer, cross-analysis, EMC analyzer with ngspice, thermal analyzer, SPICE simulation, stale production gerber analyzer

## Verdict

The current schematic and PCB are internally consistent: ERC reports 0 errors/0 warnings, DRC reports 0 violations and 0 unconnected pads, and the schematic/PCB both contain 89 placed design items. Electrically, I did not find a confirmed pinout or connectivity blocker in the local source files.

The design is not ready for a clean fabrication/assembly release yet. The production gerber zip is stale and does not match the current board outline, there are no board fiducials despite fine-pitch SMD parts, U2's thermal pad has no direct thermal vias, and several layout/DFM issues should be resolved or explicitly accepted before ordering.

## Critical Findings

| Severity | Finding | Evidence | Action |
|---|---|---|---|
| Critical | `production/rover-circuit.zip` is stale: gerbers are 105.0 mm x 70.0 mm, current PCB is 78.0 mm x 75.271 mm | Gerber analyzer vs `pcb.json` | Regenerate fabrication outputs from the current PCB before fab |
| High | No fiducials on `F.Cu` with 80 front-side SMD components and 0.25 mm finest pads | `pcb.json` `FD-001` | Add 3 global fiducials for assembled top side |
| High | U2 BQ25887 thermal pad has 0 direct thermal vias; datasheet layout section says the exposed pad must be grounded with sufficient thermal vias | `pcb.json` `TV-001`; BQ25887 datasheet section 11.1 | Add thermal vias in/near U2 exposed pad if charging current or thermal rise matters |
| Warning | Switching-regulator EMC/layout risk around U5/U7/U9 | EMC `SW-001`/`SW-003`; AP63200/AP63205 and TPS62160 layout sections | Tighten hot loops, input caps, inductor/SW routing, and local GND returns |
| Warning | Untented via-in-pad on C10:2, C24:2, and R5:2 | `pcb.json` `VP-001` | Move vias off pads, tent them, or specify filled/capped vias |
| Warning | Courtyard overlaps in LED/status cluster and regulator areas | `pcb.json` `PM-001` | Resolve overlaps or document assembly-house acceptance |

## Schematic Review

Power tree detected:

```text
VBUS -> U2 BQ25887 charger -> +BATT
+BATT -> U5 AP63200 adjustable buck -> +6V, SPICE Vfb = 0.8011 V
+BATT -> U7 AP63205 fixed buck -> +5V
+BATT -> U9 TPS62162 fixed buck -> +3V3
+BATT -> U12 MCP1799 fixed LDO -> power-control bias rail
```

The schematic analyzer reported 84 findings: 6 errors, 11 warnings, 67 info. After datasheet/raw-file review, the 6 schematic errors are not accepted as blockers:

- DRV8833 `AIN1/AIN2/BIN1/BIN2/~SLEEP` level-shifter errors are false positives. These are DRV8833 logic inputs driven by the ESP32, not 6 V outputs. The DRV8833 datasheet logic thresholds are compatible with 3.3 V drive (`VIH` 2.0 V for logic pins, 2.5 V for `nSLEEP`). Raw PCB pads match the intended nets at `rover-circuit.kicad_pcb:11829`, `rover-circuit.kicad_pcb:11909`, and `rover-circuit.kicad_pcb:11980`.
- DRV8833 `VINT` "no DC path" is a false positive. The datasheet says to bypass `VINT` to ground with 2.2 uF; the schematic has C8 = 2.2 uF on `VINT`.
- DRV8833 `AISEN/BISEN` missing pullups are false positives; these are current-sense pins, not pullup pins.
- BQ25887 `STAT` and `~PG`, and TPS62162 `PG`, are not pure missing-pullup cases. They drive LED/resistor paths rather than floating logic inputs.
- U1/MMC5983MA and U11/BMI270 interrupt warnings are low risk if the interrupt pins are intentionally unused. BMI270 supports configurable push-pull/open-drain interrupt outputs, and unused interrupt pins may be left disconnected.

Real schematic metadata gaps remain:

- J3 has no footprint assigned in the schematic, although the PCB currently has `Connector_PinSocket_2.54mm:PinSocket_1x04_P2.54mm_Vertical`.
- 10 BOM parts lack MPNs: `J3`, `U1`, `U11`, `J7`, `J8`, `J9`, `DWM1`, `U12`, `U8`, `C32`.
- Datasheets are present locally for the major ICs/modules, but there is no structured `datasheets/extracted/` cache, so the review uses manual PDF checks plus analyzer output rather than full extraction-backed verification.

## PCB Layout Review

PCB analyzer summary:

- 89 footprints, 81 SMD, 2 THT, 159 vias, 671 track segments.
- Routing complete: 0 unrouted nets.
- 2 copper layers, 1.6 mm board, 35 um copper.
- DFM tier: advanced, driven by 0.1 mm annular ring.

Placement and assembly:

- No fiducials are present. This is the strongest assembly-readiness issue because the board has fine-pitch parts such as U2 and U9.
- The edge-clearance findings for J2/J7/J8/J9 are partly intentional because these are external connectors. Still, the clearances are very small (`J7` 0.14 mm, `J8` 0.12 mm, `J9` 0.14 mm, `J2` 0.32 mm), so panelization and connector overhang should be checked with the fab/assembly house.
- Courtyard overlaps are real geometry issues, especially the D1/D2/R1/R8 status LED cluster. Some buck-regulator overlaps may be intentional compact placement, but assembly acceptance should be confirmed.
- Test point coverage is 0/132 signal nets. For prototypes this may be acceptable; for repeatable bring-up or production it is a testability gap.

Power and thermal layout:

- U2 BQ25887 pad 25 is GND exposed pad on the PCB, but there are no direct thermal vias in the pad. The BQ25887 datasheet specifically calls for sufficient thermal vias under the IC. This is more important if the charger will operate near the intended 2 A capability.
- U3 DRV8833 thermal pad has through-hole thermal pads/vias and is much better supported thermally than U2.
- The thermal analyzer estimated only 0.011 W and a 27.6 C hottest component because it lacks load-current knowledge. Treat that as "no static geometry hotspot found," not proof that charger/motor thermal performance is adequate.

DFM:

- Current via annular ring is 0.1 mm. The project rule file permits 0.075 mm annular ring, but the DFM analyzer marks 0.1 mm below IPC Class 2's 0.125 mm default. This is not a KiCad DRC violation, but it should be aligned with the chosen fab process.
- Vias in SMD pads C10, C24, and R5 are untented. These can wick solder unless the fab process tents/fills/caps them.

## EMC / Signal Integrity

EMC analyzer summary: 54 findings, 1 error, 22 warnings, 31 info, EMC risk score 52/100.

The `SU-001` error is best interpreted as a 2-layer-board limitation rather than a schematic blocker: `F.Cu` and `B.Cu` are both signal/copper layers with no internal reference plane. For a compact robot board this can be acceptable, but it raises layout discipline requirements.

EMC items worth acting on:

- GND pour fill is only 50% on `F.Cu` and 56% on `B.Cu`, with 3 filled GND regions on each layer.
- `/MCU/IO18` and `/MCU/IO19` have partial reference-plane coverage and missing nearby stitching at transitions.
- U5, U7, and U9 switching regulators were flagged for harmonics and large hot-loop geometry. This matches the datasheet guidance for AP63200/AP63205 and TPS62160: keep input caps, SW nodes, inductors, output caps, and PGND loops short and wide.
- Motor connectors J7/J8 and battery connector J9 have no EMC filtering/ESD protection nearby. This may be acceptable for short internal harnesses, but it is a radiated-emissions and ESD exposure risk for external or long cables.

SPICE simulation passed all functional checks: 15 subcircuits simulated, 13 pass, 2 warnings, 0 failures. The warnings are LC filter convergence warnings for L1/C4 and L1/C5; their simulated resonance matched the expected frequency, so they are not functional failures.

## Fabrication Outputs

`production/rover-circuit.zip` was analyzed successfully and contains complete, aligned gerbers and drill files, but it does not match the current PCB:

- Production zip board dimensions: 105.0 mm x 70.0 mm.
- Current PCB dimensions: 78.0 mm x 75.271 mm.
- Production zip timestamp: 2025-07-15.
- Current design files timestamp in workspace: 2026-05-20.

Do not order from the existing production zip for the current design. Regenerate gerbers, drills, BOM, and CPL from the current KiCad project after resolving or accepting the layout findings above.

## Review Limits

- Lifecycle/obsolescence audit was not run because no distributor API credentials were present in the environment and network access is restricted.
- Datasheet verification was manual for critical parts, not extraction-cache backed.
- Thermal analysis lacks real current/load assumptions for the charger, motor driver, and regulators.
- I did not modify schematic or PCB files; this review only generated analysis artifacts and this report.

