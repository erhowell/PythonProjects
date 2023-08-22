
f = open("PythonProjects/ConwaysGameOfLife", "r")
line = f.readline()
board = []
while line :
    board.append(line.strip().split(','))
    line = f.readline()
f.close()


def getNeighbors(row,col):
    pass

def outputBoard(board):
    pass

for row in range(len(board)):
    for col in range(len(board[row])):
        neighbors= getNeighbors(row,col)
        #logic


        outputBoard(board)
    

# make 1 iteration
#   traverse the board
#   find score
#   if Already alive : logic for already alive
#   if not alive : logic for not alive
#   output

# if cell is empty
#     only cells with 3 neighbors become populated
# if cell is populated:
#   if cell has 0 or 1 neighbors- cell dies
#   if cell has 2 or 3 neighbors - cell keeps living
#   if cell has 4 or more neighbors - cell dies
