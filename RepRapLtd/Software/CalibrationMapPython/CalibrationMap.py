# Python code to create a calibration map from two Hall sensors and a magnet

import serial
import time

port = '/dev/ttyUSB0'

def GetArduinoVoltages(usb):
 usb.write(str.encode('v\n'))
 data = usb.readline()
 return data

def OpenArduinoUSB(port):
 usb = serial.Serial(port,115200,timeout=0.1)
 time.sleep(3) # Why so long???
 return usb


usb = OpenArduinoUSB(port)
for i in range(10):
 print(GetArduinoVoltages(usb))
 time.sleep(1)

