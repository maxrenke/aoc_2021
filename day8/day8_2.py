#import sys, fileinput
import sys, fileinput, numpy as np, functools, difflib
  
#get input file
inputfile = sys.argv[1]

digits  = [ 1 , 4 , 7 , 8 ]
seg_len = [ 2 , 4,  3,  7 ]

sum  = 0

for line in fileinput.input(files = inputfile ):
    solution = [ [] for _ in range(10) ]

    pattern = (line.split("|")[0]).strip()
    output =  (line.split("|")[1]).strip()

    #1 , 4 , 7 , 8
    for val in pattern.split(" "):
        sorted_val = ''.join(sorted(val))
        
        if( len(sorted_val) in seg_len): # 1 , 4, 7 , 8
            for i in range(len(seg_len)):
                if( len(sorted_val) == seg_len[i]):
                    solution[digits[i]] = sorted_val
    #3
    for val in pattern.split(" "):
        sorted_val = ''.join(sorted(val))

        if (len(sorted_val) == 5 ): # 2, 3, 5
            if( set(solution[1]).issubset(set(sorted_val)) ):
                solution[3] = sorted_val

    #9
    for val in pattern.split(" "):
        sorted_val = ''.join(sorted(val))

        if (len(sorted_val) == 6 ): #0, 6, 9
            if( set(solution[4]).issubset(set(sorted_val)) ):
                solution[9] = sorted_val

    #2, 5
    for val in pattern.split(" "):
        sorted_val = ''.join(sorted(val))

        if (len(sorted_val) == 5 and sorted_val != solution[3]): # 2, 3, 5
            diff_len = len(list(difflib.ndiff(sorted_val,solution[9])))
            if( diff_len == 6 ):
                solution[5] = sorted_val
            if( diff_len == 7 ):
                solution[2] = sorted_val

    #0
    for val in pattern.split(" "):
        sorted_val = ''.join(sorted(val))

        if (len(sorted_val) == 6 ):
            diff_len = len(list(difflib.ndiff(sorted_val,solution[5])))
            if( diff_len == 7 ):
                solution[0] = sorted_val
                
    #6
    for val in pattern.split(" "):
        sorted_val = ''.join(sorted(val))

        if (len(sorted_val) == 6 and sorted_val != solution[9] and sorted_val != solution[0]):
             diff_len = len(list(difflib.ndiff(sorted_val,solution[8])))
             if( diff_len == 7 ):
                 solution[6] = sorted_val
                
    

    #got solution    
    #print(solution)

    output_str = ""
    for output_val in output.split(" "):
        sorted_output_val = ''.join(sorted(output_val))
        #print(output_val)
        #print(sorted_output_val)
        #print(solution.index(sorted_output_val))
        output_str += str(solution.index(sorted_output_val))
    
    #print(output_str)
    #print(int(output_str))

    print(output , ": ", int(output_str))
    sum = sum + int(output_str)

print("sum: ", sum)



