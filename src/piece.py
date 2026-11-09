
from datatypes import Color


class Piece:
    def __init__(self, color: Color):
        if not isinstance(color, Color):
            raise ValueError("La couleur doit être Color.BLACK ou Color.WHITE.")

        self._color = color

    # Getter
    @property
    def color(self):
        return self._color

    # Retourner la pièce
    def flip(self):
        if self._color == Color.BLACK:
            self._color = Color.WHITE
        else:
            self._color = Color.BLACK

    def __repr__(self):
        return f"Piece({self._color.name})"


    