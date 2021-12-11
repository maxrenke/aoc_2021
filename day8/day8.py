#import sys, fileinput
import sys, fileinput, numpy as np
  
#get input file
inputfile = sys.argv[1]

digits  = [ 1 , 4 , 7 , 8 ]
seg_len = [ 2 , 4,  3,  7 ]

count = 0

for line in fileinput.input(files = inputfile ):
    pattern = (line.split("|")[0]).strip()
    output =  (line.split("|")[1]).strip()

    for val in output.split(" "):
        for i in seg_len:
            if(len(val) == i ):
                count = count + 1

print(count)
