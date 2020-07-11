# ******************************************************************************************************************* #
#CSC 2560 Networks and Information Technologies
# Tennessee Tech University
# Subnetting: Lab 02
# Author: Bethanie Williams
# Sources: bit.ly/2ZM21F5
# Sources: bit.ly/3f4Knme
# Created: 7/4/20
# ******************************************************************************************************************* #

import socket
import struct


def valid_ip_address(users_ip):  # ensures that octect numbers must be between 0 and 255
    if ([0 <= users_ip["OctetOne"] <= 255 and
         0 <= users_ip["OctetTwo"] <= 255 and  # all 4 octects have to be satisfied
         0 <= users_ip["OctetThree"] <= 255 and
         0 <= users_ip["OctetFour"] <= 255]):
        return True
    raise ValueError  # will not be a valid IP address unless octect numbers are less than 255 and greater than 0


def valid_cidr(cidr_value):
    if 8 <= cidr_value <= 30:  # cidr value must always lie between these digits
        return True
    raise ValueError


def user_cidr(cidr_value):
    next_block_address = three_class_boundaries(cidr_value)
    block_size = subnet_block_size(cidr_value, next_block_address)

    print("General Network Information")
    print("------------------------------------------------")
    network_bits_ones = cidr_value
    host_bits_zeros = 32 - int(network_bits_ones)
    subnet_mask = socket.inet_ntoa(        # referred to stack overflow on this equation
        struct.pack('!I', (1 << 32) - (1 << host_bits_zeros)))  # imported socket and structure
    print("Subnet Mask = ", subnet_mask)

    subnet_counter = 0
    for sub in range(0, 255, block_size):
        str(subnet_counter)
        subnet_counter += 1

    print("Number of Subnets = ", str(subnet_counter))
    print("Number of Hosts per Subnet = ", ((2**host_bits_zeros)-2))

    # first_decimal = subnet_mask.index('.')
    # second_decimal = subnet_mask.index('.', first_decimal + 1,
    #                                    len(subnet_mask))  # splits the subnet masks based on decimal places
    # third_decimal = subnet_mask.index('.', second_decimal + 1, len(subnet_mask))
    #
    # binary_first_subnet_octet = bin(int(subnet_mask[0:first_decimal]))[2:]  # turns str back to integers & makes binary
    # binary_second_subnet_octet = bin(int(subnet_mask[first_decimal + 1:second_decimal]))[2:]
    # binary_third_subnet_octet = bin(int(subnet_mask[second_decimal + 1:third_decimal]))[2:]
    # binary_fourth_subnet_octet = bin(int(subnet_mask[third_decimal + 1:len(subnet_mask)]))[2:]
    #
    # binary_result = binary_first_subnet_octet + binary_second_subnet_octet + \
    #         binary_third_subnet_octet + binary_fourth_subnet_octet
    #
    # print("The Binary result is",binary_result)
    #
    # binary_result_dict = {"OctetOne": binary_first_subnet_octet, "OctetTwo": binary_second_subnet_octet,
    #                       "OctetThree": binary_third_subnet_octet,
    #                       "OctetFour": binary_fourth_subnet_octet}  # puts splitted values into a dictionary
    # print("The binary form is:", binary_result_dict)  # if unsure of splitted binary values just uncomment this
    #
    # whole_binary_subnet_mask = "".join(
    #     binary_first_subnet_octet + binary_second_subnet_octet + # combines the whole binary number together
    #     binary_third_subnet_octet + binary_fourth_subnet_octet)   # only gets the binary values after the 0b
    #
    # print("The whole binary number =", (whole_binary_subnet_mask))


def three_class_boundaries(cidr_value):  # this function is important in calculate block size
    if 8 <= cidr_value < 16:  # if CIDR value is between 8 and 16 its class A
        return 16
    elif 16 <= cidr_value < 24:  # if CIDR value is between 16 and 24 its class B
        return 24
    elif 24 <= cidr_value < 32:  # if CIDR value is between 24 and 32 its class C
        return 32
    else:
        return 0


def split_octects(users_ip):  # keeps IP address as a string
    first_decimal = users_ip.index('.')
    second_decimal = users_ip.index('.', first_decimal + 1, len(users_ip))  # splits the octect values based on decimal places
    third_decimal = users_ip.index('.', second_decimal + 1, len(users_ip))

    first_octet = int(users_ip[0:first_decimal])  # turns string back into integers
    second_octet = int(users_ip[first_decimal + 1:second_decimal])
    third_octet = int(users_ip[second_decimal + 1:third_decimal])
    fourth_octet = int(users_ip[third_decimal + 1:len(users_ip)])

    ip_split_dict = {"OctetOne": first_octet, "OctetTwo": second_octet, "OctetThree": third_octet,
                     "OctetFour": fourth_octet}  # puts splitted values into a dictionary
    # print("The Ip Address form splitted is:", ip_split_dict)
    return ip_split_dict


# calculates block size
def subnet_block_size(cidr_value, block_address_span): # reference Quora (https://www.quora.com/
    return 2 ** (block_address_span - cidr_value)         # How-do-I-find-out-the-IP-block-size#:~:text=To%20find%20
    # the block spans across (num) addresses- CIDR value  # out%20the%20block,is%20the%20number%20of%20addresses.


def class_a(users_ip, cidr_value):
    print('Network Address = ' + str(users_ip['OctetOne']) + '.', end='')
    print("")
    print("--------------------------------------------------")
    next_block_address = three_class_boundaries(cidr_value)  # calls to see what class the IP belongs
    block_size = subnet_block_size(cidr_value, next_block_address)  # calculates the block size that will be used
    layout = "{0:>10}{1:>12}{2:>14}{3:>14}"  # basically creates spacing for table/ table manually created

    subnet_counter = 0
    print(layout.format("Subnet", "First Host", "Last Host", "Broadcast"))  # table titles
    for subnet in range(0, 255, block_size):
        print(layout.format(str(subnet) + '.0' + '.0', str(subnet) + '.0' + '.1', str((subnet + block_size) - 1)
                            + '.255' + '.254', str((subnet + block_size) - 1) + '.255' + '.255'))
        if subnet_counter == 8:
            break
    print("--------------------------------------------------")


def class_b(users_ip, cidr_value): # calculates subnets for class B
    print('Network Address = ' + str(users_ip['OctetOne']) + '.' + str(users_ip['OctetTwo']) + '.', end='')
    print("")# prints network address with the two octects are bits for networks
    print("------------------------------------------------")
    next_block_address = three_class_boundaries(cidr_value)  # calls to see what class the IP belongs
    block_size = subnet_block_size(cidr_value, next_block_address)  # calculates the block size that will be used
    layout = "{0:>10}{1:>12}{2:>12}{3:>14}"  # basically creates spacing for table/ table manually created

    subnet_counter = 0
    print(layout.format("Subnet", "First Host", "Last Host", "Broadcast"))  # table titles
    for subnet in range(0, 255, block_size):
        print(layout.format(str(subnet) + '.0', str(subnet) + '.1', str((subnet + block_size) - 1)
                            + '.254', str((subnet + block_size) - 1) + '.255'))
        str(subnet_counter)
        subnet_counter += 1
        if subnet_counter == 8:
            break
    print("------------------------------------------------")


def class_c(users_ip, cidr_value):  # calculates subnets for class C
    print('Network Address = ' + str(users_ip['OctetOne']) + '.' + str(users_ip['OctetTwo']) + '.' + str(
        users_ip['OctetThree']) + '.', end='')  # prints network address with the three octects are bits for networks
    print("")
    print("------------------------------------------------")
    next_block_address = three_class_boundaries(cidr_value)
    block_size = subnet_block_size(cidr_value, next_block_address)
    layout = "{0:>10}{1:>12}{2:>12}{3:>14}"  # basically creates spacing for table/ table manually created

    subnet_counter = 0  # counter to see how many results will be in table
    print(layout.format("Subnet", "First Host", "Last Host", "Broadcast"))  # table titles
    for subnet in range(0, 255, block_size):  # gets values of all titles in range 0-255 & each step is block address
        print(layout.format(str(subnet), str(subnet + 1), str((subnet + block_size) - 2), str((subnet + block_size) - 1)))
        str(subnet_counter)
        subnet_counter += 1
        if subnet_counter == 8:  # once the counter for the table is 8 it will only print 8 results
             break

    print("------------------------------------------------")


def table(cidr_value, users_ip):
    class_selector = three_class_boundaries(cidr_value)

    if class_selector == 16:  # if the highest boundary for class a
        class_a(users_ip, cidr_value)  # then run ip in the class it belongs
    elif class_selector == 24:
        class_b(users_ip, cidr_value)   # same as above but for class b
    elif class_selector == 32:
        class_c(users_ip, cidr_value)  # same as above but for class c
    else:
        pass


def main():
    while True:
        try:  # Gets I.P. address and validates the user's input/format
            users_ip = input("Please enter a valid IP Address; the values must range from 0-255 in the (X.X.X.X) format.")
            split_octects(users_ip)  # splits users up into octects
            valid_ip_address(split_octects(users_ip))
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

    user_cidr(int(cidr))        # produces results for subnet mask, binary form of subnet mask, number of subnets,
                                # and hosts per subnet
    table(cidr, split_octects(users_ip))  # Display Subnet, First Host, Last Host, and Broadcast


if __name__ == "__main__":
    main()