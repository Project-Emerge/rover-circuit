# General check after BOM cleanup - 2026-05-28

Project: `rover-circuit`

## What was cleaned

- `R5` now has consistent BOM metadata:
  - `Manufacturer`: `BOURNS`
  - `MPN`: `CHP2512AFX-10R0ELF`
  - `LCSC`: `C1870255`
  - `Datasheet`: LCSC PDF for `C1870255`
- `R9` and `R10` now have consistent BOM metadata:
  - `Manufacturer`: `Milliohm`
  - `MPN`: `HoLRT1206-1W-200mR-1%`
  - `LCSC`: `C5127778`
  - `Datasheet`: LCSC product page for `C5127778` because the live API did not expose a direct PDF URL.

## Regenerated outputs

- BOM export: `analysis/rover_bom_clean_2026-05-28.csv`
- Live LCSC audit: `analysis/lcsc_bom_audit_2026-05-22.csv` and `.md` regenerated from the current schematic, despite the legacy filename.
- Schematic analysis: `analysis/general-check-2026-05-28/2026-05-28_2116/schematic.json`
- PCB analysis: `analysis/general-check-2026-05-28/2026-05-28_2116/pcb.json`
- Schematic/PCB cross-analysis: `analysis/general-check-2026-05-28/2026-05-28_2116/cross_analysis.json`

## Current BOM status

- Active schematic BOM lines: 59
- Active purchasable components: 84
- MPN coverage: 59/59 active BOM lines
- LCSC coverage: 59/59 active BOM lines
- Datasheet coverage: 55/59 active BOM lines
- Live LCSC audit: 57 OK, 2 review, 0 missing, 0 failed
- Estimated LCSC spend for 5 boards: USD 94.69

## Remaining BOM / sourcing issues

| Ref | Status | Finding | Action |
|---|---|---|---|
| `DWM1` | Real sourcing issue | `DWM1000 / C95238` resolves, but live LCSC stock is 0. | Source elsewhere or revise design. `DWM3000TR13 / C5299931` remains the likely LCSC successor, but it requires firmware/design verification. |
| `R5` | Audit-script review only | Live LCSC resolves `C1870255` to `CHP2512AFX-10R0ELF`; stock 100. The audit script marks package review because this LCSC API response does not expose a package string. | Manually checked as a 2512 Bourns CHP part; selection is acceptable for the intended 10 ohm / 3 W / 2512 role. |
| `R2` | Design-intent issue | Still `1.1 k / C22764`. This differs from the README/BQ25887 ILIM target of 383 ohm for about 2.9 A input limit. | If 2.9 A is intended, change to a stocked 383 ohm 0603 part. Better candidate than the earlier out-of-stock Panasonic part: `CRGH0603F383R / C2098426`, 383 ohm, 1%, 200 mW, 0603. |

## General design check

PCB:

- 98 footprints.
- Routing complete.
- 0 unrouted nets.
- Schematic/PCB cross-analysis reports no findings.

Analyzer findings needing interpretation:

- `U3.VINT` no DC path to rail is an expected false positive: DRV8833 `VINT` is an internal regulator output and is only bypassed with `C8`.
- `U8.Vcc` no DC path to named rail is likely a naming/analyzer limitation: it is fed from `U12.VO`, but the net is unnamed.
- DRV8833 logic-domain warnings on `AIN1/AIN2/BIN1/BIN2/~SLEEP` are likely false positives from assigning the whole motor driver to the 6 V motor domain. These pins are logic inputs driven from the 3.3 V MCU domain; confirm against the DRV8833 input limits if making a release decision.
- Pull-up warnings on sensor interrupt/status pins should be reviewed by firmware intent. Some may be intentionally unused or LED-driven; do not treat them as BOM mismatches.

## Bottom line

The BOM metadata cleanup is complete for the recent resistor updates. `R5` and `R9/R10` are now coherent with the selected LCSC parts. The only remaining hard sourcing blocker is `DWM1` stock. The only remaining value/design-intent mismatch from the earlier audit is `R2` if the README's 383 ohm ILIM target is still authoritative.
