# intiallize a dictionary as board to play
board= {'7':'   ' , '8':'   ' , '9':'   ',
        '4':'   ' , '5':'   ' , '6':'   ',
        '1':'   ' , '2':'   ' , '3':'   '}

#create a function to print the board
def printBoard(board):
    print(board['7']+'|'+ board['8'] + '|' + board['9'])
    print('---|---|---')
    print(board['4']+'|'+ board['5'] + '|' + board['6'])
    print('---|---|---')
    print(board['1']+'|'+ board['2'] + '|' + board['3'])

# create a function to run the game's logic
def game():
    #initialize as X's turn
    turn='X'
    count=0

    for i in range(11):
        printBoard(board)

        #Get the location
        print('Its your turn',turn,'Enter the position :')
        put=input()
        if board[put] == '   ':
            board[put] = ' '+turn+' '
            count+=1
        else:
            print('This place is already filled')
            continue
            
        #Check for match in horizontal, diagonal, and vertical
        if count>=5:
            if board['7'] == board['8'] == board['9'] != '   ':
                printBoard(board)
                print('Game Over')
                print('~~~~~~', turn , 'won ~~~~~~')
                break
            elif board['4'] == board['5'] == board['6'] != '   ':
                printBoard(board)
                print('Game Over')
                print('~~~~~~', turn , 'won ~~~~~~')
                break
            elif board['1'] == board['2'] == board['3'] != '   ':
                printBoard(board)
                print('Game Over')
                print('~~~~~~', turn , 'won ~~~~~~')
                break
            elif board['1'] == board['5'] == board['9'] != '   ':
                printBoard(board)
                print('Game Over')
                print('~~~~~~', turn , 'won ~~~~~~')
                break
            elif board['7'] == board['5'] == board['3'] != '   ':
                printBoard(board)
                print('Game Over')
                print('~~~~~~', turn , 'won ~~~~~~')
                break
            elif board['7'] == board['4'] == board['1'] != '   ':
                printBoard(board)
                print('Game Over')
                print('~~~~~~', turn , 'won ~~~~~~')
                break
            elif board['8'] == board['5'] == board['2'] != '   ':
                printBoard(board)
                print('Game Over')
                print('~~~~~~', turn , 'won ~~~~~~')
                break
            elif board['9'] == board['6'] == board['3'] != '   ':
                printBoard(board)
                print('Game Over')
                print('~~~~~~', turn , 'won ~~~~~~')
                break
        
        #Condition for tie if no match is found
        if count == 9:
            print('Game Over\nIts a Tie')
            break
        
        #Change the turn each time
        if turn == 'X':
            turn='O'
        else:
            turn='X'

    #Ask for restart
    restart = input('Do you want to play Again??(y/n)')
    if restart == 'y' or restart == 'Y':
        for key in board:
            board[key]='   '

        game()   

#Main function
if __name__ == '__main__':
    game()