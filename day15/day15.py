#import sys, fileinput
import sys, fileinput, numpy as np, heapq
  
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

print(m , "\n")

class Vertex:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c

    def __eq__(self,other):
        #return self.c == other.c
        return self.x == other.x and self.y == other.y
    
    def __lt__(self,other):
        return self.c < other.c

    def __gt__(self,other):
        return self.c > other.c

    def __hash__(self):
        #return int(str(hash(self.x))+str(hash(self.y))+str(hash(self.c)))
        #return int(str(hash(self.x))+str(hash(self.y)))
        return hash((self.x,self.y))
        

    def __str__(self):
        return str(self.c)

costs = {}
visited = set()
queue = [Vertex(0,0,0)]
costs[(0,0)] = 0
heapq.heapify(queue)

def get(r, c):
    x = (matrix[r % width][c % height] +
         (r // width) + (c // height))
    return (x - 1) % 9 + 1

for y in range(height):
    for x in range(width):
        costs[(x,y)] = matrix[y][x]


#print(costs)
#print(costs[(0,0)])
#print(costs[(width-1,height-1)])

while len(queue) > 0:
    vertex = heapq.heappop(queue)
    print( vertex.x, vertex.y, vertex.c)

    if vertex in visited:
        continue
    visited.add(vertex)

    if vertex.x == width - 1 and vertex.y == height - 1:
        break

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        rr = vertex.x + dr
        cc = vertex.y + dc
        if not (0 <= rr < width and 0 <= cc < height):
            continue

        #heapq.heappush(queue, Vertex(rr, cc, vertex.c + matrix[rr][cc]))
        heapq.heappush(queue, Vertex(rr, cc, vertex.c + get(rr,cc)))
    
#print(costs[(width - 1, height - 1)])
#print(costs)
print(vertex)