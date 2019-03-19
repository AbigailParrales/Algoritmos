def clear(array,x,y):
    array[y][x] = 0
    
def set(array,x,y):
    array[y][x] = 1
    
def check(board,x,y):
    #check Row
    for i in range(0,len(board[y])-1):
        if board[y][i] == 1:
            return False
    #check Column
    for j in range(0,len(board)-1):
        if board[j][x] == 1:
            return False
    #check Right Upward Diagonal
    for i,j in zip(range(x,len(board[y])),range(y,-1,-1)):
        if board[j][i] == 1:
            return False
    #check Left Upward Diagonal
    for i,j in zip(range(x,-1,-1),range(y,-1,-1)):
        if board[j][i] == 1:
            return False
        
    return True
    
def recursivePlacing(board,x,N):
    # Check if there are still left
    if (x >= N):
        return True
    
    for k in range(N):
        #Check for the current queen if it is safe
        if (check(board,x,k)):
            set(board,x,k)
            if(recursivePlacing(board,x+1,N)):
                return True
            clear(board,x,k)
            
    return False
            

def N_Queens(n):
    
    N = int(n)
    Board = []
    
    # Generate the board
    for j in range(0,N):
        newRow = []
        for i in range(0,N):
            newRow.append(0)
        Board.append(newRow)
        
#    if(check(Board,0,0)):
#        set(Board,0,0)
#    if(check(Board,1,1)):
#        set(Board,1,1)
        
    recursivePlacing(Board,0,N)
    
    return Board

def printBoard(board,N):
    print('Board for N: ',N)
    for i in range(N):
        print (board[i])
    print('\n')
    
"""if __name__ == '__main__':
    printBoard(N_Queens(4),4)
    printBoard(N_Queens(5),5)
    printBoard(N_Queens(10),10)"""