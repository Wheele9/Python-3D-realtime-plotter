#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import serial

port = 'COM7'
baudrate = 9600
ser = serial.Serial(port, baudrate)

print (ser.isOpen())  

print (ser.isOpen())