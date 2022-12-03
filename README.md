# domineering

Prazno - -1
Player 1 - Uspravno - 0
Player 2 - Vodoravno - 1

Nema potrebe da cuvamo koji igrac je postavio plocicu jer ne utice na ishod igre.
Za stanja je bitno samo da li je polje zauzeto ili ne

Dozvljeno je hradkodiranje pocetne dubine trazenja,
pa da posle dinamicki menjamo kako bismo kontrolisali brzinu igre
Obrada stabla stanja preko MiniMax sa alfa beta odsecanjem jer ubrzava igru za 33%
Igra ima visok nivo simetrije tako da mozemo da posmatramo samo 1/4 stanja

"""Reprezentacija stanja na nacin na koji izbegavamo navodnike

class Symbol(object):
def **init**(self, name):
self.name = name
def --repr\_\_(self):
return self.name
"""
