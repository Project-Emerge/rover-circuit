# Datasheet validation - 2026-05-22

Target: 5-board LCSC/JLCPCB-oriented build.

## Result

No existing populated LCSC component was replaced for cost. The safe cost reduction was to reuse already-selected equivalent parts where the schematic had gaps:

- `C32`: reused the existing 1 uF 0603 MLCC selection `CL10A105KA8NNNC` / `C5673`.
- `U1`: added exact MEMSIC `MMC5983MA` / `C404329`.
- `U11`: added exact Bosch Sensortec `BMI270` / `C2836813`.

The remaining unresolved lines need manual product decisions before they should be written into the schematic: `DWM1`, `J3`, `J7`, `J8`, and `J9`.

## Critical Parts

- `U2` `BQ25887RGER` / `C2761614`: datasheet supports 2-cell Li-ion/Li-polymer charging, 3.9 V to 6.2 V VBUS operation, 20 V absolute max on VBUS, 2 A-class boost charger operation, 1.5 MHz switching, REGN bypass, 1 uF VBUS minimum, 10 uF PMID/BAT-class capacitance, and thermal pad grounding. This matches the USB-input 2S charger role.
- `U3` `DRV8833PWPR` / `C50506`: datasheet supports VM operation over the low-voltage motor range, PWP thermally enhanced package, 1.5 A RMS and 2 A peak per H-bridge at VM = 5 V, and requires close VM decoupling plus thermal-pad copper. This matches the dual motor-driver role; actual motor current remains the board-level thermal constraint.
- `U5` `AP63200WU-7` / `C2071868` and `U7` `AP63205WU-7` / `C2071056`: datasheet supports 3.8 V to 32 V input, 2 A output, TSOT-23-6 package, AP63200 adjustable output, AP63205 fixed 5 V output, and recommends inductor current rating margin. These match the buck-regulator roles.
- `U9` `TPS62162DSGR` / `C40256`: datasheet supports 3 V to 17 V input, fixed 3.3 V output, 1 A output, WSON-8 exposed-pad package, and recommends thermal-pad grounding. This matches the 3.3 V rail role.
- `U4` `TPD2EUSB30ADRTR` / `C94934`: datasheet supports the DRT package, low line capacitance, 5 Gbps USB use, IEC ESD protection, and 0 V to 5.5 V IO working range for the non-A variant. This is suitable for the USB data-line ESD role.
- `U6` `ESP32-C6-WROOM-1-N8` / `C5366877`: datasheet supports 3.0 V to 3.6 V module supply and -40 C to 85 C ambient operation. This matches the +3V3-powered wireless module role.
- `U1` `MMC5983MA` / `C404329`: local datasheet supports LGA-16, 2.8 V to 3.6 V supply, 3.0 V nominal operation, I2C fast mode, and SPI operation. This matches the +3V3 IMU/magnetometer interface role.
- `U11` `BMI270` / `C2836813`: local datasheet supports 14-pin 2.5 mm x 3.0 mm LGA, VDD 1.71 V to 3.6 V, VDDIO 1.2 V to 3.6 V, I2C/SPI interfaces, and 100 nF decoupling at VDD/VDDIO. This matches the +3V3 IMU role.
- `U8` `STM6601CM2DDM6F` / `C155599`: ST ordering data maps STM6601 option `C` to active-high `EN`, long-push deasserts `EN`, and pull-up on `SR`; LCSC resolves this MPN as TDFN-12(2x3), matching the schematic footprint.
- `U12` `MCP1799T-5002H/TT` / `C2890492`: Microchip ordering data identifies this as tape-and-reel, 5.0 V output, 3-lead SOT-23 (`TT`) MCP1799; LCSC resolves it as SOT-23, matching the schematic footprint.

## Passive And Power Components

- Existing resistor, capacitor, LED, switch, connector, and inductor LCSC codes resolve to their schematic MPNs with matching package metadata and positive stock in the live audit.
- No cheaper passive substitution was written because conservative replacement would require proving equal or better voltage derating, dielectric/tolerance, ESR/DCR, current rating, and package land-pattern compatibility. The current exact-MPN choices already resolve and are low-cost relative to the IC/module spend.
- `L1` is the charger 1 uH inductor; BQ25887 datasheet examples use 1 uH-class inductance for the application. `L3`/`L4` and buck converter inductors remain acceptable only if their saturation current and DCR margins are preserved; no lower-cost alternate was applied.

## Manual Review Items

- `DWM1`: no live LCSC result found for `DWM1000`; likely consigned/manual sourcing.
- `J3`: no footprint, so no safe connector can be selected.
- `J7`/`J8`: live candidate `S2B-PH-SM4-TB(LF)(SN)` / `C295747`, but connector orientation/package must be visually confirmed against the KiCad footprint before writing.
- `J9`: live candidate `S4B-PH-SM4-K-TB(LF)(SN)` / `C265332`; this is not the same exact MPN as the existing `J4` connector, so it needs mechanical review.
