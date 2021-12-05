#import sys, fileinput
import sys, fileinput
  
#get input file
inputfile = sys.argv[1]

# Using fileinput.input() method
ans = 0
prev = -1
curr = -1
for line in fileinput.input(files = inputfile ):
    if( prev >= 0 ):
        prev = curr
        curr = int(line)
    else:
        prev = int(line)
        curr = int(line)

    if( curr > prev ):
        ans = ans + 1

print(ans)