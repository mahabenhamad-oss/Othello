
from piece import Piece
from datatypes import Color


# TEST 1 : Création d'une pièce noire
def test_create_black_piece():
    piece = Piece(Color.BLACK)

    assert piece.color == Color.BLACK


# TEST 2 : Création d'une pièce blanche
def test_create_white_piece():
    piece = Piece(Color.WHITE)

    assert piece.color == Color.WHITE


# TEST 3 : Vérification du flip noir vers blanc
def test_flip_black_to_white():
    piece = Piece(Color.BLACK)

    piece.flip()

    assert piece.color == Color.WHITE


# TEST 4 : Vérification du flip blanc vers noir
def test_flip_white_to_black():
    piece = Piece(Color.WHITE)

    piece.flip()

    assert piece.color == Color.BLACK


# TEST 5 : Vérification d'une couleur invalide
def test_invalid_color():
    try:
        Piece("red")
        assert False, "Une erreur aurait dû être déclenchée."
    except ValueError:
        pass
