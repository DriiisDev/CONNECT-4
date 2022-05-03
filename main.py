
import termcolor

"""
diagram of what the board should look like 
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | | 

"""

#how the board is built and accept move
board =[[" "," "," "," "," "," "," "], 
        [" "," "," "," "," "," "," "], 
        [" "," "," "," "," "," "," "], 
        [" "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "], 
        [" "," "," "," "," "," "," "]]

#function to create the board
def createboard():
    for r in range (12): 
        if r % 2 == 0:
            practicalRow = int(r / 2) 
            for c in range(15):
                if c % 2 == 0:
                    practicalColumn = int(c / 2)
                    if c == 14:
                        print("|")
                    else:
                        print("|", end="")
                else:
                    #print("     ", end="")
                    print( board[practicalRow][practicalColumn], end="")
    print("-" * 15)

#---------- Horizontal win checks ----------
def check_Win_H_X(): #Horizontal win for "X"
    for practicalRow in range(5,-1,-1):
        for practicalColumn in range(4):
            if (board[practicalRow][practicalColumn]==X and board[practicalRow][practicalColumn+1]==X
            and board[practicalRow][practicalColumn+2]==X and board[practicalRow][practicalColumn+3]==X):
                return True

def check_Win_H_O(): #Horizontal win for "O"
    for practicalRow in range(5,-1,-1):
        for practicalColumn in range(4):
            if (board[practicalRow][practicalColumn]==O and board[practicalRow][practicalColumn+1]==O
            and board[practicalRow][practicalColumn+2]==O and board[practicalRow][practicalColumn+3]==O):
                return True

#---------- Vertical win checks ----------
def check_Win_V_X(): #Vertical win for "X"
    for practicalRow in range(2,-1,-1):
        for practicalColumn in range(7):
            if turn>6:
                if (board[practicalRow][practicalColumn]==X and board[practicalRow+1][practicalColumn]==X
                and board[practicalRow+2][practicalColumn]==X and board[practicalRow+3][practicalColumn]==X):
                    return True

def check_Win_V_O(): #Vertical win for "O"
    for practicalRow in range(2,-1,-1):
        for practicalColumn in range(7):
            if turn > 6:
                if (board[practicalRow][practicalColumn]==O and board[practicalRow+1][practicalColumn]==O
                and board[practicalRow+2][practicalColumn]==O and board[practicalRow+3][practicalColumn]==O):
                    return True

#---------- Diagonal win checks ----------
def check_Win_D_R_X(): #Diagonal win for "X" "\"
    for practicalRow in range(3):
        for practicalColumn in range(4): 
            if (board[practicalRow][practicalColumn] == X and board[practicalRow + 1][practicalColumn + 1] == X 
            and board[practicalRow + 2][practicalColumn + 2] == X and board[practicalRow + 3][practicalColumn + 3] == X):
                return True

def check_Win_D_L_X(): #Diagonal win for "X" "/"
    for practicalRow in range(5,2,-1):
        for practicalColumn in range(3,7,1): 
            if (board[practicalRow][practicalColumn] == X and board[practicalRow - 1][practicalColumn - 1] == X 
            and board[practicalRow - 2][practicalColumn - 2] == X and board[practicalRow - 3][practicalColumn - 3] == X):
                return True
    
def check_Win_D_R_O(): #Diagonal win for "O" "\"
    for practicalRow in range(3):
        for practicalColumn in range(4): 
            if (board[practicalRow][practicalColumn] == O and board[practicalRow + 1][practicalColumn + 1] == O 
            and board[practicalRow + 2][practicalColumn + 2] == O and board[practicalRow + 3][practicalColumn + 3] == O):
                return True
                
def check_Win_D_L_O(): #Diagonal win for "O" "/"
    for practicalRow in range(5,2,-1):
        for practicalColumn in range(3,7,1): 
            if (board[practicalRow][practicalColumn] == O and board[practicalRow - 1][practicalColumn - 1] == O 
            and board[practicalRow - 2][practicalColumn - 2] == O and board[practicalRow - 3][practicalColumn - 3] == O):
                return True

createboard()

#u'\u2B24'
X = termcolor.colored(u'\u2B24',"red")
O = termcolor.colored(u'\u2B24',"blue")

#This list stores the row that its about to put a mark
checkRowList = [5,5,5,5,5,5,5] 
player = 1
turn = 0

while turn < 42:
    print("Player's",player,"turn")
    chosenColumn = int(input("choose column (1 - 7) to play: ")) - 1

    if checkRowList[chosenColumn] == -1:
        print("Column full, please choose another column")
    else:
        turn += 1
        row = checkRowList[chosenColumn]
        checkRowList[chosenColumn] -= 1
        
        if player == 1:
            board[row][chosenColumn] = X
            player = 2
            createboard()
            
            #Here check for "X" win in all ways
            if check_Win_H_X()==True:
                print("Player one h win!")
                break
            
            if check_Win_V_X() == True:
                print("Player one v win!")
                break

            if check_Win_D_R_X() == True or check_Win_D_L_X() == True:
                print("Player one d win!")
                break

        elif player == 2:
            board[row][chosenColumn] = O
            player = 1
            createboard()

            #Here check for "O" win in all ways
            if check_Win_H_O()==True:
                print("Player two h win!")
                break
            
            if check_Win_V_O() == True:
                print("Player two v win!")
                break

            if check_Win_D_R_O() == True or check_Win_D_L_O() == True:
                print("Player two d win!")
                break
else:
    print("Its a tie")

if __name__ == "__main__":
    pass