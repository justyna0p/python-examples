def change_IP_address(address):
    new_address = address.replace(".", "[.]")
    return new_address

def convert_number_to_binary(number):
    binary = ""
    if number >= 128:
        binary += "1"
        number -= 128
    else:
        binary += "0"
    if number >= 64:
        binary += "1"
        number -= 64
    else:
        binary += "0"
    if number >= 32:
        binary += "1"
        number -= 32
    else:
        binary += "0"
    if number >= 16:
        binary += "1"
        number -= 16
    else:
        binary += "0"
    if number >= 8:
        binary += "1"
        number -= 8
    else:
        binary += "0"
    if number >= 4:
        binary += "1"
        number -= 4
    else:
        binary += "0"
    if number >= 2:
        binary += "1"
        number -= 2
    else:
        binary += "0"
    if number >= 1:
        binary += "1"
        number -= 1
    else:
        binary += "0"

    return binary

def convert_IP_address_to_bianry(address):
    splitted = address.split(".")
    binary_IP = ""
    for n in splitted:
        binary_IP += convert_number_to_binary(int(n))

    return binary_IP

#Task: Change from "." in IP address to "[.]"
address = "192.168.8.10"
print(change_IP_address(address))

#Task: Change IP address into binary address
number = 180
converted_bianry = convert_number_to_binary(number)
print(converted_bianry)

bianry_address = convert_IP_address_to_bianry(address)
print(bianry_address)