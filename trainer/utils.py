#/bin/usr/python
from math import pow


def print_banner():
    print()
    print("┌─────────────────────────────────────────────┐")
    print("│     _______    ____     __            __    │")
    print("│    /  _/ _ \\  / __/_ __/ /  ___  ___ / /_   │")
    print("│   _/ // ___/ _\\ \\/ // / _ \\/ _ \\/ -_) __/   │")
    print("│  /___/_/    /___/\\_,_/_.__/_//_/\\__/\\__/    │")
    print("│  /_  __/______ _(_)__  ___ ____             │")
    print("│   / / / __/ _ `/ / _ \\/ -_) __/             │")
    print("│  /_/ /_/  \\_,_/_/_//_/\\__/_/                │")
    print("│                                 ttran.tech  │")
    print("└─────────────────────────────────────────────┘")
    print()


def binary_to_decimal(binary: str) -> int:
    """Convert binary to decimal number"""
    n = 0; decimal = 0
    for digit in "".join(reversed(binary)):
        decimal += (pow(2, n) * int(digit))
        n += 1
    return int(decimal)
