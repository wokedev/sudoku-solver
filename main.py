#wokedev

#input grid
grid = [[6,0,4,0,0,0,9,1,0],
        [8,9,0,4,5,0,3,0,0],
        [0,0,5,0,9,0,8,4,2],
        [0,0,0,0,0,9,0,0,1],
        [3,0,0,5,0,4,0,0,6],
        [2,0,0,1,0,0,0,0,0],
        [9,5,3,0,7,0,1,0,0],
        [0,0,7,0,4,5,0,3,9],
        [0,6,2,0,0,0,5,0,8]]
                
# [0,0,0,0,0,0,0,0,0]

def printBoard(bo): #print and layout of board 
    for x in range(len(bo)):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - -")

        for y in range(len(bo[0])):
            if y % 3 == 0 and y != 0:
                print(" | ", end="")
            if y == 8:
                print(bo[x][y])
            else:
                print(str(bo[x][y]) + " ", end="")

def findEmpty(bo): #find 0s 
    for x in range(len(bo)):
        for y in range(len(bo[0])):
            if bo[x][y] == 0:
                return (x,y)
    return None

def valid(bo, num, pos): #verifying 
    #check row
    for x in range(len(bo[0])):
        if bo[pos[0]][x] == num and pos[1] !=x:
            return False
    
    #check column
    for x in range(len(bo[0])):
        if bo[x][pos[1]] == num and pos[0] !=x:
            return False
    
    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for x in range(box_y * 3, box_y*3 + 3):
        for y in range(box_x * 3, box_x*3 + 3):
            if bo[x][y] == num and (x,y) !=pos:
                return False
    return True

def solve(bo): #solving algorithm 
    find = findEmpty(bo)
    if not find:
        return True
    else:
        row, col = find
    for x in range(1,10):
        if valid(bo, x, (row,col)):
            bo[row][col] = x
            if solve(bo):
                return True
            bo[row][col] = 0
    return False

if __name__ == "__main__":
    print("\nProblem:")
    printBoard(grid)
    solve(grid)
    print("\nSolution:")
    printBoard(grid)
