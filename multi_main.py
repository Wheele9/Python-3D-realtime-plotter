#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import sys
import glob
import serial
from tkinter import *
from multi_plot import make_the_plot
from minimal import make_the_plotss
from threading import Thread

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

    
    realtime=0
    while ser and realtime<duration:

        raw = (ser.readline())
        splitted= raw.split()
        realtime=realtime+1
        print (stopmsg)
        if 'reading' in splitted:

            print("error in sensor reading")
            msg = "Error in sensor readng "+raw
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

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
        On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def print_content():
    print(entry.get())

def showCOMs():
    print (serial_ports())
    my_text2 = Label(root, text='Available COM ports:',background='SlateGray1')
    
    my_text3= Label(root, text=serial_ports(),background='SlateGray1')
    my_text2.grid(row=1, column=1)
    my_text3.grid(row=2, column=1)

def read_entries():
    
    a=0
    b=0
    c=0
    
    l4=Label(root, text="Not valid duration!",background='SlateGray1')
    l4.grid(row=9, column=2)
    l1=Label(root, text='COMport unavailable!',background='SlateGray1')
    l1.grid(row=7, column=2)
    l3=Label(root, text="Not valid baudrate!",background='SlateGray1')
    l3.grid(row=8, column=2)
    
    

    try:
        global port
        port=e1.get().upper()
        if port in serial_ports():
            a=1
            
            l1.grid_remove()
            l1=Label(root, text="                                    ",background='SlateGray1')
            l1.grid(row=7, column=2)
    except ValueError:
        pass

    try:
        global baud
        baud = int(e2.get())
        b=1
        l3.destroy()
        l3=Label(root, text="                                        ",background='SlateGray1')
        l3.grid(row=8, column=2)
    except ValueError:
        pass

    try:
        global duration
        duration =int(e3.get())
        c=1
        l4.grid_remove()
        l4=Label(root, text="                                          ",background='SlateGray1')
        l4.grid(row=9, column=2)
    except ValueError:
        pass
 
    if a==1 and b==1 and c==1:

        pass
        START_button = Button(root, text='Start visualization!', command=star3d,bg="SteelBlue1",padx=5,pady=5).grid(row=8, column=2)
        
def star3d():
    global stopmsg
    stopmsg=0
    global t
    t=Thread(target=make_the_plot, args=(port,baud,duration))
    #msg=make_the_plot(port,baud, duration)
    #Label(root, text=msg, bg="SteelBlue1").grid(row=7, column=2)
    t.start()
    END_button = Button(root, text='End visualization!', command=end3d,bg="SteelBlue1",padx=5,pady=5).grid(row=9, column=2)

def end3d():

    stopmsg=1
    print ('endee')

def closeprog():
    quit()

root = Tk()
print_button = Button(root, text='Show existing COM ports!', command=showCOMs,bg="SteelBlue1",padx=5,pady=5)
print_button.grid(row=0, column=1)

my_text1 = Label(root, text='Choose COM port',background='SlateGray1').grid(row=4, column=1)
my_text2= Label(root, text='Choose baud rate',background='SlateGray1').grid(row=5, column=1)
my_text3= Label(root, text='Duration [n]',background='SlateGray1').grid(row=6, column=1)

e1 = Entry(root)
e1.grid(row=4, column=2)
e2 = Entry(root)
e2.grid(row=5, column=2)
e3 = Entry(root)
e3.grid(row=6, column=2)


Button(root, text='Read data', command=read_entries,bg="SteelBlue1",padx=5,pady=5).grid(row=3, column=2 )
root.title("data visualization")
root.geometry("300x250+500+500")
root.configure(background='SlateGray1')

root.mainloop()

