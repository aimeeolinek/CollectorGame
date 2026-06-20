from code.Entity import Entity

class Collectable(Entity):
    def __init__(self, pos):
        super().__init__("asset/Flower.png", pos, (32, 44))

    def update(self):
        pass  # Flower é estática