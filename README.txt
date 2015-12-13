
Overview
========

This script is a demo, showing an object moving in the 3D space in real time with matplotlib.

Requirements
============

* Python 3.5
* Pyserial
* matplotlib 

* Tested on Windows

Run
=======

Connect your microcontroller to the PC with serialport, and send the x, y, z coordinates.
Example:

Serial.print(x);
Serial.print('\t')
Serial.print(y);
Serial.print('\t')
Serial.print(z);
Serial.println("");

