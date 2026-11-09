
class Piece:
    def __init__(self, color):
        if color not in ("black", "white"):
            raise ValueError("La couleur doit être black ou white.")

        self._color = color

    # Getter
    @property
    def color(self):
        return self._color

    # Retourner la pièce
    def flip(self):
        if self._color == "black":
            self._color = "white"
        else:
            self._color = "black"

    def __repr__(self):
        return f"Piece({self._color})"

    