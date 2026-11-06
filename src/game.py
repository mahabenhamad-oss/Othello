import player
import board
import datatypes
import config


class Game:
    def __init__(self):
        print('Othello de taille', config.BOARDSIZE)
        self._board = board.Board()
        self._players = (
            player.Player(datatypes.Color.BLACK),
            player.Player(datatypes.Color.WHITE),
            )
        
    def start(self):
        pass

    def turn(self, color):
        pass

    def display_board(self):
        pass