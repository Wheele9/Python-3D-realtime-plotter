#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import sys
import time

port = 'COM7'

baudrate = 9600


ser = serial.Serial(port, baudrate)


print(2)
while 1:
    print (ser.readline())
    print (33)