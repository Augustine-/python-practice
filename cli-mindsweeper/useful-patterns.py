# creating a 2d matrix, a board
rows, cols = 4, 4
board = [['-' for _ in range(cols)] for _ in range(rows)]

# display a board
def display_board():
    for row in board:
        print(''.join(row))

    print("")

# get and validate user input
def get_input():
    r = int(input("enter a row: "))
    c = int(input("enter a col: "))

    if (isinstance(r, int) and isinstance(c, int)) and (1 <= r <= rows and 1 <= c <= cols):
        r -= 1
        c -= 1
        # do stuff with the input
        return (r, c)
    else:
        print("invalid input, try again.")
        print(f"enter a single integer between 1 and {rows} for the row, and 1 and {cols} for the col.")
        get_input()

# neighbor traversal in a 2d matrix
r, c = get_input()

for i in range(r-1, r+2):
    for j in range(c-1, c+2):
        if 0 <= i < rows and 0 <= j < cols:
            #do stuff with the valid neighbors
            pass

# avoid repeat visits, use a stack instead of recursion for memory efficiency
def dfs_traverse(r, c):
    seen = set()
    stack = [(r, c)]

    while stack:
        x, y = stack.pop()
        if (x, y) in seen:
            continue
        seen.add((x, y))


        # process node
        board[x][y] = "*"
        display_board()

        for i in range(x-1, y+2):
            for j in range(x-1, y+2):
                if (0 <= i < rows and 0 <= j < cols):
                    stack.append((i, j))

# bfs version of above
from collections import deque
def bfs_traverse(r, c):
    seen = set()
    q = deque([(r, c)])

    while q:
        # progress queue
        x, y = q.popleft()

        #end condition
        if (x, y) in seen:
            continue
        seen.add((x, y))

        # process node
        board[x][y] = "*"
        display_board()

        # scan neighbors
        for i in range(x-1, y+2):
            for j in range(x-1, y+2):
                if (0 <= i < rows and 0 <= j < cols):
                    q.append((i, j))


# ---

# dfs_traverse(r, c)
bfs_traverse(r, c)
