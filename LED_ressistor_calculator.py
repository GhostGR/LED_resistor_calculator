# LED resistor calculator
# Copyright (c) 2016 Lykourgos Tanious
# Read LICENCE.txt
# Description :      A script that calculates the required
#               resistance and wattage to properly run a LED.
# Author      : Lykourgos Tanious
# date        : 09/02/2016
# Version     : V1.0


def main():
    while True:
        print("################################################\n"
              "#         LED Resistor Value Calculator        #\n"
              "#==============================================#\n"
              "#     Copyright (c) 2015 Lykourgos Tanious     #\n"
              "#----------------------------------------------#\n"
              "#     Version : V1.0                           #\n"
              "#     Author  : Lykourgos Tanious              #\n"
              "################################################\n")
        while True:
            try:
                vin = float(input("power supply voltage(V)? :  "))
                break
            except:
                print("Invalid input, it must be a number")
        while True:
            try:
                vled = float(input("LED forward voltage(V)? :  "))
                break
            except:
                print("Invalid input, it must be a number")
        while True:
            try:
                Ima = float(input("operating current of the LED(ma)? :  "))
                break
            except:
                print("Invalid input, it must be a number")
        print("\n"
              "Input Voltage          :  ", vin, "V\n"
              "LED forward voltage    :  ", vled, "V\n"
              "LED operating current  :  ", Ima, "ma\n"
              "------------------------------------------------\n"
              "Resistor :  (", vin, "-", vled, ")/(", Ima, "/1000) =  ", (vin-vled)/(Ima/1000), "ohms\n"
              "Wattage  :   ", vin, "*", "(", Ima, "/1000", ")", "     =  ", (vin*(Ima/1000)), "W\n"
              "\n")
        while True:
            inp = input("Do you want to exit(Y/N)?  ")
            if inp == "Y" or inp == "y":
                exit(0)
            elif inp == "N" or inp == "n":
                break

main()
