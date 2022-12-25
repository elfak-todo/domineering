from enum import Enum
import copy

GameMode = Enum('GameMode', ['PVP', 'PVAI'])
DominoType = Enum('DominoType', ['VERTICAL', 'HORIZONTAL'])
TileType = Enum('TileType', ['EMPTY', 'VERTICAL', 'HORIZONTAL'])
Status = Enum('Status', ['PLAYING', 'VERTICAL_WON', 'HORIZONTAL_WON'])

class Game:
    def __init__(self, m, n, d_type, game_mode):
        self.board = []
        self.status = Status.PLAYING
        self.d_type = d_type
        self.m = m
        self.n = n
        self.board = [[TileType.EMPTY] * self.n for i in range(self.m)]       
        self.game_mode = game_mode       

    def is_move_valid(self, state, x, y, d_type):
        if (x < 0 or y < 0 or x >= self.n or y >= self.m):
            return False

        if d_type == DominoType.HORIZONTAL:
            if((x >= self.n - 1) or not state[y][x] == TileType.EMPTY or not state[y][x + 1] == TileType.EMPTY):
                return False
        else:
            if((y < 1) or not state[y][x] == TileType.EMPTY 
                or not state[y - 1][x] == TileType.EMPTY):
                return False
        return True

    def update_state(self, state, x, y, d_type):
        new_state = copy.deepcopy(state)
        if d_type is DominoType.HORIZONTAL:
            new_state[y][x] = TileType.HORIZONTAL
            new_state[y][x + 1] = TileType.HORIZONTAL
        else:
            new_state[y][x] = TileType.VERTICAL
            new_state[y - 1][x] = TileType.VERTICAL
        return new_state

    def get_valid_states(self, state, d_type):
        valid_moves = []
        for x in range(self.n):
            for y in range(self.m):
                if self.is_move_valid(state, x, y, d_type):
                    valid_moves.append((x, y))
        return valid_moves

    def make_a_move(self, x, y, d_type):
        if not self.is_move_valid(self.board, x, y, d_type):
            return d_type
        
        self.board = self.update_state(self.board, x, y, d_type)

        if self.game_over(self.board, d_type):
            self.status = Status.VERTICAL_WON if d_type == DominoType.VERTICAL else Status.HORIZONTAL_WON            

        self.d_type = swap(self.d_type)

        return self.d_type

    def game_over(self, state, d_type):
        if d_type is DominoType.HORIZONTAL:
            for i in range(len(state) - 1):
                for j in range(len(state[i])):
                    if state[i][j] is TileType.EMPTY and state[i + 1][j] is TileType.EMPTY:
                        return False
        else:
            for i in range(len(state)):
                for j in range(len(state) - 1):
                    if state[i][j] is TileType.EMPTY and state[i][j + 1] is TileType.EMPTY: 
                        return False
        return True

    def evaluate_state(self, state):
        return len(self.get_valid_states(state, DominoType.HORIZONTAL)) - len(self.get_valid_states(state, DominoType.VERTICAL))

    def max_stanje(self, lsv):
        return max(lsv, key=lambda x: x[1])

    def min_stanje(self, lsv):
        return min(lsv, key=lambda x: x[1])

    def minimax(self, stanje, dubina, d_type, move=None):
        lista_poteza = self.get_valid_states(stanje, d_type)
        min_max_stanje = self.max_stanje if d_type is DominoType.HORIZONTAL else self.min_stanje

        if dubina == 0 or lista_poteza is None or len(lista_poteza) == 0:
            return(move, self.evaluate_state(stanje))

        return min_max_stanje([self.minimax(self.update_state(stanje, x[0], x[1], d_type), dubina - 1, swap(d_type), x if move is None else move) for x in lista_poteza])

def swap(d_type):
    return DominoType.VERTICAL if d_type is DominoType.HORIZONTAL else DominoType.HORIZONTAL

class Settings:
    def __init__(self, m = 8, n = 8, starting_domino_type = DominoType.VERTICAL,
                    game_mode: GameMode = GameMode.PVP):
        self.m = m
        self.n = n
        self.domino_type = starting_domino_type
        self.game_mode = game_mode

