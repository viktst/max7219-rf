# MAX7219 module, read from file

This script reads lines from a .txt file and scrolls them across up to four 8x8 LED matrices using the MAX7219 chip with MicroPython.

## Hardware

- Microcontroller (e.g., RP Pico)
- 4 × 8x8 MAX7219 matrix modules (chained)
- Power supply (3.3V or 5V as needed)

### Wiring

| Function | Pin on Pico |
|----------|-------------|
| SCK      | GPIO2       |
| MOSI     | GPIO3       |
| CS       | GPIO5       |

## Software

- MicroPython firmware
- `max7219` driver module
- `main.py` script
- `file.txt` with messages (one per line)

## Functions

- `read_file(filename)`: Reads and returns non-empty lines and some stats.
- `output(text, delay)`: Scrolls text across the matrix.
- `main()`: Starts the program.

## Settings

- **Brightness**: Set to 5 (range 0–15).
- **Scroll Speed**: Change the `delay` value in `output()` to adjust speed.
- **Matrix Count**: Adjust the `4` in `Matrix8x8(..., 4)` to match your setup.