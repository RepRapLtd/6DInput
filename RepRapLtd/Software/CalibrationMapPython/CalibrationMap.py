# Python code to create a calibration map from two Hall sensors and a magnet

import serial
import time
import re

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
 data = str(data.decode('ascii'))
 data = re.findall('\d+', data)
 return data

def OpenArduinoUSB():
 usb = serial.Serial(arduinoPort,115200,timeout=0.1)
 time.sleep(3) # Why so long???
 return usb

def OpenRepRapUSB():
 usb = serial.Serial(reprapPort,115200,timeout=0.1)
 #time.sleep(3) # Why so long???
 return usb

def LogReadings():
 while True:
  print(GetArduinoVoltages(aUSB))
  time.sleep(0.5)

aUSB = OpenArduinoUSB()
#LogReadings()

rUSB = OpenRepRapUSB()
MoveRepRap(0, 0, 0, 1000, rUSB)

zMax = 10
xMax = 25
file0 = open('hall-calibration0.csv', 'w')
file1 = open('hall-calibration1.csv', 'w')

for z in range(zMax + 1):
 MoveRepRap(0, 0, z, 1000, rUSB)
 time.sleep(2)
 for x in range(xMax + 1):
  MoveRepRap(x, 0, z, 1000, rUSB)
  time.sleep(0.5)
  data = GetArduinoVoltages(aUSB)
  print(data[0], ' ', data[1])
  file0.write(data[0])
  file1.write(data[1])
  if x < xMax:
   file0.write(",")
   file1.write(",")
 file0.write("\n")
 file1.write("\n")



