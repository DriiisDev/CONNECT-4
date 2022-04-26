
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

#u'\u2B24'
X = termcolor.colored(u'\u2B24',"red")
O = termcolor.colored(u'\u2B24',"blue")

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


#Horizontal win checks

def checkForWinhX():
    #Horizontal win for "X"
    for practicalRow in range(5,-1,-1):
        for practicalColumn in range(4):
            if (board[practicalRow][practicalColumn]==X and board[practicalRow][practicalColumn+1]==X
            and board[practicalRow][practicalColumn+2]==X and board[practicalRow][practicalColumn+3]==X):
                return True

def checkForWinhO():
    #Horizontal win for "O"
    for practicalRow in range(5,-1,-1):
        for practicalColumn in range(4):
            if (board[practicalRow][practicalColumn]==O and board[practicalRow][practicalColumn+1]==O
            and board[practicalRow][practicalColumn+2]==O and board[practicalRow][practicalColumn+3]==O):
                return True


#Vertical win checks

def checkForWinvX():
    #vertical win for "X"
    for practicalRow in range(5,-1,-1):
        for practicalColumn in range(4):
            if (board[practicalRow][practicalColumn]==X and board[practicalRow-1][practicalColumn]==X
            and board[practicalRow-2][practicalColumn]==X and board[practicalRow-3][practicalColumn]==X):
                return True

def checkForWinvO():
    #vertical win for "O"
    for practicalRow in range(5,-1,-1):
        for practicalColumn in range(4):
            if (board[practicalRow][practicalColumn]==O and board[practicalRow-1][practicalColumn]==O
            and board[practicalRow-2][practicalColumn]==O and board[practicalRow-3][practicalColumn]==O):
                return True


#Diagonal win checks

def checkDiagonalX():
    #Diagonal win for "X"
    for practicalRow in range(5,-1,-1):# Checks 4 spots diagonally going left
        for practicalColumn in range(4): 
            if (board[practicalRow][practicalColumn] == X and board[practicalRow - 1][practicalColumn + 1] == X 
            and board[practicalRow - 2][practicalColumn + 2] == X and board[practicalRow - 3][practicalColumn + 3] == X):
                return True

    for practicalRow in range(len(board[0]) - 4):# Checks 4 spots diagonally going left
        for practicalColumn in range(4): 
            if (board[practicalRow][practicalColumn] == X and board[practicalRow + 1][practicalColumn + 1] == X 
            and board[practicalRow + 2][practicalColumn + 2] == X and board[practicalRow + 3][practicalColumn + 3] == X):
                return True
    

def checkDiagonalO():
    #Diagonal win for "O"
    for practicalRow in range(5,-1,-1):# Checks 4 spots diagonally going left
        for practicalColumn in range(4): 
            if (board[practicalRow][practicalColumn] == O and board[practicalRow - 1][practicalColumn + 1] == O 
            and board[practicalRow - 2][practicalColumn + 2] == O and board[practicalRow - 3][practicalColumn + 3] == O):
                return True
    
    for practicalRow in range(len(board[0]) - 4):# Checks 4 spots diagonally going right
        for practicalColumn in range(len(board) - 2): 
            if (board[practicalRow][practicalColumn] == O and board[practicalRow + 1][practicalColumn + 1] == O 
            and board[practicalRow + 2][practicalColumn + 2] == O and board[practicalRow + 3][practicalColumn + 3] == O):
                return True
    

createboard()

#This list stores the row that its about to put a mark
checkRowList = [5,5,5,5,5,5,5] 
player = 1

while True:
    print("Player's",player,"turn")
    chosenColumn = int(input("choose column (1 - 7) to play: ")) - 1

    if checkRowList[chosenColumn] == -1:
        print("Column full, choose another column")
    
    else:
        if player == 1:
            row = checkRowList[chosenColumn]
            board[row][chosenColumn] = X
            checkRowList[chosenColumn] -= 1
            player = 2
            createboard()
            
            #Here check for "X" win in all ways
            if checkForWinhX()==True:
                print("Player one win!")
                break
            
            if checkForWinvX() == True:
                print("Player one win!")
                break

            if checkDiagonalX() == True:
                print("Player one win!")
                break

        elif player == 2:
            row = checkRowList[chosenColumn]
            board[row][chosenColumn] = O
            checkRowList[chosenColumn] -= 1
            player = 1
            createboard()

            #Here check for "O" win in all ways
            if checkForWinhO()==True:
                print("Player two win!")
                break
            
            if checkForWinvO() == True:
                print("Player two win!")
                break

            if checkDiagonalO() == True:
                print("Player two win!")
                break

if __name__ == "__main__":
    pass
