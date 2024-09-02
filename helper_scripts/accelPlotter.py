import csv
import time
import board
import digitalio
import adafruit_lis3dh
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import serial

ser = serial.Serial(port='/dev/ttyACM0',
                    baudrate=115200,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

interval = 30 # this is update interval in miliseconds for plot

fig, ax = plt.subplots()

t_vector = []
x_vector = []
y_vector = []
z_vector = []

def animate(i):
    data_read = ser.readline()
    data_read = data_read.strip()
    x = float(data_read.decode("utf-8"));
    # print(x, y, z)
    t_vector.append(i)
    x_vector.append(x)
    
    ax.clear()
    ax.plot(t_vector, x_vector, "r")
    
    if(i<20):
        ax.set_xlim([0,20])
    else:
        ax.set_xlim([i-20,i])
    
    ax.set_ylim([-10,10])

ani = FuncAnimation(fig, animate, interval=interval)
plt.show()

