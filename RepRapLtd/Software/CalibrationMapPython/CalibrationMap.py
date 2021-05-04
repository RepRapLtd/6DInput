# Python code to create a calibration map from two Hall sensors and a magnet

import serial
import time

arduinoPort = '/dev/ttyUSB0'
reprapPort = '/dev/ttyACM0'

def MoveRepRap(x, y, z, f, port):
 s = "G1 X"
 s += str(x)
 s += " Y"
 s += str(y)
 s += " Z"
 s += str(z)
 s += " F"
 s += str(f)
 s += "\n"
 print(s)
 port.write(str.encode(s))

def GetArduinoVoltages(usb):
 usb.write(str.encode('v\n'))
 data = usb.readline()
 return data

def OpenArduinoUSB():
 usb = serial.Serial(arduinoPort,115200,timeout=0.1)
 time.sleep(3) # Why so long???
 return usb

def OpenRepRapUSB():
 usb = serial.Serial(reprapPort,115200,timeout=0.1)
 #time.sleep(3) # Why so long???
 return usb


#aUSB = OpenArduinoUSB()
rUSB = OpenRepRapUSB()
MoveRepRap(0, 0, 0, 1000, rUSB)
for i in range(10):
 MoveRepRap(i, 0, 0, 1000, rUSB)
 MoveRepRap(0, i, 0, 1000, rUSB)
# print(GetArduinoVoltages(usb))


