#import sys, fileinput
import sys, fileinput, numpy as np
  
#get input file
inputfile = sys.argv[1]

matrix = []
width = 0
height = 0

low_points = []

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
            #print("low spot at " , matrix[y][x])
            low_points.append((x,y))

#print(low_points)

#find adjacent (and low and not 9)
def findAdj(x_val, y_val):
    x = x_val
    y = y_val
    #print("x: ", x , " y: ", y )

    adj = []

    #up
    if( y-1 >= 0 and matrix[y][x] < matrix[y-1][x] and matrix[y-1][x] != 9):
        #print("adj = ", matrix[y-1][x])
        adj.append((x,y-1))

    #down
    if( y+1 < height and matrix[y][x] < matrix[y+1][x] and matrix[y+1][x] != 9):
        #print("adj = ", matrix[y+1][x])
        adj.append((x,y+1))

    #left
    if( x-1 >= 0 and matrix[y][x] < matrix[y][x-1] and matrix[y][x-1] != 9):
        #print("adj = ", matrix[y][x-1])
        adj.append((x-1,y))

    #right
    if( x+1 < width and matrix[y][x] < matrix[y][x+1] and matrix[y][x+1] != 9):
        #print("adj = ", matrix[y][x+1])
        adj.append((x+1,y))

    adj_all = []
    for n in adj:
        n_x = n[0]
        n_y = n[1]
        #print( matrix[n_y][n_x])
        next = findAdj(n_x,n_y)
        #adj_all = list(set(adj + next))
        adj_all = adj_all + next

    #if( adj == [] ):
    #adj_all += [(x,y)]
    adj_all = list(set(adj_all + [(x,y)]))
        #print("adj all: ", adj_all)

    return adj_all


#find basins

basins = []

for lowpoint in low_points:
    x = lowpoint[0]
    y = lowpoint[1]

    print("lowpoint: " , matrix[y][x])
    
    basin = list(set( findAdj(x,y) + [(x,y)]))

    basins.append(basin)

#sort basins from largest to smallest
basins.sort(key=len,reverse=True)

#find 3 largest basins and multiply their sizes
total_size = len(basins[0]) * len(basins[1]) * len(basins[2])

print(total_size)
    