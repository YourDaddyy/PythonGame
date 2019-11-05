#Programmer: Yixuan Liu
#Date: Wed 30 2019

def tic_tac_toe():
    board = [0,1,2,3,4,5,6,7,8,9]
    win_list = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9],
       [1, 4, 7],
       [2, 5, 8],
       [3, 6, 9],
       [1, 5, 9],
       [3, 5, 7],
    ]

    def draw(): #Draw the board
        print('  |   | ')
        print(board[7],'|',board[8],'|',board[9])
        print('-----------')
        print(board[4],'|',board[5],'|',board[6])
        print('-----------')
        print(board[1],'|',board[2],'|',board[3])
        print('  |   | ')

    def enter_number():
        while 1:
            print('Player ',player, ' pick your move.')
            try:
                move = int(input())
                if move in board:
                    board[move] = player
                    return move
                else:
                    print('\nInvaild move! Try again!')
            except ValueError:
                print('It is not a number. Please try again.')

    def game_over():#determine if game end
        for move,b,c in win_list:
            if board[move] == board[b] == board[c]:
                draw()
                print('\nPlayer ',player, ' wins!\n')
                return True
            if board.count('X') + board.count('O') == 9:
                print('The game tie!')
                return True
                
    for player in "XO"*9:
        draw()
        enter_number()
        if game_over():
            break
        
    
while 1:
    tic_tac_toe()
    if input('Play one more time? (y/n)\n') != "y" :
        break
