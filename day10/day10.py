#import sys, fileinput
import sys, fileinput, numpy as np
from collections import deque
  
#get input file
inputfile = sys.argv[1]

def check_syntax(line):

    expected = deque()

    for ch in line:
        if( ch == '(' ):
            expected.append(')')
        if( ch == '[' ):
            expected.append(']')
        if( ch == '{' ):
            expected.append('}')
        if( ch == '<' ):
            expected.append('>')
        if( ch == ')' or ch == ']' or ch == '}' or ch == '>' ):
            expected_close = expected.pop()
            if( ch != expected_close ):
                print("invalid synatx. expected: " , expected_close , " recieved: ", ch)
                return ch

    return

### --- ###

if( len(sys.argv) > 2 ):
    check_syntax(sys.argv[2])

score = 0

incomplete = []

for line in fileinput.input(files = inputfile ):
    illegal = check_syntax(line)
    if( illegal ):
        if( illegal == ')'):
            score += 3
        if( illegal == ']'):
            score += 57
        if( illegal == '}'):
            score += 1197
        if( illegal == '>'):
            score += 25137
    else:
        incomplete.append(line)

print("corrupted score: ", score)


scores = []

for line in incomplete:
    score = 0
    open = deque()
    for ch in line:
        if( ch == '(' ):
            open.append(ch)
        if( ch == '[' ):
            open.append(ch)
        if( ch == '{' ):
            open.append(ch)
        if( ch == '<' ):
            open.append(ch)
        if( ch == ')' ):
            open.pop()
        if( ch == ']' ):
            open.pop()
        if( ch == '}' ):
            open.pop()
        if( ch == '>' ):
            open.pop()
    
    #print("open: " , open)
    
    close = []

    while len(open) > 0:
        open_to_close = open.pop()
        if( open_to_close == '(' ):
            close.append(")")
        if( open_to_close == '[' ):
            close.append("]")
        if( open_to_close == '{' ):
            close.append("}")
        if( open_to_close == '<' ):
            close.append(">")

    for ch in close:
        score = score * 5
        if( ch == ')' ):
            score += 1
        if( ch == ']' ):
            score += 2
        if( ch == '}' ):
            score += 3
        if( ch == '>' ):
            score += 4

    print(''.join(close) , " : ", score)
    scores.append(score)

middle_index = len(scores)/2
print("middle: ", sorted(scores)[int(middle_index)])


        
