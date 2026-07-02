# LCSC component fit report - 2026-05-28

Project: `rover-circuit`

## Summary

- Current schematic BOM: 59 active BOM lines, 84 active purchasable components.
- LCSC coverage: 59/59 active BOM lines have LCSC codes.
- Live LCSC audit result: 58 OK, 1 needs attention, 0 missing, 0 failed.
- Estimated LCSC spend for 5 boards from resolvable current selections: USD 94.46.
- Schematic/PCB fit check: no missing MPNs, no missing footprints, PCB routing complete.

Generated audit files:

- `analysis/lcsc_bom_audit_2026-05-22.md` (regenerated from current schematic despite legacy filename)
- `analysis/lcsc_bom_audit_2026-05-22.csv` (regenerated from current schematic despite legacy filename)
- `analysis/current-lcsc-check/2026-05-28_2049/{schematic.json,pcb.json,cross_analysis.json}`

## Needs attention

| Ref | Current part | Current LCSC | Issue | Recommendation |
|---|---|---:|---|---|
| DWM1 | DecaWave DWM1000 | C95238 | Live LCSC stock is 0. LCSC also marks it not available now / not recommended for new designs. | Replace for new builds. Best LCSC candidate is Qorvo DWM3000TR13 / C5299931, but firmware must be checked because it is a newer DW3000-family module. |

## Suggested replacement for DWM1

Recommended LCSC candidate: Qorvo `DWM3000TR13`, LCSC `C5299931`.

Why:

- It is the closest LCSC-listed successor in the same DWM module family.
- LCSC brand listing shows `DWM3000TR13 / C5299931` with 6 in stock.
- Qorvo documents `DWM3000` as pin and size compatible with `DWM1000`, and channel 5 operation as compatible with `DWM1000`.

Caveats:

- This should be treated as a design change, not a pure BOM-only swap, until firmware is verified with a DW3000 driver/register map.
- LCSC stock is only 6 units, which covers the 5-board audit quantity but is thin.
- If you need a larger build, source confirmation is needed before ordering.

Alternatives considered:

- Keep `DWM1000 / C95238`: not recommended because live LCSC stock is 0.
- `DWM3001CTR13 / C6796910`: not a drop-in for the current `RF_Module:DWM1000` footprint and LCSC/JLCPCB stock is 0 in the searched listing.
- `DW1000-I-TR13 / C5241969`: available as the IC, but it requires RF/antenna/layout redesign, so it is not a module replacement for this PCB.
- `UWB3000F00 / C19632388`: in stock, but not footprint-compatible with the current DWM1000 module footprint.

## Low-stock but currently usable

These passed package/MPN/value checks, but stock is thin relative to even small production:

| Ref | Part | LCSC | Live stock | Required for 5 boards | Note |
|---|---|---:|---:|---:|---|
| J4 | JST S4B-PH-SM4-TB(LF)(SN) | C265102 | 7 | 5 | Fits current footprint, but little margin. |
| R5 | FOJAN FRC2512F10R0TS | C2934046 | 10 | 5 | Fits current 2512 resistor footprint, but little margin. |
| U8 | ST STM6601CM2DDM6F | C155599 | 38 | 5 | Fits current TDFN-12 footprint; okay for prototype quantity. |
| U12 | Microchip MCP1799T-5002H/TT | C2890492 | 21 | 5 | Fits current SOT-23 footprint; okay for prototype quantity. |

## Sources checked

- Live LCSC/jlcsearch metadata via `analysis/lcsc_bom_audit.py`.
- Local KiCad schematic and PCB analyzers.
- LCSC product pages/search snippets for `C95238`, `C5299931`, `C6796910`, `C5241969`, and `C19632388`.
- Qorvo DWM3000 product data for DWM1000 compatibility.
