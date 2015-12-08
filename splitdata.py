#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import sys
import time

text='34	5634	53\r'

print (text)

x=float(text.split()[0])
y=float(text.split()[1])
z=float(text.split()[2])

print (2*x)