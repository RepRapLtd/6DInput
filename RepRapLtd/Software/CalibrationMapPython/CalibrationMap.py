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
 #print(s)
 port.write(str.encode(s))

def GetArduinoVoltages(usb):
 usb.write(str.encode('v\n'))
 data = usb.readline()
 return str(data.decode('ascii')).replace('\r', '').replace('\n', '')

def OpenArduinoUSB():
 usb = serial.Serial(arduinoPort,115200,timeout=0.1)
 time.sleep(3) # Why so long???
 return usb

def OpenRepRapUSB():
 usb = serial.Serial(reprapPort,115200,timeout=0.1)
 #time.sleep(3) # Why so long???
 return usb


aUSB = OpenArduinoUSB()
#while True:
# print(GetArduinoVoltages(aUSB))
# time.sleep(0.5)

rUSB = OpenRepRapUSB()
MoveRepRap(0, 0, 0, 1000, rUSB)
for z in range(11):
 MoveRepRap(0, 0, z, 1000, rUSB)
 time.sleep(2)
 for x in range(21):
  MoveRepRap(x, 0, z, 1000, rUSB)
  time.sleep(0.5)
  print(GetArduinoVoltages(aUSB))



