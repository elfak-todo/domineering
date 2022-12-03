from enum import Enum

GameMode = Enum('GameMode', ['PVP', 'PVAI'])
DominoType = Enum('DominoType', ['VERTICAL', 'HORIZONTAL'])
TileType = Enum('TileType', ['EMPTY', 'VERTICAL', 'HORIZONTAL'])

class Game:
    def __init__(self):
        self.board = []
        self.d_type = DominoType.VERTICAL

    def init(self, m, n, d_type):
        self.m = m
        self.n = n
        self.d_type = d_type
        self.reset_board(m, n)

    def reset_board(self, m, n):
        self.board = [[TileType.EMPTY] * n for i in range(m)]

    def is_move_valid(self, x, y, d_type):
        if (x < 0 or y < 0 or x >= self.n or y >= self.m):
            return False

        if d_type is DominoType.HORIZONTAL:
            if((x >= self.n - 1) or not self.board[y][x] is TileType.EMPTY or not self.board[y][x + 1] is TileType.EMPTY):
                return False
        else:
            if((y < 1) or not self.board[y][x] is TileType.EMPTY 
                or not self.board[y - 1][x] is TileType.EMPTY):
                return False
        return True

    def make_a_move(self, x, y, d_type):
        if not self.is_move_valid(x, y, d_type):
            return d_type
        
        if d_type is DominoType.HORIZONTAL:
            self.board[y][x] = TileType.HORIZONTAL
            self.board[y][x + 1] = TileType.HORIZONTAL
        else:
            self.board[y][x] = TileType.VERTICAL
            self.board[y - 1][x] = TileType.VERTICAL

        self.d_type = swap(self.d_type)
        return self.d_type

    def game_over(self, d_type):
        if d_type is DominoType.HORIZONTAL:
            for i in range(len(self.board) - 1):
                for j in range(len(self.board[i])):
                    if self.board[i][j] is TileType.EMPTY and self.board[i + 1][j] is TileType.EMPTY:
                        return False
        else:
            for i in range(len(self.board)):
                for j in range(len(self.board[i]) - 1):
                    if self.board[i][j] is TileType.EMPTY and self.board[i][j + 1] is TileType.EMPTY: 
                        return False
        return True

def swap(d_type):
    return DominoType.VERTICAL if d_type is DominoType.HORIZONTAL else DominoType.HORIZONTAL

class Settings:
    def __init__(self, m = 8, n = 8, starting_domino_type = DominoType.VERTICAL,
                    game_mode: GameMode = GameMode.PVP):
        self.m = m
        self.n = n
        self.domino_type = starting_domino_type
        self.game_mode = game_mode

