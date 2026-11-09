
from piece import Piece

# TEST 1 : Création d'une pièce noire
piece_black = Piece("black")
assert piece_black.color == "black"
print("TEST 1 réussi : création d'une pièce noire")

# TEST 2 : Création d'une pièce blanche
piece_white = Piece("white")
assert piece_white.color == "white"
print("TEST 2 réussi : création d'une pièce blanche")

# TEST 3 : Retourner une pièce noire en blanche
piece_black.flip()
assert piece_black.color == "white"
print("TEST 3 réussi : flip black -> white")

# TEST 4 : Retourner une pièce blanche en noire
piece_white.flip()
assert piece_white.color == "black"
print("TEST 4 réussi : flip white -> black")

# TEST 5 : Retourner deux fois une pièce
piece_black.flip()
piece_black.flip()
assert piece_black.color == "white"
print("TEST 5 réussi : deux retournements")

print("\nTous les tests Piece sont réussis !")
