#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import glob
import serial
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib as mpl


def make_the_plot(port1, baud1, duration):


    plt.ion()
    mpl.rcParams['toolbar'] = 'None'
    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')

    port = port1 
    baudrate = baud1
    ser = serial.Serial(port, baudrate)

    maxtime=2*duration ##considering delays in ardu code 
    realtime=0
    while ser and realtime<maxtime:

        raw = (ser.readline())
        splitted= raw.split()
        realtime=realtime+1
        #print (realtime, maxtime)
        if 'reading' in splitted:

            print("error in sensor reading")
            msg = "Error in sensor readng"+raw
            return msg  
        try:
            ax.cla()
            x=float(splitted[0])
            y=float(splitted[1])
            z=float(splitted[2])

            ax.scatter(x,y,z)
            ax.set_xlim([0, 100])
            ax.set_ylim([0, 100])
            ax.set_zlim([0, 100])
            #fig.suptitle("Title centered above all subplots", fontsize=14)
            ax.set_xlabel('x [cm]')
            ax.set_ylabel('y [cm]')
            ax.set_zlabel('z [cm]')
            plt.tight_layout()
            plt.draw()
            plt.pause(0.003)
                
        except:
            pass
            
        msg="time's up"

    print (msg)
    return msg    

if __name__ == '__main__':

    ###MODIFY THEESE :D ####
    make_the_plot('COM7',9600,100)   