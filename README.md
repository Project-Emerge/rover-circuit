# Rover Circuit

A KiCad PCB project for a rover circuit board.

## Project Structure

- `rover-circuit.kicad_sch` - Main schematic file
- `rover-circuit.kicad_pcb` - PCB layout file
- `front_wheels.kicad_sch` - Front wheels schematic
- `rear_wheels.kicad_sch` - Rear wheels schematic
- `rover-circuit.step` - 3D model of the circuit board
- `production/` - Production files (BOM, pick & place, etc.)

## Development Workflow

This project uses automated CI/CD with semantic versioning based on conventional commits.

### Conventional Commits

Please follow the [Conventional Commits](https://www.conventionalcommits.org/) specification for your commit messages:

- `feat:` - New features (triggers minor version bump)
- `fix:` - Bug fixes (triggers patch version bump)  
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring without changing functionality
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks, dependency updates
- `BREAKING CHANGE:` - Breaking changes (triggers major version bump)

#### Examples

```text
feat: add power management circuit to main schematic
fix: correct trace width on high current paths
docs: update component specifications in README
chore: update footprint libraries
```

### CI/CD Pipeline

The GitHub Actions workflow automatically:

1. **On every push/PR:**
   - Validates KiCad schematic and PCB files
   - Generates schematic PDFs
   - Exports 3D models (STEP files)
   - Creates Gerber files for manufacturing

2. **On main branch:**
   - Runs semantic-release to determine version
   - Creates GitHub releases with generated artifacts
   - Includes schematic PDFs and 3D models as release assets

### Release Artifacts

Each release automatically includes:

- **Schematic PDFs** - Visual documentation of the circuit
- **3D Models (STEP)** - For mechanical integration
- **Gerber Files** - For PCB manufacturing

## Getting Started

1. Clone this repository
2. Open the project in KiCad 8.0+
3. Make your changes following conventional commit format
4. Push to trigger the CI/CD pipeline

## Requirements

- KiCad 8.0 or later
- Git with conventional commit messages

# Components BOM


### BQ25887 -- Charger 2S boost + Cell Balancing

| Rif.     | Qtà | Funzione                             | Specifica / valore da montare                                       | Package          | Codice JLCPCB/LCSC                     |
| -------- | --: | ------------------------------------ | ------------------------------------------------------------------- | ---------------- | -------------------------------------- |
| U1       |   1 | Charger 2S boost + bilanciamento     | TI **BQ25887RGER**, QFN-24-EP 4×4                                   | QFN-24-EP(4×4)   | **C2761614** ([LCSC Electronics][1])   |
| L1       |   1 | Induttore boost | **1 µH**, molded/shielded, **Irms 12 A**, **Isat 15 A**, **DCR 7.4 mΩ**, ±20% | **SMD 7×6.6 mm** | **C167216**        |
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


---

## License

MIT License - see LICENSE file for details.
