#import sys, fileinput
import sys, fileinput, copy
  
#get input file
inputfile = sys.argv[1]

input_flag = 0
template = ''
polymer = ''
rules = []
rules_dict = {}
insert = []
freq = {}

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

for e in range(len(template)-1):
    left = template[e]
    right = template[e+1]
    pair = left+right
    freq[pair] = freq.get(pair,0) + 1

print(freq)

for i in range(1,step+1):
    
    print("After step " , i , ":")
    new_freqs = copy.copy(freq)
    for pair in freq:
        m = rules_dict.get(pair)
        if( m ):
            occs = freq[pair]
            if( new_freqs[pair] > 0 ):
                new_freqs[pair] = new_freqs.get(pair,0) - occs
            new_left_pair = pair[0] + m
            new_right_pair = m + pair[1]
            new_freqs[new_left_pair] = new_freqs.get(new_left_pair,0) + occs
            new_freqs[new_right_pair] = new_freqs.get(new_right_pair,0) + occs
    freq = new_freqs
    print("freq: ", freq)

    #count
    count = {}
    for pair in new_freqs:
        left = pair[0]
        right = pair[1]

        count[left] = count.get(left,0) + new_freqs[pair]
        count[right] = count.get(right,0) + new_freqs[pair]

    count[template[0]] = count.get(template[0],0) + 1
    count[template[-1]] = count.get(template[-1],0) + 1

    len = 0
    for c in count:
        count[c] = count.get(c,0) // 2
        len += count[c]
    print("count: " , count)
    print("len: ", len)
    
    sorted_count = sorted(count,key = lambda item:count.get(item))
    print(count.get(sorted_count[-1]) - count.get(sorted_count[0]))

#counted = count(polymer)
#sorted_counted = sorted(counted,key = lambda item:counted.get(item))
#print(counted.get(sorted_counted[-1]) - counted.get(sorted_counted[0]))

