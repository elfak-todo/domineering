# Prazno - -1
# Player 1 - Uspravno - 0
# Player 2 - Vodoravno - 1

class Game:
    def __init__(self):
        self.board = []

    def init(self, m, n):
        self.resetBoard(m, n)

    def resetBoard(self, m, n):
        self.board = [[-1] * m] * n
