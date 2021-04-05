board= {1:' ' , 2:' ' , 3:' ',
        4:' ' , 5:' ' , 6:' ',
        7:' ' , 8:' ' , 9:' '}
inf=100000
neginf=-100000
def printBoard(board):
    print('',board[7],'|',board[8] , '|' , board[9],'')
    print('---|---|---')
    print('',board[4],'|',board[5] , '|' , board[6],'')
    print('---|---|---')
    print('',board[1],'|',board[2] , '|' , board[3],'')
    print()

def insertBoard(position, letter):
    if spaceIsFree(position):
        board[position] = letter

def spaceIsFree(position):
    return board[position] == ' '

def isBoardFull(board):
    for key in board.keys():
        if board[key]==' ':
            return False
    return True

def isWinner(board, letter):
    if(board[7] == board[8] == board[9] == letter) or (board[4] == board[5] == board[6] == letter) or (board[1] == board[2] == board[3] == letter) or (board[7] == board[5] == board[3] == letter) or (board[1] == board[5] == board[9] == letter) or (board[7] == board[4] == board[1] == letter) or (board[8] == board[5] == board[2] == letter) or (board[9] == board[6] == board[3] == letter):
        return True
    else: return False
    
def playerMove():
    run=True
    while run:
        move=input('Enter the move \'X\'(1-9):')
        try:
            move=int(move)
            if move>0 and move<10:
                if spaceIsFree(move):
                    run=False
                    insertBoard(move,'X')
                else:
                    print('The position is already filled!')
            else:
                print('Enter a number within (1-9)!')
        except:
            print('Enter a Valid number!')

def compMove():
    mEval=neginf
    bMove=0
    for key in board.keys():
        if board[key]==' ':
            board[key]='O'
            currEval=minimax(board,0,False)
            if currEval>mEval:
                mEval=currEval
                bMove=key
    insertBoard(bMove,"O")

def evaluate(board):
    score=isWinner(board,'X')
    if score==True:
        return -10
    score=isWinner(board,"O")
    if score==True:
        return 10
    if score==False:
        return 0

def minimax(board, depth, isMaximizingPlayer):
    value = evaluate(board)
    if value==10:
        return value
    
    if value==-10:
        return value
    
    if isBoardFull(board)==True or value==0:
        return 0
    
    if isMaximizingPlayer:
        maxEval=neginf
        for key in board.keys():
            if board[key]==' ':
                board[key]='O'
                currEval=minimax(board,depth+1,False)
                maxEval=max(currEval,maxEval)
                board[key]=' '
        return maxEval
    
    else:
        minEval=inf
        for key in board.keys():
            if board[key]==' ':
                board[key]='X'
                currEval=minimax(board,depth+1,True)
                minEval=min(currEval,minEval)
                board[key]=' '
        return minEval

    

# def randomMove(board):
#     run=True
#     while run:
#         move=random.randrange(0,10)
#         move=int(move)
#         if move>0 and move<10:
#             if spaceIsFree(move):
#                 run=False
#                 insertBoard(move,'X')


def main():
    print(inf)
    print('Welcome to Tic Tac Toe')
    printBoard(board)
    starter=input('Do you want to start?(Y/N)?')
    if starter=='y' or starter=='Y':
        turn = 'X'
    else:
        turn = 'O'
    while not isBoardFull(board):
        if turn=='X':
            if not isWinner(board,'O'):
                playerMove()
                printBoard(board)
                turn='O'
            else:
                print('Sorry,"O" won the match')
                break
        elif turn=='O':
            if not isWinner(board,'X'):
                compMove()
                printBoard(board)
                turn='X'
            else:
                print('Yehh, "X" won the match')
                break
    
    if isBoardFull(board):
        print('Game over\nIt is a Tie')
    

main()
