# Prazno - -1
# Player 1 - Uspravno - 0
# Player 2 - Vodoravno - 1

# Nema potrebe da cuvamo koji igrac je postavio plocicu jer ne utice na ishod igre. 
# Za stanja je bitno samo da li je polje zauzeto ili ne


# Dozvljeno je hradkodiranje pocetne dubine trazenja, 
# pa da posle dinamicki menjamo kako bismo kontrolisali brzinu igre
# Obrada stabla stanja preko MiniMax sa alfa beta odsecanjem jer ubrzava igru za 33%
# Igra ima visok nivo simetrije tako da mozemo da posmatramo samo 1/4 stanja


"""Reprezentacija stanja na nacin na koji izbegavamo navodnike

class Symbol(object):
    def __init__(self, name):
        self.name = name
    def --repr__(self):
        return self.name
"""



class Game:
    def __init__(self):
        self.board = []
        self.d_type = 0

    def init(self, m, n, d_type):
        self.d_type = d_type
        self.resetBoard(m, n)
        print(self.board)

    def resetBoard(self, m, n):
        self.board = [[[0] * m] * n]

    def gameOver(self, d_type):
        if d_type == True:
            for i in range(len(self.board) - 1):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == 0 and self.board[i + 1][j] == 0:
                        return True
        else:
            for i in range(len(self.board)):
                for j in range(len(self.board[i]) - 1):
                    if self.board[i][j] == 0 and self.board[i][j + 1] == 0: 
                        return True
        return False

    def swap(self):
        self.d_type = not self.d_type
        return self.d_type
    

class Settings:
    def __init__(self, m=4, n=4, domino_type=0, pvp=False):
        self.m = m
        self.n = n
        self.domino_type = domino_type
        self.pvp = pvp

    