# This file contains the functions to generate challenges and answers
from generator import *
from calculator import *

def generate_challenge() -> str:
    "Generate a challenge question. Return <ip address>/<cird suffix>"
    return f"{generate_ip()}/{generate_cidr()}"

def generate_answer(challenge:str) -> dict:
    ip, cidr = challenge.split('/')
    subnet = calculate_subnet_mask(cird=cidr)
    block_size = 0

    for i in subnet:
        if i != 255:
            block_size = 256 - i
            break

    return {
        'ip': ip,
        'cidr': cidr,
        'subnetMask': subnet,
        'blockSize': block_size,
    }


if __name__ == '__main__':
    challenge = generate_challenge()
    answer = generate_answer(challenge=challenge)
    print(answer)