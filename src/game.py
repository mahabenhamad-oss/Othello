import player as player
import board as board
from datatypes import Color
import config


class Game:
    def __init__(self):
        print('Othello de taille', config.BOARDSIZE)
        self._board = board.Board()
        
        # # ajouter les 4 pièces de départ
        # self._board.set_piece(color=Color.WHITE, coord=(3,3))
        # self._board.set_piece(color=Color.BLACK, coord=(3,4))
        # self._board.set_piece(color=Color.BLACK, coord=(4,3))
        # self._board.set_piece(color=Color.WHITE, coord=(4,4))


        self._players = (
            player.Player(Color.BLACK),
            player.Player(Color.WHITE),
            )

    @property
    def board(self):
        return self._board

    def start(self):
        color = Color.BLACK
        while self.turn(color):
            # incrémenter la couleur
            # %len(Color) est utilisé pour revenir à 0 après la dernière couleur,
            # si on ajoute une couleur le code fonctionnera encore
            color = Color.BLACK if color == Color.WHITE else Color.WHITE

    def turn(self, color):
        # todo: ajouter une fonction pour regarder si le coup est valide
        if color == Color.BLACK:
            current_player = self._players[0]
        else:
            current_player = self._players[1]
        move = current_player.get_move()
        self._board.set_piece(coord=move,color=color)

    def display_board(self):
        # self.board.display()
        raise NotImplementedError('Utiliser la fonction display de board après implémentation')