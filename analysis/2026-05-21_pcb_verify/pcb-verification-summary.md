# PCB Verification Summary

**Date:** 2026-05-21  
**Board:** `rover-circuit.kicad_pcb`  
**Output folder:** `analysis/2026-05-21_pcb_verify/`

## Result

The current PCB passes KiCad DRC: 0 violations, 0 unconnected pads, 0 footprint errors.

The current schematic also passes KiCad ERC: 0 violations. Schematic/PCB cross-analysis reports no blocker-level synchronization problems.

## Current PCB Metrics

- Footprints: 96
- SMD components: 87
- Track segments: 673
- Vias: 159
- Copper layers: 2
- Board outline: 78.0 mm x 75.271 mm
- Routing complete: yes, 0 unrouted nets

## Changes Since Previous Review

- Added 3 front-side fiducials: `FID4`, `FID5`, `FID6`.
- Added 3 rail test points: `TP1` (+3V3), `TP2` (+5V), `TP3` (+6V).
- Added `REF**` OSHW silkscreen logo footprint.
- The previous front-side fiducial error is resolved.

## Remaining Analyzer Findings

### Errors

- `PM-001`: courtyard overlap between `D1` and `D2`.
- `PM-001`: courtyard overlap between `R1` and `R8`.
- `PM-002`: edge clearance for `J2`, `J7`, `J8`, `J9`.

These are not KiCad DRC violations, but they remain assembly/mechanical review items.

### Warnings

- `DFM-001` / `DFM-002`: 0.1 mm annular ring requires advanced process and is below IPC Class 2 default 0.125 mm.
- `PM-001`: courtyard overlaps involving `C19/L3`, `C2/L1`, `C22/L3`, `D1/R1`, `D2/R8`, `R11/U12`.
- `PM-002`: `J3` is 0.72 mm from board edge.
- `TE-001`: analyzer still reports 0/132 signal-net test point coverage, although power rail test points `TP1`-`TP3` are present.
- `TV-001`: U2 thermal pad still has 0 direct thermal vias.
- `VP-001`: untented via-in-pad at `C10:2`, `C24:2`, and `R5:2`.

## Cross-Analysis Notes

- Extra PCB-only footprint `REF**` is the OSHW logo and is acceptable if intentional.
- `+3V3` plane now reports 3 islands; `VBUS` reports 2 islands. These are informational but worth checking if the islands are meant to carry current or provide return path.

