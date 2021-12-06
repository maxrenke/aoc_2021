#import sys, fileinput
import sys, fileinput, numpy as np
  
#get input file
inputfile = sys.argv[1]

matrix = []

for line in fileinput.input(files = inputfile ):
    strlist = list(line.strip())
    matrix.append(list(map(int,strlist)))

mSum = np.sum(matrix, axis=0)

gamma = []
for i in mSum:
    if( len(matrix) - i <= i):
        gamma.append(1)
    else:
        gamma.append(0)

print('gamma: ' + str(int('0b' + ''.join(map(str,gamma)),2)))


epsilon = []
for i in mSum:
    if( len(matrix) - i > i):
        epsilon.append(1)
    else:
        epsilon.append(0)

print('epsilon: ' + str(int('0b' + ''.join(map(str,epsilon)),2)))

print('power consumption: ' + str( int('0b' + ''.join(map(str,gamma)),2) * int('0b' + ''.join(map(str,epsilon)),2) ))