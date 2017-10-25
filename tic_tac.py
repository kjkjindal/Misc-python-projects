    #   |  |
    # __|__|__
    #   |  |
    # __|__|__  
    #   |  |
    #   |  |
#just prints the tic tac toe  board now

#converts a list of moves to a dictionary (tic tac toe board)
def list_to_dict(l, default):
    d = {}
    for i in l:
        d.setdefault(i, default)
    
    return d

#prints a tic tac toe board with given moves       
def printBoard(board, l):
    print (board[l[0]] + '|' + board[l[1]] + '|' + board[l[2]])
    print ("")
    print (board[l[3]] + '|' + board[l[4]] + '|' + board[l[5]])
    print ("")
    print (board[l[6]] + '|' + board[l[7]] + '|' + board[l[8]])

#check if game is won
def checkGame(board, l):
    #horizontals
    if(board[l[0]] == board[l[1]] == board[l[2]]):
        return board[l[0]]
    
    elif(board[l[3]] == board[l[4]] == board[l[5]]):
        return board[l[3]]
        
    elif(board[l[6]] == board[l[7]] == board[l[8]]):
        return board[l[6]]
    
    #verticals
    elif(board[l[0]] == board[l[3]] == board[l[6]]):
        return board[l[0]]
    
    elif(board[l[1]] == board[l[4]] == board[l[7]]):
        return board[l[1]]
        
    elif(board[l[2]] == board[l[5]] == board[l[8]]):
        return board[l[2]]
        
    #diagonals
    elif(board[l[0]] == board[l[4]] == board[l[8]]):
        return board[l[0]]
        
    elif(board[l[2]] == board[l[4]] == board[l[6]]):
        return board[l[2]]  
        
    return (' ')

#checks if board is full. Returns true if board is full.
def isBoardFull(board):
    c = 0
    for i in board.values():
        if (i == ' '):
            c+=1
            
    return not c

#setup tic tac toe board
moves = ['topL', 'topM', 'topR', 'midL', 'midM', 'midR', 'lowL', 'lowM', 'lowR']
board = list_to_dict(moves, ' ')
printBoard(board, moves)
exit_code = 0

#print instructions
print ('Available spaces:')
for i in moves:
    print (i + ', '),
print ("")

#play
while (True):
    #turn for X
    print ('Turn for X, move to which space? (blank to exit)')
    move = raw_input()
    if (move == ''):
        break
    
    board[move] = 'X'
    printBoard(board, moves)
    
    #check game
    a = checkGame(board, moves)
    if (a!= ' '):
        print ('Winner:' +a)
        break
    if (isBoardFull(board)):
        exit_code = 1
        break
    
    #turn for O
    print ('Turn for O, move to which space? (blank to exit)')
    move = raw_input()
    if (move == ''):
        break
    
    board[move] = 'O'
    printBoard(board, moves)
    
    #check game
    a = checkGame(board, moves)
    if (a!= ' '):
        print ('Winner:' +a)
        break
    if (isBoardFull(board)):
        exit_code = 1
        break
    
if (exit_code ==1):
    print("Sorry board is full!!")