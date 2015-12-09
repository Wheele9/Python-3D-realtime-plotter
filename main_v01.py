#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import sys
import glob
import serial
from tkinter import *
from plot_v01 import make_the_plot


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
        START_button = Button(root, text='Start visualization!', command=star3d,bg="SteelBlue1").grid(row=8, column=2)
        
def star3d():
    
    msg=make_the_plot(port,baud, duration)
    Label(root, text=msg).grid(row=7, column=2)

def closeprog():
    quit()

root = Tk()
print_button = Button(root, text='Show existing COM ports!', command=showCOMs,bg="SteelBlue1")
print_button.grid(row=0, column=1)

my_text1 = Label(root, text='Choose COM port',background='SlateGray1').grid(row=4, column=1)
my_text2= Label(root, text='Choose baud rate',background='SlateGray1').grid(row=5, column=1)
my_text3= Label(root, text='Duration [s]',background='SlateGray1').grid(row=6, column=1)

e1 = Entry(root)
e1.grid(row=4, column=2)
e2 = Entry(root)
e2.grid(row=5, column=2)
e3 = Entry(root)
e3.grid(row=6, column=2)


Button(root, text='Read data', command=read_entries,bg="SteelBlue1").grid(row=3, column=2 )
root.title("data visualization")
root.geometry("350x250+500+500")
root.configure(background='SlateGray1')
# menu_bar = Menu(root)
# file_menu = Menu(menu_bar, tearoff=0)
# file_menu.add_command(label=" Quit", command=closeprog)
# menu_bar.add_cascade(label="File", menu=file_menu)
# root.config(menu=menu_bar)

root.mainloop()

