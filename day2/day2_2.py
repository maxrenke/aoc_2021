#import sys, fileinput
import sys, fileinput
  
#get input file
inputfile = sys.argv[1]

x=0
y=0
aim=0
for line in fileinput.input(files = inputfile ):
    input_arr = line.split()
    val = int(input_arr[1])
    if( input_arr[0] == 'forward'):
        #print('forward', input_arr[1])
        y = y + (aim * val)
        x = x + val
    if( input_arr[0] == 'down'):
        #print('down', input_arr[1])
        #y = y - val
        aim = aim + val
    if( input_arr[0] == 'up'):
        #print('up', input_arr[1])
        #y = y + val
        aim = aim - val

    #print("x: " + str(x))
    #print("y: " + str(y))
    #print("aim: " + str(aim))

#print(x)
#print(y)
print(abs(x*y))