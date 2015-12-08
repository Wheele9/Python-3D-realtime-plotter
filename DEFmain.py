"""
reading serial
"""
import sys
import glob
import serial
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt



def make_the_plot(port1, baud1, duration):
    print (22, duration)
    #print (serial_ports())
    plt.ion()
    fig = plt.figure()
    #fig.tight_layout()
    ax = fig.add_subplot(111, projection='3d')

    port = port1
    baudrate = baud1
    ser = serial.Serial(port, baudrate)


    ###write to start action
    #command=b"\x89\x45\x56"
    #ser.write(command)
    cc=0
    while ser and cc<duration:
        raw = (ser.readline())
        splitted= raw.split()
        cc=cc+1
        print (cc)
        # if len(splitted)<3:
        #     pass
        # else:
        if 'reading' in splitted:
            #break
            print("error in sensor reading")
            msg = "Error in sensor readng"+raw
            return msg  
        try:
            x=float(splitted[0])
            y=float(splitted[1])
            z=float(splitted[2])

            ax.scatter(x,y,z)
            ax.set_xlim([0, 50])
            ax.set_ylim([0, 50])
            ax.set_zlim([0, 55])
            ax.set_xlabel('x [mm]')
            ax.set_ylabel('y [mm]')
            ax.set_zlabel('z [mm]')

            plt.draw()
            plt.pause(0.003)
            ax.cla()
        except:
            pass

    msg='Serial Connection lost'
    return msg    

if __name__ == '__main__':
    make_the_plot('COM7',9600,30)   