from board import Board

# Création du plateau
board = Board()

# TEST 1 : Vérifier les dimensions du plateau
assert len(board.board) == 8
assert len(board.board[0]) == 8
print("TEST 1 réussi : plateau 8x8")

# TEST 2 : Vérifier la configuration initiale
assert board[3, 3].color == "white"
assert board[3, 4].color == "black"
assert board[4, 3].color == "black"
assert board[4, 4].color == "white"
print("TEST 2 réussi : configuration initiale")

# TEST 3 : Vérifier l'accès à une case vide
assert board[0, 0] is None
print("TEST 3 réussi : accès à une case vide")

# TEST 4 : Vérifier le placement d'une pièce
board.set_piece((2, 3), "black")
assert board[2, 3].color == "black"
print("TEST 4 réussi : placement d'une pièce")

# TEST 5 : Vérifier le calcul des scores
assert board.eval_score("black") == 3
assert board.eval_score("white") == 2
print("TEST 5 réussi : calcul des scores")

print("\nTous les tests Board sont réussis !")

