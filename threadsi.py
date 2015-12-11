#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
import time
def secondthread():


	while 1:
		print (dataa)
		time.sleep(1)

def changedat():
	global dataa
	dataa=23


dataa = 22



t = threading.Thread(target=secondthread)

t.start()

time.sleep(4)
print ("dataa changed in main thread:")
changedat()