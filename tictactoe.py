board = [' ' for  x in range(10)]



def insertletter(letter,pos):
    board[pos]=letter

def freespace(pos):
    return board[pos] == " "

def boardlayout(board):
    print(' ' + board[1] +' | '+ board[2] +' | '+ board[3] +' ')
    print("-------------")
    print(' ' + board[4] +' | '+ board[5] +' | '+ board[6] +' ')
    print("-------------")
    print(' ' + board[7] +' | '+ board[8] +' | '+ board[9] +' ')

def isboardfull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True

def winner(b,l):
    return ((b[1]==l and b[2]==l and b[3]==l) or
    (b[4]==l and b[5]==l and b[6]==l) or
    (b[7]==l and b[8]==l and b[9]==l) or
    (b[1]==l and b[4]==l and b[7]==l) or
    (b[2]==l and b[5]==l and b[8]==l) or
    (b[3]==l and b[6]==l and b[9]==l) or
    (b[7]==l and b[5]==l and b[3]==l) or
    (b[1]==l and b[5]==l and b[9]==l))

def playermove():
    run = True
    while run:
        move = input("Please select the position to place X between (1-9) ")
        try:
            move=int(move)
            if move > 0 and move <10:

                if freespace(move):
                    run= False
                    insertletter('X',move)
                else:
                    print("Sorry, this space is occupied")
            else:
                print("Please type a number between 1 and 9")
        except:
            print("Please type a number")

def computermove():
    possiblemoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0 ]
    move = 0

    for let in ['O' , 'X']:
        for i in possiblemoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if winner(boardcopy, let):
                move=i
                return move

    cornersopen = []
    for i in possiblemoves:
        for i in [1,3,7,9]:
            cornersopen.append(i)

    if len(cornersopen)>0:
        move= selectrandom(cornersopen)
        return move

    if 5 in possiblemoves:
        move=5
        return move

    edgesopen = []
    for i in possiblemoves:
        for i in [2,4,8,6]:
            edgesopen.append(i)
    if len(edgesopen)>0:
        move= selectrandom(edgesopen)
        return move

def selectrandom(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]

def main():

        print("Welcome to Tic Tac Toe!")
        boardlayout(board)


        while not(isboardfull(board)) :
            if not(winner(board,"O")):
                playermove()
                boardlayout(board)
            else :
                print("Sorry, you loose !")
                break

            if not(winner(board,"X")):
                move =computermove()
                if move == 0:
                    print(" ")
                else :
                    insertletter('O',move)
                    print('computer placed O on the board ',move, ":")
                    boardlayout(board)
            else :
                print("Congratulations,You win!")


        if isboardfull(board):
            print("Tie Game!")



while True:
    yn=input("Do you want to play? (y/n)")
    yn=yn.lower()

    if yn=="y":
        board = [' ' for  x in range(10)]
        print("------------------------------------------------------------")
        main()
    else:
        break
