# Sources: bit.ly/3f4Knme
# Created: 7/4/20
#
import socket
import struct


def valid_ip_address(ipAdd):  # ensures that octect numbers must be between 0 and 255
    ipDict = ipAdd
    if ([0 <= ipDict["OctetOne"] <= 255 and
         0 <= ipDict["OctetTwo"] <= 255 and  # all 4 octects have to be satisfied
         0 <= ipDict["OctetThree"] <= 255 and
         0 <= ipDict["OctetFour"] <= 255]):
        return True
    raise ValueError  # will not be a valid IP address unless octect numbers are less than 255 and greater than 0


def split_octects(users_IP):  # keeps IP address as a string
    first_decimal = users_IP.index('.')
    second_decimal = users_IP.index('.', first_decimal + 1,
                                    len(users_IP))  # splits the octect values based on decimal places
    third_decimal = users_IP.index('.', second_decimal + 1, len(users_IP))
    first_octet = int(users_IP[0:first_decimal])  # turns string back into integers
    second_octet = int(users_IP[first_decimal + 1:second_decimal])
    third_octet = int(users_IP[second_decimal + 1:third_decimal])
    fourth_octet = int(users_IP[third_decimal + 1:len(users_IP)])
    ip_split_dict = {"OctetOne": first_octet, "OctetTwo": second_octet, "OctetThree": third_octet,
                     "OctetFour": fourth_octet}  # puts splitted values into a dictionary
    # print("The Ip Address form splitted is:", ip_split_dict)
    return ip_split_dict


def valid_cidr(cidr_value):
    if 8 <= cidr_value <= 30:  # cidr value must always lie between these digits
        return True
    raise ValueError


def valid_class(letter):
    if letter == "A":
        # calculate_subnet_class_A(ipDict, subnet_mask)
        print("This is class A.")
        return True
    elif letter == "B":
        # calculate_subnet_class_B(ipDict, subnet_mask)
        print("This is class B")
        return True
    elif letter == "C":
        # calculate_subnet_class_C(ipDict, subnet_mask)
        print("This is class C")
        return True
    raise ValueError


def valid_subnet_mask(users_subnet_mask):
    subnet_dict = users_subnet_mask
    if ([0 <= subnet_dict["OctetOne"] <= 255 and
         0 <= subnet_dict["OctetTwo"] <= 255 and  # all 4 octects have to be satisfied
         0 <= subnet_dict["OctetThree"] <= 255 and
         0 <= subnet_dict["OctetFour"] <= 255]):
        return True
    raise ValueError


def splitting_octects(users_subnet_mask):  # keeps IP address as a string
    first_decimal = users_subnet_mask.index('.')
    second_decimal = users_subnet_mask.index('.', first_decimal + 1,
                                    len(users_subnet_mask))  # splits the octect values based on decimal places
    third_decimal = users_subnet_mask.index('.', second_decimal + 1, len(users_subnet_mask))
    first_octet = int(users_subnet_mask[0:first_decimal])  # turns string back into integers
    second_octet = int(users_subnet_mask[first_decimal + 1:second_decimal])
    third_octet = int(users_subnet_mask[second_decimal + 1:third_decimal])
    fourth_octet = int(users_subnet_mask[third_decimal + 1:len(users_subnet_mask)])
    subnet_split_dict = {"OctetOne": first_octet, "OctetTwo": second_octet, "OctetThree": third_octet,
                     "OctetFour": fourth_octet}  # puts splitted values into a dictionary
    # print("The Ip Address form splitted is:", subnet_split_dict)
    return subnet_split_dict


def convert_subnet_binary(subnet_split_dict):
    first_decimal = subnet_split_dict.index('.')  # splits the subnet masks based on decimal places
    second_decimal = subnet_split_dict.index('.', first_decimal + 1, len(subnet_split_dict))
    third_decimal = subnet_split_dict.index('.', second_decimal + 1, len(subnet_split_dict))
    binary_first_subnet_octet = bin(int(subnet_split_dict[0:first_decimal]))[2:]  # turns str back to integers & makes binary
    binary_second_subnet_octet = bin(int(subnet_split_dict[first_decimal + 1:second_decimal]))[2:]
    binary_third_subnet_octet = bin(int(subnet_split_dict[second_decimal + 1:third_decimal]))[2:]
    binary_fourth_subnet_octet = bin(int(subnet_split_dict[third_decimal + 1:len(subnet_split_dict)]))[2:]
    binary_result = binary_first_subnet_octet + binary_second_subnet_octet + \
                    binary_third_subnet_octet + binary_fourth_subnet_octet
    print("The Binary result is", binary_result)

def table_results(letter, ipDict, subnet_mask):
    class_selector = valid_class(letter)
    # if class_selector == "A":
     # calc_subnet_class_A(ipDict, cidr_value)
    # elif class_selector == "B":
    # calc_subnet_class_B(ipDict, cidr_value)
    if class_selector == "C":
        (calculate_subnet_class_C(ipDict, subnet_mask))
    else:
        pass


def calculate_block_size(subnet_mask):
    return int(256-subnet_mask)  # diff way


def calculate_subnet_class_C(ipDict, subnet_mask):  # calculates subnets for class C
    print('Network Address = ' + str(ipDict['OctetOne']) + '.' + str(ipDict['OctetTwo']) + '.' + str(
        ipDict['OctetThree']) + '.', end='')  # prints network address with the three octects are bits for networks
    print("")
    print("------------------------------------------------")
#     next_block_address = calculate_3_class_boundaries(cidr_value)
    block_size = calculate_block_size(subnet_mask)
    layout = "{0:>10}{1:>12}{2:>12}{3:>14}"  # basically creates spacing for table
    subnet_counter = 0
    print(layout.format("Subnet", "First Host", "Last Host", "Broadcast"))  # table titles
    for subnet in range(0, 255, block_size):  # gets values of all titles in range 0-255 & each step is block address
        print(layout.format(str(subnet), str(subnet + 1), str((subnet + block_size) - 2), str((subnet + block_size) - 1)))
        str(subnet_counter)
        subnet_counter += 1
        if subnet_counter == 8:
             break
    print("------------------------------------------------")


def general_info(subnet_mask, cidr_value):
#     next_block_address = calculate_3_class_boundaries(cidr_value)
#     block_size = calculate_block_size(cidr_value, next_block_address)
#
    print("General Network Information")
    print("------------------------------------------------")
    print("The Subnet Mask = ", subnet_mask)
    network_bits_ones = cidr_value
    host_bits_zeros = 32 - int(network_bits_ones)
    print("Number of Hosts per Subnet = ", ((2 ** host_bits_zeros) - 2))
#     subnetmask = socket.inet_ntoa(  # referred to stack overflow on this equation
#         struct.pack('!I', (1 << 32) - (1 << host_bits_zeros)))  # imported socket and structure
#     # print("The number of network bits is:", network_bits_ones)
#     print("Subnet Mask = ", subnetmask)
#
#     subnet_counter = 0
#     for sub in range(0, 255, block_size):
#         str(subnet_counter)
#         subnet_counter += 1
#
#     print("Number of Subnets = ", str(subnet_counter))
#
#
#     binary_result_dict = {"OctetOne": binary_first_subnet_octet, "OctetTwo": binary_second_subnet_octet,
#                           "OctetThree": binary_third_subnet_octet,
#                           "OctetFour": binary_fourth_subnet_octet}  # puts splitted values into a dictionary
#     # print("The binary form is:", binary_result_dict)  # if unsure of splitted binary values just uncomment this
#
#     whole_binary_subnet_mask = "".join(
#         binary_first_subnet_octet + binary_second_subnet_octet +  # combines the whole binary number together
#         binary_third_subnet_octet + binary_fourth_subnet_octet)  # only gets the binary values after the 0b
#
#     # print("The whole binary number =", (whole_binary_subnet_mask))
#
#     # count_ones_in_whole = whole_binary_subnet_mask.count("1")
#     # print(count_ones_in_whole)
#     # number_of_subnets = (2 ** count_ones_in_whole)
#     # print("Number of subnets = ", number_of_subnets)
#     # count_zeros_in_whole = whole_binary_subnet_mask.count("0")
#     # print(count_zeros_in_whole)
#     # number_of_hosts = (2 ** count_zeros_in_whole - 2)
#     # print("Number of hosts = ", number_of_hosts)
#


def main():
    while True:
        try:  # Gets I.P. address and validates the user's input/format
            users_ip_address = input(
                "Please enter a valid IP Address; the values must range from 0-255 in the (X.X.X.X) format.")
            ipAddDict = split_octects(users_ip_address)
            valid_ip_address(ipAddDict)
        except ValueError:
            continue
        else:
            break
    while True:
        try:  # Gets CIDR values and validates the user's input/format
            cidr = int(input("CIDR values range from 8-30. Please enter the CIDR value: /"))
            valid_cidr(cidr)
        except ValueError:
            continue
        else:
            break
    while True:
        try:  # Gets CIDR values and validates the user's input/format
            users_subnet_mask = (input("Please enter a valid subnet mask: the values must range from 0-255 in the (X.X.X.X) format."))
            subnet_add_dict = splitting_octects(users_subnet_mask)
            valid_subnet_mask(subnet_add_dict)
        except ValueError:
            continue
        else:
            break
    while True:
        try:
            users_class = (input("Please enter which class the IP address belongs. Type A, B, or C  "))
            valid_class(users_class)
        except ValueError:
            continue
        else:
            break
    convert_subnet_binary(users_subnet_mask)
    general_info(users_subnet_mask, int(cidr))
    # user_cidr(user_subnet_mask)  # produces results for subnet mask and binary form of subnet mask
    table_results(users_class, ipAddDict, subnet_add_dict)  # Display Subnet, First Host, Last Host, and Broadcast