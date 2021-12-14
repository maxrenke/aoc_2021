#import sys, fileinput
import sys, fileinput
  
#get input file
inputfile = sys.argv[1]

input_flag = 0
template = ''
polymer = ''
rules = []
rules_dict = {}
insert = []

step = int(sys.argv[2])

def match(pair):
    #print(pair)
    #print(rules_dict.get(pair))
    return rules_dict.get(pair)
    #for rule in rules:
    #    if( pair == rule[0] ):
    #        return rule[1]
    #return None

def count(string):
    counted = {}
    for i in string:
        counted[i] = counted.get(i,0) + 1
    return counted

# Using fileinput.input() method
for line in fileinput.input(files = inputfile ):
    if(line == "\n"):
        input_flag = 1
    
    elif( input_flag == 0 ): #template
        template = line.strip()
    
    elif( input_flag == 1 ): #rules
        line_split = line.strip().split(" -> ")
        l = line_split[0]
        r = line_split[1]
        #rules.append((l,r))
        rules_dict[l] = r      

print("Template: " , template)
polymer = template

#for rule in rules:
#    print("rule: " , rule[0] , " -> ", rule[1])

for i in range(1,step+1):
    polymer_build = polymer[0]
    polymer_copy = polymer#polymer.copy()
    for e in range(len(polymer_copy)-1):
        left = polymer_copy[e]
        right = polymer_copy[e+1]

        pair = left + right
        #m = match(pair)
        m = rules_dict.get(pair)
        
        if( m ):
            #print("matched rule , " , left , " -> ", right , " insert ", m, " at ", e+1)
            #insert.append((m,e+1))

            polymer_build += m
            polymer_build += right
            #polymer_build = ''.join((polymer_build,m,right))
            
        else:
            polymer_build += left
            polymer_build += right
            #polymer_build = ''.join((polymer_build,left,right))
    
    #perform insertions
    #iter = 0
    #for j in insert:
    #    elm = j[0]
    #    loc = j[1] + iter
    #    polymer = polymer[:loc] + elm + polymer[loc:] #Character at specific pos
    #    iter = iter + 1

    insert = []
    polymer = polymer_build

    #print("After step ", i, " (", len(polymer) , ") : ", polymer)
    #print("After step ", i, " (", len(polymer) , ")")
    print("After step ", i )
    #print("polymer_build: " , polymer_build)
    #print("polymer      : " , polymer)
    

counted = count(polymer)
sorted_counted = sorted(counted,key = lambda item:counted.get(item))

print(counted.get(sorted_counted[-1]) - counted.get(sorted_counted[0]))
    