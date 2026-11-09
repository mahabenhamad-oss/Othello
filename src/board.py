from piece import Piece
from datatypes import Color


class Board:
    def __init__(self):
        # Création du plateau 8x8
        self.board = [[None for _ in range(8)] for _ in range(8)]

        # Configuration initiale d'Othello
        self.board[3][3] = Piece(Color.WHITE)
        self.board[3][4] = Piece(Color.BLACK)
        self.board[4][3] = Piece(Color.BLACK)
        self.board[4][4] = Piece(Color.WHITE)

    def set_piece(self, coord, color: Color):
        # Récupérer les coordonnées
        row, col = coord

        # Vérifier les coordonnées
        if not (0 <= row < 8 and 0 <= col < 8):
            raise ValueError("Coordonnées hors du plateau.")

        # Vérifier la couleur
        if not isinstance(color, Color):
            raise ValueError("Couleur invalide.")

        # Vérifier si la case est libre
        if self.board[row][col] is not None:
            raise ValueError("Cette case est déjà occupée.")

        # Créer et placer la pièce
        self.board[row][col] = Piece(color)

    def eval_score(self, color: Color):
        # Calculer le score d'une couleur
        if not isinstance(color, Color):
            raise ValueError("Couleur invalide.")

        score = 0

        for row in self.board:
            for piece in row:
                if piece is not None and piece.color == color:
                    score += 1

        return score

    def __getitem__(self, key):
        # Accéder à une case avec deux coordonnées
        if isinstance(key, tuple):
            if len(key) != 2:
                raise TypeError("Deux coordonnées sont nécessaires.")

            row, col = key
            return self.board[row][col]

        # Accéder à une ligne
        if isinstance(key, int):
            return self.board[key]

        raise TypeError("L'accès doit être un entier ou un tuple.")

    def display(self):
        # Symboles des pièces
        BLACK = "●"
        WHITE = "○"
        EMPTY = " "

        # Couleurs du terminal
        GREEN = "\033[42m"
        RESET = "\033[0m"

        # En-tête des colonnes
        print("\n     0   1   2   3   4   5   6   7")
        print("   +" + "---+" * 8)

        for i, row in enumerate(self.board):
            print(f" {i} |", end="")

            for piece in row:
                if piece is None:
                    symbol = EMPTY
                elif piece.color == Color.BLACK:
                    symbol = BLACK
                else:
                    symbol = WHITE

                # Affichage de chaque case
                print(f"{GREEN} {symbol} {RESET}|", end="")

            print()
            print("   +" + "---+" * 8)

