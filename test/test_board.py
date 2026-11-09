
from board import Board
from datatypes import Color


# TEST 1 : Vérifier les dimensions du plateau
def test_board_dimensions():
    board = Board()

    assert len(board.board) == 8
    assert len(board.board[0]) == 8

# TEST 2 : Vérifier la configuration initiale
def test_initial_configuration():
    board = Board()

    assert board[3, 3].color == Color.WHITE
    assert board[3, 4].color == Color.BLACK
    assert board[4, 3].color == Color.BLACK
    assert board[4, 4].color == Color.WHITE


# TEST 3 : Vérifier l'accès à une case vide
def test_empty_case():
    board = Board()

    assert board[0, 0] is None


# TEST 4 : Vérifier le placement d'une pièce
def test_set_piece():
    board = Board()

    board.set_piece((2, 3), Color.BLACK)

    assert board[2, 3].color == Color.BLACK


# TEST 5 : Vérifier le calcul des scores
def test_eval_score():
    board = Board()

    board.set_piece((2, 3), Color.BLACK)

    assert board.eval_score(Color.BLACK) == 3
    assert board.eval_score(Color.WHITE) == 2

