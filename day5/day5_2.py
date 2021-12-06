#import sys, fileinput
import sys, fileinput, numpy as np
  
#get input file
inputfile = sys.argv[1]

maxList = []
input = []

for line in fileinput.input(files = inputfile ):
    sarr = line.split("->")
    left = list(map(int,sarr[0].strip().split(",")))
    right = list(map(int,sarr[1].strip().split(",")))
    
    maxList.append(left[0])
    maxList.append(left[1])
    maxList.append(right[0])
    maxList.append(right[1])

    input.append([left,right])
    
max = np.max(maxList) + 1

matrix = np.zeros((max,max),int)

for coords in input:
    #print(coords)
    start = coords[0]
    end = coords[1]

    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    
    #only consider horizontal and vertical lines
    if( x1 == x2 ):
        #len = abs(y1 - y2)+1
        #print(len)
        for y in range(y1,y2+1):
            #print(x1, y)
            matrix[y][x1] = matrix[y][x1] + 1
        for y in range(y2,y1+1):
            #print(x1, y)
            matrix[y][x1] = matrix[y][x1] + 1
    elif( y1 == y2 ):
        for x in range(x1,x2+1):
            #print(x,y1)
            matrix[y1][x] = matrix[y1][x] + 1
        for x in range(x2,x1+1):
            #print(x,y1)
            matrix[y1][x] = matrix[y1][x] + 1
    else:
        print("diagonal!")
        print(coords)
        if(x2 > x1 and y2 > y1): # +1 +1 ###GOOD###
            print("+1 +1")
            y = y1
            for x in range(x1,x2+1):
                print(x, y)
                matrix[y][x] = matrix[y][x] + 1
                y = y + 1
        if( x2 > x1 and y2 < y1): # +1 -1 ###BAD###
            print("+1 -1")
            y = y1
            for x in range(x2,x1+1):
                print(x, y)
                matrix[y][x] = matrix[y][x] + 1
                y = y - 1
        
        if(x2 < x1 and y2 > y1): # -1 +1 ###GOOD###
            print("-1 +1")
            x = x1
            for y in range(y1,y2+1):
                print(x, y)
                matrix[y][x] = matrix[y][x] + 1
                x = x - 1

        if(x2 < x1 and y2 < y1): # -1 -1 ####BAD####
            print("-1 -1")
            x = x1
            for y in range(y2,y1+1):
                print(x, y)
                matrix[y][x] = matrix[y][x] + 1
                x = x - 1
        
    
#get overlap(s)
overlap = 0
for x in range(0,max):
    for y in range(0,max):
        if( matrix[y][x] >= 2 ):
            overlap = overlap + 1
#print(input)
print(matrix)
print("overlap: ", overlap)