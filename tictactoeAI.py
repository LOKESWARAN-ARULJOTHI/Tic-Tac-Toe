import random

# board
board= {1:' ' , 2:' ' , 3:' ',
        4:' ' , 5:' ' , 6:' ',
        7:' ' , 8:' ' , 9:' '}


# Prints the board
def printBoard(board):
    print('',board[7],'|',board[8] , '|' , board[9],'')
    print('---|---|---')
    print('',board[4],'|',board[5] , '|' , board[6],'')
    print('---|---|---')
    print('',board[1],'|',board[2] , '|' , board[3],'')
    print()

# Insert the symbol at the positon
def insertBoard(position, letter):
    if spaceIsFree(position):
        board[position] = letter

# Checks if a position is free 
def spaceIsFree(position):
    return board[position] == ' '

# Checks if the game draws
def isBoardFull(board):
    for key in board.keys():
        if board[key]==' ':
            return False
    return True

# Checks for winner 
def isWinner(board, letter):
    if(board[7] == board[8] == board[9] == letter) or (board[4] == board[5] == board[6] == letter) or (board[1] == board[2] == board[3] == letter) or (board[7] == board[5] == board[3] == letter) or (board[1] == board[5] == board[9] == letter) or (board[7] == board[4] == board[1] == letter) or (board[8] == board[5] == board[2] == letter) or (board[9] == board[6] == board[3] == letter):
        return True
    else: return False
    
# Human 1 input function
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

# Human 2 input function
def player2Move():
    run=True
    while run:
        move=input('Enter the move \'O\'(1-9):')
        try:
            move=int(move)
            if move>0 and move<10:
                if spaceIsFree(move):
                    run=False
                    insertBoard(move,'O')
                else:
                    print('The position is already filled!')
            else:
                print('Enter a number within (1-9)!')
        except:
            print('Enter a Valid number!')

# AI function that uses minimax algorithm
def compMove():
    bestScore = -999
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = 'O'
            score = minimax(board, 0,-999,999,False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertBoard(bestMove, 'O')
    return

# Minimax algorithm
def minimax(board, depth,alpha,beta, isMaximizing):
    if (isWinner(board,'O')):
        return 1
    elif (isWinner(board,'X')):
        return -1
    elif (isBoardFull(board)):
        return 0

    if (isMaximizing):
        bestScore = -999
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = 'O'
                score = minimax(board, depth + 1,-999,999, False)
                board[key] = ' '
                bestScore=max(bestScore,score)
                alpha=max(alpha,bestScore)
                if beta<=alpha:
                    break
        return bestScore

    else:
        bestScore = 999
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = 'X'
                score = minimax(board, depth + 1,-999,999, True)
                board[key] = ' '
                bestScore=min(bestScore,score)
                beta=min(beta,bestScore)
                if beta<=alpha:
                    break
        return bestScore
    
# Random move function for Human vs Random bot 
def randomMove(board):
    run=True
    while run:
        move=random.randrange(1,10)
        move=int(move)
        if move>0 and move<10:
            if spaceIsFree(move):
                run=False
                insertBoard(move,'O')

# Main function
def main():
    print('Welcome to Tic Tac Toe')
    printBoard(board)
    enemy=int(input('Do you want to play against\n1.Human\n2.Random bot\n3.AI : '))
    
    # Human vs Human
    if enemy==1:
        turn='X'
        while not isBoardFull(board):
            if turn=='X':
                if not isWinner(board,'O'):
                    playerMove()
                    printBoard(board)
                    turn='O'
                else:
                    print('Yeah,"O" won the match')
                    break
            elif turn=='O':
                if not isWinner(board,'X'):
                    player2Move()
                    printBoard(board)
                    turn='X'
                else:
                    print('Yehh, "X" won the match')
                    break
        if isBoardFull(board):
            print('Game over\nIt is a Tie')

    # Human vs random bot 
    elif enemy==2:
        turn='X'
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
                    randomMove(board)
                    printBoard(board)
                    turn='X'
                else:
                    print('Yehh, "X" won the match')
                    break
        if isBoardFull(board):
            print('Game over\nIt is a Tie')

    # Human vs AI
    elif enemy==3:
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
