import game
import board
from datatypes import Color

def test_board_getter(monkeypatch):
    game1 = game.Game()

    def mock_getitem(_, key):
        print(f"Accès board {key}")
        return 42

    monkeypatch.setattr(board.Board, '__getitem__', mock_getitem)

    # getter de board appelé implicitement
    b = game1.board
    assert b[0,0] == 42

def test_game_start(monkeypatch):
    game1 = game.Game()
    global liste_couleurs_tours
    liste_couleurs_tours = []
    
    def mock_turn(_, color):
        print(f"Jeu tour {color}")
        global liste_couleurs_tours
        if len(liste_couleurs_tours)<42:
            liste_couleurs_tours.append(color)
            return True
        else:
            return False
    
    monkeypatch.setattr(game.Game, 'turn', mock_turn)
    
    game1.start()
    # Vérifier l'alternance des couleurs
    assert liste_couleurs_tours == [Color.BLACK, Color.WHITE]*21

def test_game_turn(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda : "a1")

    game1 = game.Game()
    game1.turn(color=Color.BLACK)