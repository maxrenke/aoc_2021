#import sys, fileinput
import sys, fileinput, numpy as np
  
#get input file
inputfile = sys.argv[1]

matrix = []

for line in fileinput.input(files = inputfile ):
    strlist = list(line.strip())
    matrix.append(list(map(int,strlist)))

#oxygen
oxygen = matrix

i = 0
new = []
mcommon = []
while( len(oxygen) > 1 ):
    mSum = np.sum(oxygen, axis=0)

    for k in mSum:
        if( len(oxygen) - k <= k):
            mcommon.append(1)
        else:
            mcommon.append(0)

    for j in range(0,len(oxygen)):
        if( oxygen[j][i] == mcommon[i]):
            new.append(oxygen[j])

    oxygen = new
    new = []
    mcommon = []

    i = i + 1

oxygen_int = int('0b' + ''.join(map(str,oxygen[0])),2)
print('oxygen: ' + str(oxygen_int))

#carbon
carbon = matrix

i = 0
new = []
lcommon = []
while( len(carbon) > 1 ):
    mSum = np.sum(carbon, axis=0)

    for k in mSum:
        if( len(carbon) - k > k):
            lcommon.append(1)
        else:
            lcommon.append(0)

    for j in range(0,len(carbon)):
        if( carbon[j][i] == lcommon[i]):
            new.append(carbon[j])

    carbon = new
    new = []
    lcommon = []

    i = i + 1

carbon_int = int('0b' + ''.join(map(str,carbon[0])),2)
print('carbon: ' + str(carbon_int))

print('life support rating: ' , (oxygen_int * carbon_int))