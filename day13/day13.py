#import sys, fileinput
import sys, fileinput
  
#get input file
inputfile = sys.argv[1]

points = set()
lines = []

def grid(points):
    max_x = sorted(points,key = lambda item:item[0],reverse=True)[0][0]
    max_y = sorted(points,key = lambda item:item[1],reverse=True)[0][1]
    for y in range(0,max_y+1):
        for x in range(0,max_x+1):
            if( (x,y) in points ):
                print(" # ", end = "")
            else:
                print(" . ", end = "")
        print("")

def move(fold,p):
    axis = fold[0]
    line = int(fold[1])
    x = p[0]
    y = p[1]
    
    #print(axis, " move ", p )

    if( axis == 'x' ):
        from_axis = x - line
        points.add( ( line - from_axis , y))
    if( axis == 'y' ):
        from_axis = y - line
        points.add( ( x,  line - from_axis ))
        

    points.remove(p)

input_flag = 0
# Using fileinput.input() method
for line in fileinput.input(files = inputfile ):
    if(line == "\n"):
        input_flag = 1
    
    elif( input_flag == 0 ): #points
        split_line = line.strip().split(",")
        points.add((int(split_line[0]),int(split_line[1])))
    
    elif( input_flag == 1 ): #folds
        split_line = line.strip().split(" ")
        line_input = split_line[2] #last element in line
        line_input_split = line_input.split("=")
        lines.append((line_input_split[0],int(line_input_split[1])))

#print("points: ", points)
#print("lines: ", lines)

grid(points)

for fold in lines:
    print("fold on :" , fold)

    if(fold[0] == 'x'): #vertical fold
        for p in points.copy():
            if( p[0] > fold[1] ):
                move(fold,p)
    if(fold[0] == 'y'): #horizontal fold
        for p in points.copy():
            if( p[1] > fold[1] ):
                move(fold,p)

    print("overlapping points: " , len(points))
    grid(points)
    #break #only do first fold