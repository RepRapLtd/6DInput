# Python code to create a calibration map from two Hall sensors and a magnet
#
# Adrian Bowyer
# RepRap Ltd
# https://reprapld.com
#
# 7 May 2021
#
# Licence: GPL
#

import serial
import time
import re
import math as maths
import sys

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

def GetHallSumAndDifference(usb):
 usb.write(str.encode('v\n'))
 data = usb.readline()
 data = str(data.decode('ascii'))
 data = re.findall('\d+', data)
 s = int(data[0]) + int(data[1])
 d = int(data[0]) - int(data[1])
 data = (s, d)
 return data

def OpenArduinoUSB():
 usb = serial.Serial(arduinoPort,115200,timeout=0.1)
 time.sleep(3) # Why so long???
 return usb

def OpenRepRapUSB():
 usb = serial.Serial(reprapPort,115200,timeout=0.1)
 return usb

def LogReadings():
 while True:
  print(GetHallSumAndDifference(aUSB))
  time.sleep(0.5)

def V2Length(a, b):
 d0 = a[0] - b[0]
 d1 = a[1] - b[1]
 return maths.sqrt(d0*d0 + d1*d1)

# Really dumb search function...

def FindXZ(data, hallMatrix):
 xz = (-1, -1)
 closeValue = sys.float_info.max
 for z in range(len(hallMatrix)):
  v = hallMatrix[z]
  for x in range(len(v)):
   d = v[x]
   dist = V2Length(d, data)
   if dist < closeValue:
    closeValue = dist
    xz = (x, z)
 return xz


aUSB = OpenArduinoUSB()
#LogReadings()

rUSB = OpenRepRapUSB()
MoveRepRap(0, 0, 0, 1000, rUSB)

zMax = 10
xMax = 25
file0 = open('../../Experiments/HallCalibration/hall-calibration0.csv', 'w')
file1 = open('../../Experiments/HallCalibration/hall-calibration1.csv', 'w')

hallMatrix = []

for z in range(zMax + 1):
 hallVector = []
 MoveRepRap(0, 0, z, 1000, rUSB)
 time.sleep(2)
 for x in range(xMax + 1):
  MoveRepRap(x, 0, z, 1000, rUSB)
  time.sleep(0.5)
  data = GetHallSumAndDifference(aUSB)
  print(data[0], ' ', data[1])
  file0.write(str(data[0]))
  file1.write(str(data[1]))
  hallVector.append(data)
  if x < xMax:
   file0.write(",")
   file1.write(",")
 hallMatrix.append(hallVector)
 file0.write("\n")
 file1.write("\n")

file0.close()
file1.close()

errorFile = open('../../Experiments/HallCalibration/xzErrors.csv', 'w')
errorMatrix = []

for z in range(zMax + 1):
 MoveRepRap(0, 0, z, 1000, rUSB)
 time.sleep(2)
 errorVector = []
 for x in range(xMax + 1):
  MoveRepRap(x, 0, z, 1000, rUSB)
  time.sleep(0.5)
  data = GetHallSumAndDifference(aUSB)
  xz = FindXZ(data, hallMatrix)
  e = V2Length(xz, (x, z))
  errorVector.append(e)
  errorFile.write(str(e))
  if e > 0.1:
   print(x, " ", z, " error: ", e)
  if x < xMax:
   errorFile.write(",")
 errorFile.write("\n")
 errorMatrix.append(errorVector)




