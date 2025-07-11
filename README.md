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

## License

MIT License - see LICENSE file for details.
