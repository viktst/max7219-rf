import max7219
from machine import Pin, SPI
import time

spi = SPI(0, baudrate=10_000_000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
display_matrix = max7219.Matrix8x8(spi, Pin(5, Pin.OUT), 4)  # 4 chained matrices
display_matrix.brightness(5)

def read_file(filename: str) -> list:
    try:
        with open(filename, "r") as file:
            lines = [line.strip() for line in file if line.strip()]
            total_lines = len(lines)
            total_chars = sum(len(line) for line in lines)
        return lines, total_lines, total_chars
    except OSError as e:
        print(f"error reading file {filename}: {e}")
        return ["file not found"], 0, 0

def output(text: str, delay: float = 0.1):
    text = f" {text} "
    text_len = len(text) * 8

    for x in range(32, -text_len - 16, -1):
        display_matrix.fill(0)
        display_matrix.text(text, x + 18, 0, 1)
        display_matrix.show()
        time.sleep(delay)

def main():
    display_matrix.fill(0)
    display_matrix.show()

    filename = "file.txt"
    lines, total_lines, total_chars = read_file(filename)

    print(f"file: {filename}")
    print(f"lines: {total_lines}")
    print(f"chars: {total_chars}")

    while True:
        for line in lines:
            output(line, delay=0.15)
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("program interrupted by user!")
