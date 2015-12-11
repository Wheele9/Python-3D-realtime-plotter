#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import glob
import serial
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib as mpl


def make_the_plotss(port1, baud1, duration):


    plt.ion()
    mpl.rcParams['toolbar'] = 'None'
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x=1
    y=2
    z=6

    while 1 :

            x=x+1
            y=y+1.5
            ax.scatter(x,y,z)
            ax.set_xlim([0, 100])
            ax.set_ylim([0, 100])
            ax.set_zlim([0, 100])
            ax.set_xlabel('x [cm]')
            ax.set_ylabel('y [cm]')
            ax.set_zlabel('z [cm]')
            plt.tight_layout()
            plt.draw()
            plt.pause(0.003)

if __name__ == '__main__':

    ###MODIFY THEESE :D ####
    make_the_plotss('COM7',9600,100)   