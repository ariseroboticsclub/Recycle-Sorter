import smbus
import time
bus = smbus.SMBus(1)

#address on the arduino
address = 0x04

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

while True:
    var = input("enter 1-9:")
    if not var:
        continue

    writeNumber(var)
    print "RPI: arduino i sent you ", var
    time.sleep(5)

    number = readNumber()
    print "arduino: i received ", number
    print
    
