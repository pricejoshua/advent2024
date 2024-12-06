
word = ['X', 'M', 'A', 'S']

def check_next(grid, index, x, y, down, right):
    if (x >= 0 and x < len(grid) and (y >= 0 and y < len(grid[0]))):
        # print(len(grid[0]), len(grid))
        letter = grid[x][y]
        if (letter == word[index]): 
            if index == 3:
                return True
            else:
                return check_next(grid, index + 1, x + down, y + right, down, right)
        else: 
            return False
    else:
        return False

def check_x_mas(grid, x, y):
    if (x > 0 and x < len(grid) - 1) and (y > 0 and y < len(grid[0]) - 1):

        string = grid[x-1][y-1] + grid[x-1][y+1] + grid[x+1][y-1] + grid[x+1][y+1]

        if (string.count('M') == 2 and string.count('S') == 2 and grid[x-1][y-1] != grid[x+1][y+1] ):
            print("[", x-1, y-1, "]", "[", x-1, y+1, "]", "[", x+1, y-1, "]", "[", x+1, y+1, "]")
            # print(grid[x-1][y-1], grid[x-1][y+1], grid[x+1][y-1], grid[x+1][y+1])
            # print(grid[x-1][y-1], grid[x+1][y-1], "\n", grid[x-1][y+1], grid[x+1][y+1])
            for i in range(-1,2):
                for j in range(-1,2):
                    if (j == 0 or i == 0):
                        print("*", end = " ")
                    else:
                        print(grid[x+i][y+j], end = " ")
                print()
            return True



with open('day4/input.txt') as f:
    grid = []
    input = f.read()
    for line in input.split("\n"):
        grid.append(list(line))

    print(grid)
    
    count = 0
    

    for (i, row) in enumerate(grid):
        for (j, letter) in enumerate(row):
            if letter == 'A':
                if (check_x_mas(grid, i, j)):
                    count += 1
            # if letter == 'X':
            #     for d in range(-1,2):
            #         for r in range(-1,2):
            #             if (d != 0 or r != 0):
            #                 if (j  == 4):
            #                     print("here")
            #                 if (check_next(grid, 0, i, j, d, r) is True):
            #                     count += 1

    print(count)