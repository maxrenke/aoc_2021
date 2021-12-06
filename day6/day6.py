#import sys, fileinput
import sys, fileinput, numpy as np
  
#get input file
inputfile = sys.argv[1]

#second argument is number of days to run simulation
input = sys.argv[2]


for line in fileinput.input(files = inputfile ):
    state = list(map(int,line.split(",")))

print("Initial State: " , state)

day = 0
for days in range(0,int(input)):
    print("Running day " , day+1)
    statelen = len(state)
    for fish in range(0,statelen):
        if( state[fish] == 0 ):
            state[fish] = 6
            state.append(8)
        else:
            state[fish] = state[fish] - 1
            
    #print("After " , day+1 , " days: " , state)
    day = day + 1

#print("After " , day+1 , " days: " , state)
print("total fish: ", len(state))