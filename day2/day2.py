#import sys, fileinput
import sys, fileinput
  
#get input file
inputfile = sys.argv[1]

x=0
y=0
for line in fileinput.input(files = inputfile ):
    input_arr = line.split()
    val = int(input_arr[1])
    if( input_arr[0] == 'forward'):
        #print('forward', input_arr[1])
        x = x + val
    if( input_arr[0] == 'down'):
        #print('down', input_arr[1])
        y = y - val
    if( input_arr[0] == 'up'):
        #print('up', input_arr[1])
        y = y + val

#print(x)
#print(y)
print(abs(x*y))