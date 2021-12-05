#import sys, fileinput
import sys, fileinput
  
#get input file
inputfile = sys.argv[1]

# Using fileinput.input() method
from collections import deque

stack = deque(maxlen=3)
ans = 0
prev = -1
curr = -1
for line in fileinput.input(files = inputfile ):
    stack.append(int(line))

    if( len(stack) == 3):
        if( prev >= 0 ):
            prev = curr
            curr = stack[0] + stack[1] + stack[2]
        else:
            prev = stack[0] + stack[1] + stack[2]
            curr = stack[0] + stack[1] + stack[2]

        if( curr > prev ):
            ans = ans + 1

print(ans)