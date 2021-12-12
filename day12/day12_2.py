#import sys, fileinput
import sys, fileinput, numpy as np
from collections import defaultdict, Counter
  
#get input file
inputfile = sys.argv[1]

paths = []
nodes = []
path_nodes = []
path_dict = {}

class path_node:
    neighbors = []
    size = 0 # 0=small , 1=big
    name = ''
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        if( str(name).islower() ):
            self.size = 0 #small
        else:
            self.size = 1 #big

    def __str__(self):
        return self.name
    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)
    def getNeighbors(self):
        return self.neighbors

# Using fileinput.input() method
for line in fileinput.input(files = inputfile ):
    path = line.strip().split("-")
    nodes = list(set( nodes + [path[0]]))
    nodes = list(set( nodes + [path[1]]))

    paths.append(path)

#print("nodes: " , nodes)

#create path_nodes
for node in nodes:
    n = path_node(node)
    path_nodes.append(n)
    path_dict[n.name] = n

#print("paths: ", paths)
#print("path_nodes: ", path_nodes)
#print("dict: " , path_dict)

#add neighbors
for p in paths:

    l = p[0]
    r = p[1]

    print("p: ", p , " l: ", p[0] , " r: ", p[1])

    if( r == 'start'):
        l = p[1]
        r = p[0]
    if( l == 'end'):
        l = p[1]
        r = p[0]

    if( r != 'start' ):
        path_dict.get(l).addNeighbor(r)
    if( l != 'start' and l != 'end'):
        if( r != 'start' and r != 'end'):
            path_dict.get(r).addNeighbor(l)

    #path_dict.get(l).addNeighbor(r)
    #path_dict.get(r).addNeighbor(l)

for n in path_nodes:
    print(n.name , " : " , n.getNeighbors())

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  
  #visited.append(node)
  if( node.size == 0 ):
    visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0)
    print (m, end = " ")

    for neighbour in m.getNeighbors():
      if neighbour not in visited:
        #visited.append(neighbour)
        if( path_dict.get(neighbour).size == 0 ):
            visited.append(neighbour)
        #queue.append(neighbour)
        queue.append(graph.get(neighbour))        
        #bfs(visited.copy(),graph,path_dict.get(neighbour))
  
  #for v in visited:
  #    print( v, end = " ")
  #print("")
        

#bfs(visited, path_dict, path_dict.get('start'))
print("\n")

#visited = set() # Set to keep track of visited nodes of graph.

#def dfs(visited, graph, node):  #function for dfs 
#    if node not in visited:
#        #print (node)
#        #visited.add(node)
#        #if( node.size == 0 ):
#        #    visited.add(node)
#        print(node.size)
#        visited.add(node)
#        
#        #for neighbour in graph[node]:
#        for neighbour in node.getNeighbors():
#            dfs(visited, graph, path_dict.get(neighbour))
#
#dfs(visited, path_dict, path_dict.get('start'))
#
#for v in visited:
#  print( v, end = " ")
#  print("")

visitedList = [[]]

def depthFirst(graph, node, visited):
    visited.append(node.name)
    
    for vertex in node.getNeighbors():
        #print("if ", vertex , " not in ", visited)
        filtered = filter (lambda v: v[0].islower() , visited)        
        new_list = list(filtered)
        #print("if ", vertex , " not in ", list(filtered))
        #if vertex not in visited:
        #print(vertex, " : ", visited.count(vertex), " : " , visited)
        #if vertex not in list(filtered):
        dupe = 0
        for item in new_list:
            #print(item, " : ", filtered_list.count(item))
            if( new_list.count(item) > 1 ):
                dupe = dupe + 1

        #print("dupe: " , dupe )
        if( dupe < 4 ):
            if new_list.count(vertex) < 2 :
                depthFirst(graph, path_dict.get(vertex), visited.copy())

    visitedList.append(visited)
    

depthFirst(path_dict, path_dict.get('start'), [])

print(len(visitedList))

final_count = 0

visitedListSet = []
for final_path in visitedList:
    if( 'end' in final_path):
        if( final_path[-1] == 'end' ):
            #print(final_path)
            filtered = filter (lambda v: v[0].islower() , final_path)

            dupe = 0
            filtered_list = list(filtered)
            #print("filtered_list :", filtered_list)
            for item in filtered_list:
                #print(item, " : ", filtered_list.count(item))
                if( filtered_list.count(item) > 1 ):
                    dupe = dupe + 1

            #print("dupe: " , dupe , "\n\n")
            if( dupe < 4 ):
                final_count = final_count + 1

#print(visitedListSet)

print("")

print("total paths: ", final_count)
