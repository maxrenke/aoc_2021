#import sys, fileinput
import sys, fileinput, numpy as np
  
#get input file
inputfile = sys.argv[1]

#second argument is number of days to run simulation
input = sys.argv[2]


for line in fileinput.input(files = inputfile ):
    inputstate = list(map(int,line.split(",")))

print("Initial State: " , inputstate)
#set initial state
count = np.zeros(9, np.float64)
for i in inputstate:
    count[i] = count[i] + 1
#print(count)
#run simulation for 'input' number of days
day = 0
prev = count
for days in range(0,int(input)):
    #print("Running day " , day+1)
    zeros = prev[0]    
    for i in range(0,len(count)):
        if( i != 0 ):
            count[i-1] = count[i]
    
    count[6] = count[6] + zeros
    count[8] = zeros

    #print(count)
 
    print("day " , day+1 , " = " , count.sum())
    day = day + 1

print("After " , day+1 , " days: " , count)

print("total fish: ", count.sum())