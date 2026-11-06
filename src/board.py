class Board:
    def __init__(self):
        pass

    def set_piece(self, coord, color):
        pass

    def eval_score(self, color):
        pass

    def __getitem__(self, key):
        if not isinstance(key,slice):
            raise TypeError("L'accès doit être un slice.")
        pass