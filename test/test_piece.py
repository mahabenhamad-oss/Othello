
from piece import Piece
from datatypes import Color


# TEST 1 : Création d'une pièce noire
piece = Piece(Color.BLACK)
assert piece.color == Color.BLACK
print("TEST 1 réussi : création d'une pièce noire")


# TEST 2 : Création d'une pièce blanche
piece = Piece(Color.WHITE)
assert piece.color == Color.WHITE
print("TEST 2 réussi : création d'une pièce blanche")


# TEST 3 : Vérification du flip noir vers blanc
piece = Piece(Color.BLACK)
piece.flip()
assert piece.color == Color.WHITE
print("TEST 3 réussi : flip noir vers blanc")


# TEST 4 : Vérification du flip blanc vers noir
piece.flip()
assert piece.color == Color.BLACK
print("TEST 4 réussi : flip blanc vers noir")


# TEST 5 : Vérification d'une couleur invalide
try:
    Piece("red")
    assert False, "Une erreur aurait dû être déclenchée."
except ValueError:
    print("TEST 5 réussi : rejet d'une couleur invalide")


print("\nTous les tests Piece sont réussis !")
