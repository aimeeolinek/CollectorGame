from code.Entity import Entity

"""
    Classe que representa um coletável no jogo.
    Herda da classe Entity e lida com o comportamento específico do coletável,
    como a exibição da imagem e a detecção de colisão com o jogador."""
class Collectable(Entity):
    def __init__(self, pos):
        super().__init__("asset/Flower.png", pos, (32, 44))

    def update(self):
        pass  # Flower é estática