# This files contains the functions that calculate and generate the answer
# based on the IP and CIDR from the generator.
from src.utils import binary_to_decimal

def calculate_subnet_mask(cird:str) -> list:
    """Calculate subnet mask from a given CIDR"""
    binary_subnet = {1:'00000000', 2:'00000000', 3:'00000000', 4:'00000000'}
    octet = 1   # first octet
    full_octet = int(int(cird) / 8)
    extra_bit = int(int(cird) % 8)

    for i in range(full_octet):
        binary_subnet[octet] = '11111111'
        octet += 1

    if extra_bit > 0:
        for i in range(extra_bit):
            binary_subnet[octet] = binary_subnet[octet][:i] + '1' + binary_subnet[octet][i+1:]

    return [
        binary_to_decimal(value)
        for value in binary_subnet.values()
    ]


# if __name__ == "__main__":
#     subnet = calculate_subnet_mask(8)
#     subnet = calculate_subnet_mask(12)
#     subnet = calculate_subnet_mask(20)
#     subnet = calculate_subnet_mask(28)
#     subnet = calculate_subnet_mask(30)