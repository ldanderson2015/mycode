#!/usr/bin/env python3

import csv

def main():
    #open CSV dataset
    with open("vendor.csv","r") as vfile:
        vdata = csv.reader(vfile, delimiter=",")
        for row in vdata:
            print(f"IP Address {row[2]} requires the driver {row[3]}")

main()
