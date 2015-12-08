#!/usr/bin/python
# -*- coding: utf-8 -*-

# set_icon_and_title.py
import sys
import sys
import glob
import serial
from tkinter import *

root = Tk()

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





class show_gui(object):
    
    def __init__(self):
        print_button = Button(root, text='Show existing COM ports!', command=showCOMs)
        print_button.grid(row=0, column=1)
        # Image path provided as first command line arg. PNG format
        #root.iconphoto(root, PhotoImage(file=sys.argv[1])) 

        my_text2 = Label(root, text='Choose COM port')
           
        my_text3= Label(root, text='Choose baud rate')
        my_text2.grid(row=4, column=1)
        my_text3.grid(row=5, column=1)

        e1 = Entry(root)
        e2 = Entry(root)

        e1.grid(row=4, column=2)
        e2.grid(row=5, column=2)

        Button(root, text='Read data', command=read_entries).grid(row=3, column=2 )
        root.title("data visualization")
        root.geometry("350x200+500+500")

        menu_bar = Menu(root)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label=" Quit", command=root.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)
        root.config(menu=menu_bar)

        root.mainloop()

    def showCOMs(self):
        print (serial_ports())
        my_text2 = Label(root, text='Available COM ports:')
        
        my_text3= Label(root, text=serial_ports())
        my_text2.grid(row=1, column=1)
        my_text3.grid(row=2, column=1)


    def read_entries(self):
        port=e1.get()
        try:
            baud = int(e2.get())
        except ValueError:
            Label(root, text="That's not a valid baud rate!").grid(row=9, column=2)
        if port in serial_ports():

            START_button = Button(root, text='Start visualization!', command=showCOMs).grid(row=8, column=2)
        else:
            Label(root, text='The selected COM port is not available!').grid(row=6, column=2)
            Label(root, text='Choose an other one!').grid(row=7, column=2)


if __name__ == '__main__':
    show_gui()  