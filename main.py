# Jeu n°1
# En premier lieu un jeu que l’on notera A qui est un simple jeu de pile ou face avec une pièce biaisée (pile avec une probabilité de p=0.49). Le joueur mise un euro et lance la pièce : s’il obtient pile il gagne un euro en plus de récupérer sa mise, sinon il perd sa mise.

import random


def jeuA(capital=1000):
    piece = ['pile', 'face']
    pourcentage = [49, 51]
    nbLance = random.choices(piece, pourcentage, k=10000)
    for elt in nbLance:
        if elt == 'pile':
            capital += 1
        else:
            capital -= 1
    return capital


print(jeuA())
# Jeu perdant

# Jeu n°2
# Ensuite, un jeu que l’on notera B, qui est un jeu avec deux pièces biaisées. La première pièce donne pile avec une probabilité p1 = 0.09 et la seconde pièce donne pile avec une probabilité p2 = 0.74. Le joueur de ne peut miser qu’un euro à la fois ! En revanche, on regarde à chaque lancé son capital (la somme d’argent total) dont il dispose pour déterminer quelle pièce lancer : si le capital est un multiple de 3, on lance la pièce numéro une, sinon on lance la seconde pièce. Comme dans le jeu A, le joueur remporte sa mise plus un euro supplémentaire si la pièce choisie tombe sur pile, sinon il perd sa mise.

import random


class Jeu:

    def __init__(self, capital=1000):
        self.capital = capital

    def tirage_piece(self, capital):
        piece = ['pile', 'face']
        pourcentage1 = [9, 91]
        pourcentage2 = [74, 26]
        if capital % 3 == 0:
            result = random.choices(piece, pourcentage1)
        else:
            result = random.choices(piece, pourcentage2)
        return result


def compteCapital(tirage):
    if "pile" in tirage:
        game.capital += 1
    else:
        game.capital -= 1
    return game.capital


game = Jeu()
for i in range(10000):
    tirage = game.tirage_piece(game.capital)
    compteCapital(tirage)
print(compteCapital(tirage))
# Jeu perdant


# Jeu n°3
# On va à présent mixer les deux jeux présentés dans la question précédente ! En effet, à chaque tour, on lance une pièce (cette fois-ci...) équilibrée ! Si l'on a pile, on joue au jeu A, sinon on joue au jeu B.
# On suppose que le joueur a 1000 euros comme capital de départ.
# Après avoir joué 1.000.000 de parties, quel est le statut du jeu, du point de vue du joueur ?

import random


class Jeu:

    def __init__(self, capital=1000):
        self.capital = capital

    def jeuA(self):
        piece = ['pile', 'face']
        pourcentage = [49, 51]
        lance = random.choices(piece, pourcentage)
        return result

    def jeuB(self, capital):
        result = []
        piece = ['pile', 'face']
        pourcentage1 = [9, 91]
        pourcentage2 = [74, 26]
        if capital % 3 == 0:
            result = random.choices(piece, pourcentage1)
        else:
            result = random.choices(piece, pourcentage2)
        return result

    def jeuC(self):
        piece = ['pile', 'face']
        pourcentage = [50, 50]
        result = random.choices(piece, pourcentage)
        return result


def compteCapital(lanceDePiece):  # lanceDePiece = result du jeu A ou du jeu B
    if "pile" in lanceDePiece:
        game.capital += 1
    else:
        game.capital -= 1
    return game.capital


game = Jeu()
for i in range(1000000):
    result = game.jeuC()  # on tire  la pièce équilibré pour savoir à quel jeu on joue
    if 'pile' in result:  # si pile dans la variable result
        result = game.jeuA()  # on joue au jeu A
        compteCapital(result)  # on met à jour le capital
    else:
        result = game.jeuB(game.capital)  # on joue au jeu B
        compteCapital(result)  # on met à jour le capital
print(compteCapital(result))

# Jeu Gagnant