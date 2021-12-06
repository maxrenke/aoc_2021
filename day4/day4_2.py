#import sys, fileinput
import sys, fileinput, numpy as np
  
#get input file
inputfile = sys.argv[1]

f = open(inputfile,"r")

#get bingo draw lines
draw = f.readline()
draw = list(map(int,draw.split(",")))

#read in boards
boards = [[]]
winnerboards = []
winner = [[]]
winnum = 0
winners = 0
lines = f.readlines()

i = 0
j = 0
for line in lines:
    if(len(line) == 0 ):
        exit()

    line = line.replace("\n","")
    line = line.replace("  ", " ")
    
    if(len(line) > 0 ):  
        strlist = line.strip().split(" ")
        boards[i].append(list(map(int,strlist)))
        
        j = j + 1
        if( j == 5 ):   
            i = i + 1
            boards.append([])
            j = 0

total_boards = len(boards) - 1
print("total_boards", total_boards)

for num in draw:
    print("draw: ", num)

    for board in boards:
        if(not board):
            break
        
        #draw number
        x = 0
        y = 0
        for row in board:
            for val in row:
                if( val == num):
                    board[x][y] = -1
                y = y + 1
            x = x + 1
            y = 0
        

    #check winner
    
    #rows
    for board in boards:
        if(not board):
            break
        
        #print(board)
        #np.rot90(board)

        for row in board:
            if( sum(row) == (-1 * len(row))):
                winner = board
                winnerboards.append(board)

        rotboard = np.rot90(board)
        for row in rotboard:
            if( sum(row) == (-1 * len(row))):
                winner = board
                winnerboards.append(board)

    if(len(winner) > 1):
        print("winner!")
        winnum = num
        winners = winners + 1
        print("winners: ", winners)

        if( winners == total_boards):
            print("winning board: ", winner)
            print("winners",winners)
            print(len(board))
            if(len(board) > 0 ):
                winner = board
                winnerboards.append(board)
            break

        boards.remove(winner)
        winner = [[]]
    

#print(boards)

#print("winner:")
#print(winner)

print("----")
print(boards)
print("----")
print(winnerboards)

x = 0
y = 0
for row in winner:
    for val in row:
        if( val == -1):
            winner[x][y] = 0
        y = y + 1
    x = x + 1
    y = 0

print("---")
print(winnerboards.pop())
print("winnum,", winnum)
print("sum,", np.matrix(winner).sum())
print(winnum * np.matrix(winner).sum())