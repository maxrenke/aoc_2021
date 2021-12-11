#import sys, fileinput
import sys, fileinput, numpy as np
  
#get input file
inputfile = sys.argv[1]

matrix = []
width = 0
height = 0

for line in fileinput.input(files = inputfile ):
    row = []
    for c in line.strip():
        row.append(int(c))
    width = len(row)
    matrix.append(row)
    height = height + 1

m = np.matrix(matrix)
print(m)

risk = 0

for y in range(height):
    for x in range(width):
        #if corner, low = 2
        #if edge, low = 3
        #else low = 4
        
        if( x == 0 and y == height - 1 ):
            low = 2
            #print(matrix[y][x])

        elif( x == 0 and y == 0 ):
            low = 2
            #print(matrix[y][x])

        elif( x == width -1 and y == height - 1 ):
            low = 2
            #print(matrix[y][x])

        elif( x == width -1 and y == 0 ):
            low = 2
            #print(matrix[y][x])

        elif( x == 0 or y == 0 or x == width -1 or y == height -1 ):
            low = 3
            #print(matrix[y][x])

        else:
            low = 4
            #print(matrix[y][x])

        #up
        if( y-1 >= 0 and matrix[y][x] < matrix[y-1][x] ):
            low = low - 1

        #down
        if( y+1 < height and matrix[y][x] < matrix[y+1][x] ):
            low = low - 1
      

        #left
        if( x-1 >= 0 and matrix[y][x] < matrix[y][x-1] ):
            low = low - 1


        #right
        if( x+1 < width and matrix[y][x] < matrix[y][x+1] ):
            low = low - 1

        if( low == 0 ):
            print("low spot at " , matrix[y][x])
            risk = risk + (matrix[y][x] + 1)

        #print(x , " " , y , " :" , matrix[y][x])

print("sum of risk: ", risk)