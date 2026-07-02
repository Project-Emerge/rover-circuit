# Component value/package re-check - 2026-05-28

Project: `rover-circuit`

Basis: current KiCad files after the latest updates, regenerated BOM JSON, schematic/PCB analysis, cross-analysis, and live LCSC metadata.

## Summary

- Current BOM: 59 active BOM lines, 84 active purchasable components.
- LCSC coverage: 59/59 active BOM lines still have LCSC codes.
- Current BOM metadata coverage regressed slightly: 57/59 lines have MPNs because `R5`, `R9`, and `R10` now have blank `MPN`/`Manufacturer` fields.
- Live LCSC audit: 56 OK, 3 review, 0 missing, 0 failed.
- PCB routing remains complete; schematic/PCB cross-analysis reports no findings.

## Resolved by the updates

| Ref | Previous issue | New state | Verdict |
|---|---|---|---|
| R5 | Old LCSC `C2934046` was a 10 ohm 2512 resistor rated only 1 W, below the 3 W cell-balancing requirement. | Now points to `C1870255`, live MPN `CHP2512AFX-10R0ELF`, Bourns, stock 100. | Electrical selection looks correct for 10 ohm / 2512 / 3 W requirement. Schematic metadata still needs cleanup. |
| R9, R10 | Old LCSC `C309533` was 0.2 ohm 1206 but did not meet the requested >=1 W margin. | Now point to `C5127778`, live MPN `HoLRT1206-1W-200mR-1%`, stock 10812. | Same-footprint 1206 upgrade looks correct for 0.2 ohm / 1 W / 1%. This still does not change the PCB to the README's 2512 package, but it satisfies the same-footprint improvement path. |

## Still needs attention

| Ref | Current state | Issue | Recommended fix |
|---|---|---|---|
| R5 | Value `10`, footprint `R_2512_6332Metric`, LCSC `C1870255`; `Manufacturer` and `MPN` are blank; datasheet still points to old `C2934046`. | The component choice is likely right, but the schematic BOM fields are inconsistent. This can export the wrong datasheet and leaves traceability incomplete. | Set `Manufacturer=BOURNS`, `MPN=CHP2512AFX-10R0ELF`, `Datasheet=https://datasheet.lcsc.com/datasheet/pdf/15b904ea8ab556bb357f10bd4cab1f31.pdf?productCode=C1870255`. |
| R9, R10 | Value `200m`, footprint `R_1206_3216Metric`, LCSC `C5127778`; `Manufacturer` and `MPN` are blank; datasheet still points to old `C309533`. | The selected LCSC part matches the intended same-footprint upgrade, but schematic metadata is incomplete and the datasheet URL is stale. | Set `MPN=HoLRT1206-1W-200mR-1%`, set manufacturer from LCSC if desired, and update the datasheet URL once confirmed from LCSC. |
| R2 | Still `1.1K`, LCSC `C22764`. | This was not changed. It still differs from the README/BQ25887 ILIM requirement of 383 ohm for about 2.9 A input current. | If the 2.9 A input limit is still intended, change R2 to a 383 ohm 0603 part such as `ERJ-S03F3830V / C2111592`. If 1.1 k is intentional, update the README requirement. |
| DWM1 | Still `DWM1000`, LCSC `C95238`. | Live LCSC stock remains 0. | Replace/source elsewhere. Candidate remains `DWM3000TR13 / C5299931`, but that is a design/firmware change, not a drop-in BOM-only substitution. |

## Checks that passed

- `R5` footprint remains `R_2512_6332Metric`, which matches the 2512 replacement family.
- `R9/R10` footprint remains `R_1206_3216Metric`, and `C5127778` resolves as a 1206 0.2 ohm 1 W current-sense resistor.
- The current PCB has 98 footprints, routing complete, and 0 unrouted nets.
- Schematic/PCB cross-analysis for the re-check reports no findings.
- The rest of the LCSC BOM remains unchanged from the previous OK state.

## Generated files

- `analysis/recheck-2026-05-28/2026-05-28_2110/schematic.json`
- `analysis/recheck-2026-05-28/2026-05-28_2110/pcb.json`
- `analysis/recheck-2026-05-28/2026-05-28_2110/cross_analysis.json`
- `analysis/lcsc_bom_audit_2026-05-22.csv` and `.md` were regenerated from the current schematic, despite the legacy filename.
