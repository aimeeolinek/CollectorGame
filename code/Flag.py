from code.Entity import Entity

class Flag(Entity):
    def __init__(self, pos):
        super().__init__("asset/Flag.png", pos, (48, 48))

    def update(self):
        pass  # Bandeira é estática