# CSC 2560 Networks and Information Technologies
# Subnetting: Lab 02
# Author: Bethanie Williams
# Sources: bit.ly/2ZM21F5
#Sources: bit.ly/3f4Knme
# Created: 7/4/20
#
import socket
import struct
from prettytable import PrettyTable


def valid_IP_Address(users_IP):  # ensures that octect numbers must be between 0 and 255
    ipDict = users_IP

    if ([0 <= ipDict["FirstOctet"] <= 255 and
         0 <= ipDict["SecondOctet"] <= 255 and  # all 4 octects have to be satisfied
         0 <= ipDict["ThirdOctet"] <= 255 and
         0 <= ipDict["FourthOctet"] <= 255]):
        return True
    raise ValueError  # will not be a valid IP address unless octect numbers are less than 255 and greater than 0


def valid_cidr(cidr_value):
    if 8 <= cidr_value <= 30:  # cidr value must always lie between these digits
        return True
    raise ValueError


def user_cidr(cidr_value):  
    print("General Network Information")
    print("----------------------------")
    net_bits = cidr_value
    host_bits_zeros = 32 - int(net_bits)
    subnet_mask = socket.inet_ntoa(        # referred to stack overflow on this equation
        struct.pack('!I', (1 << 32) - (1 << host_bits_zeros)))  # imported socket and structure
    print("The subnet mask is", subnet_mask)
    # print("The number of hosts are", host_bits_zeros)

    first_decimal = subnet_mask.index('.')
    second_decimal = subnet_mask.index('.', first_decimal + 1,
                                       len(subnet_mask))  # splits the subnet masks based on decimal places
    third_decimal = subnet_mask.index('.', second_decimal + 1, len(subnet_mask))

    binary_first_subnet_octet = bin(int(subnet_mask[0:first_decimal]))  # turns string back into integers and makes them binary
    binary_second_subnet_octet = bin(int(subnet_mask[first_decimal + 1:second_decimal]))
    binary_third_subnet_octet = bin(int(subnet_mask[second_decimal + 1:third_decimal]))
    binary_fourth_subnet_octet = bin(int(subnet_mask[third_decimal + 1:len(subnet_mask)]))
    # if len(binary_fourth_subnet_octet) < 8:
    #     binary_fourth_subnet_octet.zfill(8)
    # else:
    #     binary_fourth_subnet_octet

    binary_result_dict = {"FirstOctet": binary_first_subnet_octet[2:], "SecondOctet": binary_second_subnet_octet[2:],
                          "ThirdOctet": binary_third_subnet_octet[2:],
                          "FourthOctet": binary_fourth_subnet_octet[2:]}  # puts splitted values into a dictionary
    print("The binary form is:", binary_result_dict)  # if unsure of splitted binary values just uncomment this

    whole_binary_subnet_mask = "".join(
        binary_first_subnet_octet[2:] + binary_second_subnet_octet[2:] + # combines the whole binary number together
        binary_third_subnet_octet[2:] + binary_fourth_subnet_octet[2:])   # only gets the binary values after the 0b

    print("The whole binary number =", (whole_binary_subnet_mask))

    count_ones_in_whole = whole_binary_subnet_mask.count("1")
    # print(count_ones_in_whole)
    number_of_subnets = (2 ** count_ones_in_whole)
    print("Number of subnets = ", number_of_subnets)
    count_zeros_in_whole = whole_binary_subnet_mask.count("0")
    # print(count_zeros_in_whole)
    number_of_hosts = (2 ** count_zeros_in_whole - 2)
    print("Number of hosts = ", number_of_hosts)


def calculate_3_class_boundaries(cidr_value):  # this function is important in calculate block size
    if 8 < cidr_value < 16:  # if CIDR value is between 8 and 16 its class A
        return 16
    elif 16 < cidr_value < 24:  # if CIDR value is between 16 and 24 its class B
        return 24
    elif 24 < cidr_value < 32:  # if CIDR value is between 24 and 32 its class C
        return 32
    else:
        return 0


def split_octects(users_IP):  # keeps IP address as a string
    first_decimal = users_IP.index('.')
    second_decimal = users_IP.index('.', first_decimal + 1, len(users_IP))  # splits the octect values based on decimal places
    third_decimal = users_IP.index('.', second_decimal + 1, len(users_IP))

    first_octet = int(users_IP[0:first_decimal])  # turns string back into integers
    second_octet = int(users_IP[first_decimal + 1:second_decimal])
    third_octet = int(users_IP[second_decimal + 1:third_decimal])
    fourth_octet = int(users_IP[third_decimal + 1:len(users_IP)])

    ip_split_dict = {"FirstOctet": first_octet, "SecondOctet": second_octet, "ThirdOctet": third_octet,
                     "FourthOctet": fourth_octet}  # puts splitted values into a dictionary
    # print("The Ip Address form splitted is:", ip_split_dict)
    return ip_split_dict


def calc_3_class_boundaries(cidr_value):  # sets boundaries for the different subnet classes
    if 8 < cidr_value < 16:  # class A
        return 16
    elif 16 < cidr_value < 24:  # class B
        return 24
    elif 24 < cidr_value < 32:  # class C
        return 32
    else:
        return 0

# calculates block size
def calculate_block_size(cidr_value, block_address_span): # reference Quora (https://www.quora.com/
    return 2 ** (block_address_span - cidr_value)         # How-do-I-find-out-the-IP-block-size#:~:text=To%20find%20
    # the block spans across (num) addresses- CIDR value  # out%20the%20block,is%20the%20number%20of%20addresses.


def calc_subnet_class_A(ipDict, cidr_value):
    print('Network Address = ' + str(ipDict['FirstOctet']) + '.', end='')
    print("")
    print("----------------------------")
    next_block_address = calc_3_class_boundaries(cidr_value)
    block_size = calculate_block_size(cidr_value, next_block_address)
    print('Network Address = ' + str(ipDict['FirstOctet']) + '.', end='')

    for subnet in range(0, 255, block_size):
        print('Subnet ', subnet + .0 + .0, end='')
        print(' First Host = ', subnet + .0 + .1, end='')
        print(' Last Host = ', (subnet + block_size) - 1 + .255 + .254)
        print(' Broadcast Address =', (subnet + block_size) - 1 + .255 + .255)


def calc_subnet_class_B(ipDict, cidr_value):
    print('Network Address = ' + str(ipDict['FirstOctet']) + '.' + str(ipDict['SecondOctet']) + '.', end='')
    print("")
    print("----------------------------")
    next_block_address = calc_3_class_boundaries(cidr_value)
    block_size = calculate_block_size(cidr_value, next_block_address)

    for subnet in range(0, 255, block_size):
        print(' Subnet = ', subnet, .0, end='')
        print(' First Host = ', subnet + .1, end='')
        print(' Last Host = ', (subnet + block_size) - 1 + .254)
        print('Broadcast Address = ', (subnet + block_size) - 1 + .255)


def calc_subnet_class_C(ipDict, cidr_value):
    print('Network Address = ' + str(ipDict['FirstOctet']) + '.' + str(ipDict['SecondOctet']) + '.' + str(
        ipDict['ThirdOctet']) + '.', end='')
    print("")
    print("----------------------------")
    next_block_address = calc_3_class_boundaries(cidr_value)
    block_size = calculate_block_size(cidr_value, next_block_address)

    for subnet in range(0, 255, block_size):  # prints out numbers w/in range of 0-255 and steps of the block size chunks
        print(' Subnet = ', subnet, end='')
        print(' First Host = ', (subnet + 1), end='')
        print(' Last Host = ', ((subnet + block_size) - 2))
        print(' Broadcast Address = ', (subnet + block_size) - 1)

        # results = PrettyTable()
        # results.field_names = [" Subnet", "First Host", "Last Host", "Broadcast Address"]
        # results.add_row = ([subnet, (subnet + 1), ((subnet + block_size) - 2), ((subnet + block_size) - 1)])
        # print(results)


def table_results(cidr_value, ipDict):
    class_selector = calc_3_class_boundaries(cidr_value)

    if class_selector == 16:
        calc_subnet_class_A(ipDict, cidr_value)
    elif class_selector == 24:
        calc_subnet_class_B(ipDict, cidr_value)
    elif class_selector == 32:
        calc_subnet_class_C(ipDict, cidr_value)
    else:
        pass


def main():
    while True:
        try:  # Gets I.P. address and validates the user's input/format
            users_IP = input("Please enter a valid I.P. Address; the values must range from 0-255 in the (X.X.X.X) format.")
            ipAddDict = split_octects(users_IP)
            valid_IP_Address(ipAddDict)
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

    user_cidr(int(cidr))  # produces results for subnet mask and binary form of subnet mask
    table_results(cidr, ipAddDict)  # Display Subnet Addresses, First Host, Last Host, and Broadcast Addresses


if __name__ == "__main__":
    main()