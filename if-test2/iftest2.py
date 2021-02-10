#!/usr/bin/env python3

from ipaddress import ip_address, IPv4Address, IPv6Address

ipchk = input('Apply an IP address: ') # this line now prompts the user for input

try:
    ipchk = ip_address(ipchk)
except AddressValueError:
    print('You did not provide a valid IP Address! Aborting...')

if ipchk == '192.168.70.1': # if a match on '192.168.70.1'
    # indented under if
    print('Looks like the IP address of the Gateway was set: ' + ipchk + ' This is not recommended.')
elif (type(ipchk) == IPv4Address): # if any data is provided, this will test tru
    print(f'Looks like the IPv4 address was set: {ipchk}') # indented under if
elif (type(ipchk) == IPv6Address): 
    print(f'Looks like the IPv6 address was set: {ipchk}')
else: # if data is NOT provided
    print('You did not provide input.') # indented under else


