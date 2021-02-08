#!/usr/bin/env python3

my_list = ["192.168.0.5",5060,"UP"]

print("The first item in the list (IP):" + my_list[0])

print("The second item in the list (port): " + str(my_list[1]) )

print("The last item in the list (state): " + my_list[2] )

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print(f"The port numbers are {str(new_list[0])}, {new_list[1]}, {str(new_list[2])}. The IP Addresses are {new_list[3]} and {new_list[4]}. The protocol is {new_list[5]}.")
