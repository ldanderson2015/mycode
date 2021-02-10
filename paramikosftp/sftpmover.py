#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os
from ipaddress import ip_address, IPv4Address, IPv6Address

while input('xfer files? (Y/n)').lower() != 'n':
    try:
        ip = ip_address(input("Enter an IP address (IPv4 only)"))
        if (type(ip) == IPv6Address):
            print('ipv6 input not supported at this time') 
    except ValueError:
        print('invalid input detected.')
        break

    ip = str(ip)
    user = input('enter username: ')
    passwd = input('enter password: ')
    
    ## where to connect to
    t = paramiko.Transport(ip, 22) ## IP and port
    
    ## how to connect (see other labs on using id_rsa private/public keypairs)
    t.connect(username=user, password=passwd)
    
    ## Make an sftp connection object
    sftp = paramiko.SFTPClient.from_transport(t)
    
    ## iterate across the files within directory
    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
        if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
            sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location
    
    ## close the connection
    sftp.close() # close the connection

