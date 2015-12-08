"""
reading serial
"""
import sys
import glob
import serial
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


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

def make_the_plot(port1, baud1):
    #print (serial_ports())
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    port = port1
    baudrate = baud1
    ser = serial.Serial(port, baudrate)

    while ser:
    	raw = (ser.readline())
    	splitted= raw.split()
    	print (11,raw)

    	print (22,splitted)

    	x=float(splitted[0])
    	y=float(splitted[1])
    	z=float(splitted[2])
    	print(x+1000)
    	print(y)
    	print(z)
    	ax.scatter(x,y,z)
    	ax.set_xlim([0, 50])
    	ax.set_ylim([0, 50])
    	ax.set_zlim([0, 55])
    	ax.set_xlabel('x axis')
    	ax.set_ylabel('y axis')
    	ax.set_zlabel('z axis')

    	plt.draw()
    	plt.pause(0.01)
    	ax.cla()

	
if __name__ == '__main__':
    make_the_plot('COM7',9600)   