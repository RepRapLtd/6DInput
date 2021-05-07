# Utility to convert CSV files to input files for GNU Plot

import csv

fileRoot = '../../Experiments/HallCalibration/'
gnuFile = open(fileRoot + 'xzErrors.gnu', 'w')

with open(fileRoot + 'xzErrors.csv',  newline='\n') as csvfile:
 m = csv.reader(csvfile, delimiter=',')
 for row in m:
  for v in row:
   gnuFile.write(str(v))
   gnuFile.write("\n")
  gnuFile.write("\n")


'''
m0 = []

with open(fileRoot + 'hall-calibration0.csv',  newline='\n') as csvfile:
 m = csv.reader(csvfile, delimiter=',')
 for row in m:
  m00 = []
  for v in row:
   m00.append(int(v))
  m0.append(m00)

m1 = []

with open(fileRoot + 'hall-calibration1.csv',  newline='\n') as csvfile:
 m = csv.reader(csvfile, delimiter=',')
 for row in m:
  m11 = []
  for v in row:
   m11.append(int(v))
  m1.append(m11)

sum = []
diff = []
for z in range(len(m0)):
 row0 = m0[z]
 row1 = m1[z]
 sum0 = []
 diff0 = []
 for x in range(len(row0)):
  sum0.append(row0[x] + row1[x])
  diff0.append(row0[x] - row1[x])
 sum.append(sum0)
 diff.append(diff0)

gnuFile = open(fileRoot + 'sum', 'w')
for row in sum:
 for v in row:
  gnuFile.write(str(v))
  gnuFile.write("\n")
 gnuFile.write("\n")
gnuFile.close()

gnuFile = open(fileRoot + 'diff', 'w')
for row in diff:
 for v in row:
  gnuFile.write(str(v))
  gnuFile.write("\n")
 gnuFile.write("\n")
gnuFile.close()
'''
