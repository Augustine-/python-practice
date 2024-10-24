class Node():
    def __init__(self):
        self.mine = False
        self.adj_mines = 0
        self.revealed = False
        self.adj_nodes = []

class Game():
    def __init__(self, m=4, n=4, mines=[(0, 2), (1, 2)]) -> None:
        self.board = []
        self.running = True
        self.width = m
        self.height = n
        self.setup(mines)

    def loop(self):
        while self.running:
            self.display()
            self.get_input()
            self.victory()

    def setup(self, mines):
        for r in range(self.height):
            row = []
            for c in range(self.width):
                row.append(Node())
            self.board.append(row)

        for mine in mines:
            self.board[mine[0]][mine[1]].mine = True

        for r in range(self.height):
            for c in range(self.width):
                node = self.board[r][c]
                for v1 in range(-1, 2):
                    for v2 in range(-1, 2):
                        if (r+v1, c+v2) != (r, c) and self.valid_coord(r+v1, c+v2):
                            adj = self.board[r + v1][c + v2]
                            node.adj_nodes.append(adj)
                            if adj.mine:
                                node.adj_mines += 1

    def display(self):
        for row in self.board:
            rowstr = ""
            for node in row:
                if node.mine:
                    rowstr += "*"
                elif node.revealed:
                    rowstr += str(node.adj_mines)
                else:
                    rowstr += "-"

            print(rowstr)

    def get_input(self):
        r = int(input("select a row: ")) - 1
        c = int(input("select a column: ")) - 1

        if not isinstance(r, int) or not isinstance(c, int) or not self.valid_coord(r, c):
            print("invalid input, try again")
            self.get_input()
        else:
            self.reveal(self.board[r][c])

    def reveal(self, node):
        if node.mine:
                self.display()
                print('you lose')
                self.running = False
        else:
            node.revealed = True
            if node.adj_mines == 0:
                for adj_node in node.adj_nodes:
                    if not adj_node.revealed:
                        self.reveal(adj_node)

    def valid_coord(self, r, c):
        if r < 0 or r >= self.height:
            return False
        elif c < 0 or c >= self.width:
            return False
        else:
            return True

    def victory(self):
        for row in self.board:
            for node in row:
                if not node.mine and not node.revealed:
                    return

        print("you win")
        self.running = False


def prompt_user_for_board():
    m = int(input("select a board width: "))
    n = int(input("select a board height: "))
    # TODO: allow the user to select mines
    # or a difficulty that derives a num of mines based on area
    # and randomly assigns those mines to nodes.
    # mines = int(input("select a number of mines: "))

    if not isinstance(m, int) or not isinstance(n, int):
        print("invalid input. proceeding with default size of 4x4...")
        return Game()
    else:
        return Game(m, n)

if __name__ == "__main__":
    g = prompt_user_for_board()
    g.loop()

