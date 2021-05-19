# Python code to create a 3D calibration map from three Hall sensors in a ring and a magnet
#
# Adrian Bowyer
# RepRap Ltd
# https://reprapld.com
#
# 10 May 2021
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

def MoveRepRap(x, f, port):
 s = "G1 X"
 s += str(x[0])
 s += " Y"
 s += str(x[1])
 s += " Z"
 s += str(x[2])
 s += " F"
 s += str(f)
 s += "\n"
 #print(s)
 port.write(str.encode(s))

def Get3HallReadings(usb):
 usb.write(str.encode('v\n'))
 data = usb.readline()
 data = str(data.decode('ascii'))
 data = re.findall('\d+', data)
 data = (int(data[0]), int(data[1]), int(data[2]))
 return data

def OpenArduinoUSB():
 usb = serial.Serial(arduinoPort,115200,timeout=0.1)
 time.sleep(3) # Why so long???
 return usb

def OpenRepRapUSB():
 usb = serial.Serial(reprapPort,115200,timeout=0.1)
 return usb

def LogReadings(a):
 while True:
  if a is 1:
   print(Get3HallReadings(aUSB)[0])
  else:
   print(Get3HallReadings(aUSB))
  time.sleep(0.5)

def V2Length(a, b):
 xd = a[0] - b[0]
 yd = a[1] - b[1]
 zd = a[2] - b[2]
 return maths.sqrt(xd*xd + yd*yd + zd*zd)

def VAdd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

# Really dumb search function...

def FindXYZ(data, offset, hallTensor):
 xyz = (0, 0, 0)
 closeValue = sys.float_info.max
 for z in range(len(hallTensor)):
  matrix = hallTensor[z]
  for y in range(len(matrix)):
   vector = matrix[y]
   for x in range(len(vector)):
    d = vector[x]
    dist = V2Length(d, data)
    if dist < closeValue:
     closeValue = dist
     xyz = VAdd((x, y, z), offset)
 return xyz

def WriteHallTensor(hallTensor):
 hallTensorFile = open('../../Experiments/HallCalibration/hallTensor.tns', 'w')
 hallTensorFile.write(str(len(hallTensor)))
 hallTensorFile.write(" ")
 hallTensorFile.write(str(len(hallTensor[0])))
 hallTensorFile.write(" ")
 hallTensorFile.write(str(len(hallTensor[0][0])))
 hallTensorFile.write("\n")
 for hallMatrix in hallTensor:
  for hallVector in hallMatrix:
   for hallValues in hallVector:
    for value in hallValues:
     hallTensorFile.write(str(value))
     hallTensorFile.write(" ")
    hallTensorFile.write("\n")



def ReadHallTensor():
 hallTensorFile = open('../../Experiments/HallCalibration/hallTensor.tns', 'r')
 lengths = hallTensorFile.readline()
 lengths = str(lengths.decode('ascii'))
 lengths = re.findall('\d+', lengths)
 hallTensor = []
 for z in range(lengths[0]):
  hallMatrix = []
  for y in range(lengths[1]):
   hallVector = []
   for x in range(lengths[2]):
    data = hallTensorFile.readline()
    data = str(data.decode('ascii'))
    data = re.findall('\d+', data)
    data = (int(data[0]), int(data[1]), int(data[2]))
    hallVector.append(data)
   hallMatrix.append(hallVector)
  hallTensor.append(hallMatrix)
 return hallTensor

centre = (72, 46, 2.75)
aUSB = OpenArduinoUSB()
LogReadings(1)

rUSB = OpenRepRapUSB()
MoveRepRap(centre, 1000, rUSB)

rMax = 7
zMax = 7


offset = (-rMax, -rMax, 0)

scan = True

if scan:
 hallTensor = []
 for z in range(zMax + 1):
  hallMatrix = []
  MoveRepRap(VAdd(centre, (-rMax, -rMax, z)), 1000, rUSB)
  time.sleep(2)
  for y in range(-rMax, rMax+1):
   hallVector = []
   MoveRepRap(VAdd(centre, (-rMax, y, z)), 1000, rUSB)
   time.sleep(2)
   for x in range(-rMax, rMax+1):
    MoveRepRap(VAdd(centre, (x, y, z)), 1000, rUSB)
    time.sleep(0.5)
    r2 = x*x + y*y
    if r2 > rMax*rMax:
     hallVector.append((-1, -1, -1))
    else:
     data = Get3HallReadings(aUSB)
     print(x, " ", y, " ", z, " ", data)
     hallVector.append(data)
   hallMatrix.append(hallVector)
  hallTensor.append(hallMatrix)
 WriteHallTensor(hallTensor)
else:
 hallTensor = ReadHallTensor()


errorFile = open('../../Experiments/HallCalibration/xyzErrors.gnu', 'w')

for z in range(zMax + 1):
 errorFile = open('../../Experiments/HallCalibration/xyz-'+str(z)+'-Errors.gnu', 'w')
 hallMatrix = hallTensor[z]
 MoveRepRap(VAdd(centre, (-rMax, -rMax, z)), 1000, rUSB)
 time.sleep(2)
 for y in range(-rMax, rMax+1):
  hallVector = hallMatrix[y]
  MoveRepRap(VAdd(centre, (-rMax, y, z)), 1000, rUSB)
  time.sleep(2)
  for x in range(-rMax, rMax+1):
   hallValue = hallVector[x]
   MoveRepRap(VAdd(centre, (x, y, z)), 1000, rUSB)
   time.sleep(0.5)
   r2 = x*x + y*y
   if r2 > rMax*rMax:
    error = -1.0
   else:
    data = Get3HallReadings(aUSB)
    xyz = FindXYZ(data, offset, hallTensor)
    error = V2Length(xyz, (x, y, z))
   errorFile.write(str(error))
   errorFile.write("\n")
   if error > 0.1:
    print(x, " ", y, " ", z, " error: ", error)
  errorFile.write("\n")
 errorFile.close()





