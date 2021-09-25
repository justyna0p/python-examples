#Task: Change from "." in IP address to "[.]"

def change_IP_address(address):
    new_address = address.replace(".", "[.]")
    return new_address

address = "192.168.8.10"
print(change_IP_address(address))
