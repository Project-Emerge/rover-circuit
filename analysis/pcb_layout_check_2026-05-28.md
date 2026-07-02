# PCB layout check - 2026-05-28

Project: `rover-circuit`

Primary source: KiCad 10.0.1 DRC JSON at `analysis/layout-check-2026-05-28/kicad_drc_2026-05-28.json`.

KiCad DRC was used as the authority for courtyard checks because it evaluates KiCad courtyard geometry directly, not rectangular bounding boxes.

## Summary

- KiCad DRC found 9 violations when exclusions were included.
- 0 unconnected items.
- 4 schematic parity warnings.
- No KiCad courtyard-overlap violations were reported.
- PCB analyzer courtyard-overlap findings are therefore treated as false positives unless confirmed visually or by KiCad DRC.

## Real KiCad DRC errors

| Type | Item | Actual | Required | Notes |
|---|---|---:|---:|---|
| Board edge clearance | `J2` shield PTH pad `SH` near edge arc | 0.3595 mm | 0.5000 mm | USB-C shield pad too close to `Edge.Cuts`. |
| Board edge clearance | `J2` shield PTH pad `SH` near left/right edge segments | 0.3300 mm | 0.5000 mm | Three separate shield-pad/edge checks fail at 0.33 mm. |

Action: move `J2` inward or revise the local board cutout/edge clearance rule if the connector datasheet and fabricator accept the geometry. Because this involves USB connector shield PTH pads, verify against JLCPCB minimum copper-to-edge/slot rules before overriding.

## KiCad DRC warnings

| Type | Item | Actual | Required | Action |
|---|---|---:|---:|---|
| Silkscreen text thickness | `SCL` on `F.Silkscreen` | 0.1400 mm | 0.1500 mm | Increase stroke width to >= 0.15 mm. |
| Silkscreen text height | `SCL` on `F.Silkscreen` | 0.7000 mm | 1.0000 mm | Increase text height or relax rule if fab accepts smaller legend. |
| Silkscreen text thickness | `SDA` on `F.Silkscreen` | 0.1400 mm | 0.1500 mm | Increase stroke width to >= 0.15 mm. |
| Silkscreen text height | `SDA` on `F.Silkscreen` | 0.7000 mm | 1.0000 mm | Increase text height or relax rule if fab accepts smaller legend. |

## Excluded KiCad violation

| Type | Item | Detail | Action |
|---|---|---|---|
| Starved thermal | `U2` pad 20 on `GND`, `F.Cu` zone | Zone min spoke count is 2; actual is 1. This violation is marked excluded in the KiCad report. | Revisit the exclusion. For charger IC `U2`, a stronger ground/thermal connection is usually preferable. |

## Schematic parity warnings

| Item | Warning | Action |
|---|---|---|
| `J2` | No pad found for schematic pin `S1 (GND)`. | Check USB-C connector symbol/footprint pin mapping for shield pins. |
| `R5` | PCB footprint field `Manufacturer` is empty; schematic says `BOURNS`. | Update PCB from schematic. |
| `R9` | PCB footprint field `Manufacturer` is empty; schematic says `Milliohm`. | Update PCB from schematic. |
| `R10` | PCB footprint field `Manufacturer` is empty; schematic says `Milliohm`. | Update PCB from schematic. |

## PCB analyzer warnings worth reviewing

These are not KiCad DRC violations, but they are still useful manufacturing checks:

- Via annular ring is 0.1 mm. Analyzer notes this requires advanced process and is below IPC Class 2 0.125 mm.
- Test point coverage is low: 2/132 nets, about 2%.
- `U2` thermal vias are insufficient by the analyzer rule: 0/5 minimum.
- Untented via-in-pad warnings:
  - `C10:2`
  - `C24:2`
  - `J9:1`
  - `J9:MP`

## Courtyard findings

KiCad DRC reported no courtyard-overlap violations. The earlier analyzer-reported overlaps, including `C6/J9`, `D1/D2`, `L3/J9`, and `R1/R8`, are not accepted as real errors from this check because they come from simplified geometry and do not account for KiCad's actual courtyard shapes.

## Bottom line

Fix `J2` shield-pad edge clearance first. Then clean up the `SDA`/`SCL` silkscreen rule violations and update the PCB from schematic to clear the field-parity warnings. Review, but do not blindly act on, the analyzer-only courtyard overlaps.
