import serial
import numpy
import matplotlib.pyplot as plt
from drawnow import *

#things to install
#matplotlib
#drawnow
#vpython


xArray = []
yArray = []

arduinoData = serial.Serial('/dev/tty.usbmodem1411',9600)
plt.ion()
cnt = 0
def makeFig():
    plt.title('recycle')
    plt.plot(xArray, '-ro', label='paper')
    plt.legend(loc='upper left')
    plt2=plt.twinx()
    plt2.plot(yArray, 'b^-', label='plastic')
    plt2.legend(loc='upper center')
    #theres only two graph here
    #gonna add another one


while True:
    while (arduinoData.inWaiting()==0):
        pass

    arduinoString = arduinoData.readline()
    dataArray = arduinoString.split(',')
    x = float(dataArray[0])
    y = float(dataArray[1])
    xArray.append(x)
    yArray.append(y)
    drawnow(makeFig)
    plt.pause(.01)
    cnt=cnt+1
    if (cnt>10):
        xArray.pop(0)
        yArray.pop(0)

    print x, ",", y
