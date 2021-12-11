#import sys, fileinput
import sys, fileinput, numpy as np
  
#get input file
inputfile = sys.argv[1]

width = 0
height = 0
matrix = []
flashes = 0

# Using fileinput.input() method
for line in fileinput.input(files = inputfile ):
    row = []
    for c in line.strip():
        row.append(int(c))
    width = len(row)
    matrix.append(row)
    height = height + 1

m = np.matrix(matrix)

ones = np.zeros([width,height], int)
for x in range(width):
    for y in range(height):
        ones[y][x] = 1


steps = int(sys.argv[2])

print("Before any steps:")

print(m , "\n")

def readyToFlash():
    readyToFlashList = []
    for x in range(width):
        for y in range(height):
            if( m.item(x,y) > 9 ):
                readyToFlashList.append((x,y))

    return readyToFlashList

def flash(octopus, flashed):
    if( octopus in flashed ):
        return
    
    x = octopus[1]
    y = octopus[0]
    #print("flash " , x , y )

    # -1 , -1
    if( x-1 > -1 and y-1 > -1 ):
        m.itemset((y-1,x-1),m.item(y-1,x-1)+1)
        #m[y-1][x-1] = m[y-1][x-1] +1

    #  0 , -1
    if( x > -1 and y-1 > -1 ):
        m.itemset((y-1,x),m.item(y-1,x)+1)
        #m[y-1][x] = m[y-1][x] +1

    #  1 , -1
    if( x+1 < width and y-1 > -1 ):
        m.itemset((y-1,x+1),m.item(y-1,x+1)+1)
        #m[y-1][x+1] = m[y-1][x+1] +1

    # -1 , 0
    if( x-1 > -1 and y > -1 ):
        m.itemset((y,x-1),m.item(y,x-1)+1)
        #m[y][x-1] = m[y][x-1] +1

    # -1 , 1
    if( x-1 > -1 and y+1 < height ):
        m.itemset((y+1,x-1),m.item(y+1,x-1)+1)
        #m[y+1][x-1] = m[y+1][x-1] +1

    #  1 , 0
    if( x+1 < width and y > -1 ):
        m.itemset((y,x+1),m.item(y,x+1)+1)
        #m[y][x+1] = m[y][x+1] +1

    #  1, 1
    if( x+1 < width and y+1 < height ):
        m.itemset((y+1,x+1),m.item(y+1,x+1)+1)
        #m[y+1][x+1] = m[y+1][x+1] +1

    #  0 , 1
    if( x > -1 and y+1 < height ):
        m.itemset((y+1,x),m.item(y+1,x)+1)
        #m[y+1][x] = m[y+1][x] +1

for s in range(1,steps+1):
    #First, increase energy level of each octopus by 1
    m = np.add(m,ones)
    
    #Then, flash anything greater than 9 (repeat)

    flashed = []
    
    while (len(readyToFlash()) > len(flashed) ):
        for octopus in readyToFlash():
            flash(octopus, flashed)
            flashed = list(set( flashed + [octopus]))

    #Finally, all octopus that flashed set to 0
    for octopus in flashed:
        m.itemset(octopus,0)
        #increment flashes
        flashes = flashes + 1

    print("After step ", s , "\n" , m, "\n")

    print("total number of flashes: " , flashes)

    if( len(flashed) == (width * height)):
        print("All octopus flashed simultaneously! ")
        break

    
    