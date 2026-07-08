# Requirements

---

### General Requirements

### Mechanical Requirements

### Electrical Requirements

### Functional Requirements


### 2. General Board Overview

* **Application**: Robot rover controller with battery charging and motor driving capabilities.
* **Target Enclosure**: Custom 3D-printed case with mounting points for motors, battery, and sensors.
* **Operating Temperature Range**: -20 °C to +60 °C.

---

### 3. Mechanical Requirements

* **Board Dimensions**: ?? mm × ?? mm (to fit within the enclosure).
* **Mounting Holes**: 4 holes for M2 screws, located at the two sides of the board.
* **Thickness**: Standard 1.6 mm PCB thickness.
* **Keep-out Zones**: 5 mm from the edges for mounting clearance; No components in the center bottom side (battery slot). No components closer than 3 mm to the mounting holes.

---

### 4. Electrical Requirements

#### 4.1 Power Domains
* **Input Voltage**: Two-cell Li-ion battery (7.4 V nominal) with USB-C charging support.
* **Internal Voltage Rails**: 3.3 V for logic and sensors, 6 V for motors, and regulated 5 V for external Raspberry Pi connection.
* **Current Requirements**: Up to 2 A for motors, 1 A for sensors and logic.

#### 4.2 Interfaces
* **I2C**: For communication with sensors and battery management.
* **GPIO**: For motor control signals and status LEDs.
* **USB-C**: For charging and potential data communication with a host computer.
* **Motor Outputs**: Two H-bridge outputs for controlling two DC motors.
