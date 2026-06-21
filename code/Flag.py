from code.Entity import Entity

class Flag(Entity):
    def __init__(self, pos):
        super().__init__("asset/Flag.png", pos, (64, 64))

    def update(self):
        pass  # Bandeira é estática