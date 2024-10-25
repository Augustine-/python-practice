# setup
rows = 4
cols = 4
mines = [(0, 2), (1, 2)]
board = [['-' for _ in range(cols)] for _ in range(rows)]

for mine in mines:
    board[mine[0]][mine[1]] = "*"

def display():
    for row in board:
        print("".join(row))

def reveal(r, c):
    if board[r][c] == "*":
        display()
        print("you lose")
        return False
    else:
        board[r][c] = count_adj_mines(r, c)
        return True

def count_adj_mines(r, c):
    mines = 0

    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if valid_coord(i, j) and board[i][j] == "*":
               mines += 1

    return str(mines)

def valid_coord(r, c):
    return (0 <= r < rows) and (0 <= c < cols)

def play_game():
    running = True

    while running:
        display()
        r, c = get_input()
        running = reveal(r, c)
        running = win_check()

def get_input():
    r = input("input a row: ")
    c = input("input a col: ")

    try:
        r = int(r) -1
        c = int(c) -1
        if not valid_coord(r, c):
            print("invalid coords, try again")
            get_input()
        else:
            return (r, c)
    except:
        print("invalid input, try again")
        get_input()

def win_check():
    for row in board:
        if "-" in row:
            return True
    display()
    print("you win")
    return False

###

play_game()