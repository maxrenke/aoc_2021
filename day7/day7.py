#import sys, fileinput
import sys, fileinput, numpy as np
  
#get input file
inputfile = sys.argv[1]

for line in fileinput.input(files = inputfile ):
    positions = list(map(int,line.split(",")))

fuel = np.zeros(max(positions),int)

for end in range(min(positions),max(positions)):
    #print("get ", positions , "to end:" , end)

    for x in positions:
        fuel_cost = abs(x - end);
        fuel[end] = fuel[end] + fuel_cost

print(fuel)
#get min cost
print(min(fuel) , " to get to " , np.where(fuel == min(fuel))[0][0])
