#Task: Change from "." in IP address to "[.]"

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

address = "192.168.8.10"
print(change_IP_address(address))

number = 180
converted_bianry = convert_number_to_binary(number)
print(converted_bianry)
