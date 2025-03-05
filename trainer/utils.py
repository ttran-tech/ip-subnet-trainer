#/bin/usr/python
from math import pow


def binary_to_decimal(binary: str) -> int:
    """Convert binary to decimal number"""
    n = 0; decimal = 0
    for digit in "".join(reversed(binary)):
        decimal += (pow(2, n) * int(digit))
        n += 1
    return int(decimal)

if __name__ == "__main__":
    binary = "11000000"
    decimal = binary_to_decimal(binary=binary)

    print(f"{binary} = {decimal}")