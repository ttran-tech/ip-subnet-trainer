# IP Subnet Trainer

IP Subnet Trainer is an interactive Python tool designed to help users master subnetting calculations through hands-on practice. The tool randomly generates IP address with CIDR notation (e.g., 192.168.0.0/16) and challenges the users to identify or calculate:

:heavy_check_mark: Subnet Mask

:heavy_check_mark: Block Size

:heavy_check_mark: Network & Broadcast Addresses

:heavy_check_mark: Usage IP Range

## :bulb: Features
:small_blue_diamond: Randomized subnet challenges for real-world learning

:small_blue_diamond: Supports CIRD from **/8** to **/30** for flexible training

## :white_check_mark: TO DO

- Question/Challenge/Quiz:
    - [x] Randomized generate an IP address from either class A, B, or C.
    - [x] Randomize generate CIDR suffix
    - [ ] Generating the answer:
        - [x] Calculate Subnet Mask
        - [ ] Calculate Block Size (Block Size = 256 - last non-255 octet)
        - [ ] Find Network Address (e.g., 192.168.1.0)
        - [ ] Find Broadcast Address (e.g., 192.168.1.255)
        - [ ] Find Usable IP Range
        - [ ] Subnet Increment Challenge (Find the next subnet in a range)

- User Interaction:
    - CLI:
        - [ ] Input prompt for user's answers

    - GUI:
        - [WIP]

- Score System:
    - [WIP]