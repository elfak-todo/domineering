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

    def is_move_valid(self, state, move, d_type):
        (x, y) = move
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

    def update_state(self, state, move, d_type):
        (x, y) = move
        new_state = copy.deepcopy(state)
        if d_type is DominoType.HORIZONTAL:
            new_state[y][x] = TileType.HORIZONTAL
            new_state[y][x + 1] = TileType.HORIZONTAL
        else:
            new_state[y][x] = TileType.VERTICAL
            new_state[y - 1][x] = TileType.VERTICAL
        return new_state

    def get_valid_moves(self, state, d_type):
        valid_moves = []
        for x in range(self.n):
            for y in range(self.m):
                if self.is_move_valid(state, (x, y), d_type):
                    valid_moves.append((x, y))
        return valid_moves

    def make_a_move(self, move, d_type):
        if not self.is_move_valid(self.board, move, d_type):
            return d_type
        
        self.board = self.update_state(self.board, move, d_type)

        if self.game_over(self.board, d_type):
            self.status = Status.VERTICAL_WON if d_type == DominoType.VERTICAL else Status.HORIZONTAL_WON            

        self.d_type = swap(self.d_type)

        return self.d_type

    def game_over(self, state, d_type):
        if d_type == DominoType.HORIZONTAL:
            for i in range(self.m - 1):
                for j in range(self.n):
                    if state[i][j] == TileType.EMPTY and state[i + 1][j] == TileType.EMPTY:
                        return False
        else:
            for i in range(self.m):
                for j in range(self.n - 1):
                    if state[i][j] == TileType.EMPTY and state[i][j + 1] == TileType.EMPTY: 
                        return False
        return True

    def evaluate_state(self, state):
        return (len(self.get_valid_moves(state, DominoType.HORIZONTAL))
                - len(self.get_valid_moves(state, DominoType.VERTICAL)))

    def max_value(self, state, depth, alpha, beta, move=None):
        valid_moves = self.get_valid_moves(state, DominoType.HORIZONTAL)

        if depth == 0 or valid_moves is None or len(valid_moves) == 0:
            return(move, self.evaluate_state(state))

        for vm in valid_moves:
            alpha = max(alpha, self.min_value(self.update_state(state, vm, DominoType.HORIZONTAL),
                    depth - 1, alpha, beta, vm if move is None else move), key=lambda x: x[1])
            if alpha[1] >= beta[1]:
                return beta
        return alpha

    def min_value(self, state, depth, alpha, beta, move=None):
        valid_moves = self.get_valid_moves(state, DominoType.VERTICAL)

        if depth == 0 or valid_moves is None or len(valid_moves) == 0:
            return(move, self.evaluate_state(state))

        for vm in valid_moves:
            beta = min(beta, self.max_value(self.update_state(state, vm, DominoType.VERTICAL),
                    depth - 1, alpha, beta, vm if move is None else move), key=lambda x: x[1])
            if beta[1] <= alpha[1]:
                return alpha
        return beta

    def minimax_alpha_beta(self, state, depth, d_type,
                        alpha=(None, -float('inf')), beta=(None, float('inf'))):
        if d_type == DominoType.HORIZONTAL:
            return self.max_value(state, depth, alpha, beta)
        else:
            return self.min_value(state, depth, alpha, beta)

def swap(d_type):
    return DominoType.VERTICAL if d_type is DominoType.HORIZONTAL else DominoType.HORIZONTAL

class Settings:
    def __init__(self, m = 8, n = 8, starting_domino_type = DominoType.VERTICAL,
                    game_mode: GameMode = GameMode.PVP):
        self.m = m
        self.n = n
        self.domino_type = starting_domino_type
        self.game_mode = game_mode

