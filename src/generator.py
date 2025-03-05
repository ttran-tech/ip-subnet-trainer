# This file contains the functions for generating the IP Address and CIRD suffix
import random


def _generate_first_octet(start:int, end:int, exclude:int) -> int:
    """Generate the first octet of the IP address, but excludes 127 (loopback) """
    octet = random.randint(start, end)
    if octet == exclude:
        return (_generate_first_octet(start, end, exclude))
    return octet


def generate_ip() -> str:
    """
    Generate a random IP address from the following classes:
        Class A (1-126)
        Class B (128-191)
        Class C (192-223)
    """
    return f"{ _generate_first_octet(1, 223, 127) }.{ random.randint(1, 255) }.{ random.randint(1, 255) }.{ random.randint(1, 255) }"


def generate_cidr() -> str:
    """Generate a random CIDR between 8 and 30"""
    return f"{random.randint(1, 30)}"