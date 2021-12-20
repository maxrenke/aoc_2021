#import sys, fileinput
import sys, fileinput, numpy as np, heapq

version_sum = 0

def pop(arr,n):
    list = []
    for i in range(n):
        list.append(arr.pop(0))

    return list

def bin_dec(a):
    result = 0
    for bit in a:
        result *= 2
        if bit == '1':
            result +=1
    return result

def readLiteral(bits): #TODO return how many bits were read!
    #print("literal value!")
    len_read = 0
    value_list = []
    next = [1] #start
    while next[0] > 0: #while 1s
        next = pop(bits,5)
        len_read += 5
        for next_i in range(1,5):
            value_list.append(next[next_i])
    
    value = bin_dec(''.join(map(str,value_list)))
    #print(value)
    return len_read

def readOperator(bits):
    #print("operator!")
    len_read = 0
    length_type_id = bin_dec(''.join(map(str,pop(bits,1))))
    len_read += 1
    #print("length type id: ", length_type_id)
    if( length_type_id == 0):
        total_length = bin_dec(''.join(map(str,pop(bits,15))))
        len_read += 15
        #print("total_length: ", total_length)
        len_read = 0
        while len_read <= total_length:
            len_read += readPacket(bits)
            #print("len_read = ", len_read)
    if( length_type_id == 1):
        num_sub_packets = bin_dec(''.join(map(str,pop(bits,11))))
        len_read += 11
        #print("num_sub_packets: ", num_sub_packets)
        for sub_packets in range(num_sub_packets):
            readPacket(bits)

def readPacket(bits):
    global version_sum
    #print("bits: ", bits, len(bits))
    if( len(bits) == 0 ):
        return 0
    if( sum(bits) == 0 ):
        return len(bits)
    len_read = 0
    try:
        #version (3)
        version = bin_dec(''.join(map(str,pop(bits,3))))
        version_sum += version
        print("VERSION: ", version)
        len_read += 3
        
        #type_id (3)
        type_id = bin_dec(''.join(map(str,pop(bits,3))))
        len_read += 3
        #print("type_id: ", type_id)


        if( type_id == 4 ): #literal value
            len_read += readLiteral(bits)

        else:
            len_read += readOperator(bits)
    except Exception:
        return len_read

    return len_read

#get input
for i in range(len(sys.argv)):
    if i == 0:
        continue
    
    input = sys.argv[i].lower()

    res = str(bin(int(input, 16)))[2:].zfill(len(input)*4)

    bits = []
 
    for b in res:
        bits.append(int(b))
    #print(bits)
    
    version_sum = 0
    readPacket(bits)
    print(version_sum)