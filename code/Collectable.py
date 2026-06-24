from code.Entity import Entity

class Collectable(Entity):
    """
    Representa um item coletável do jogo.

    Herda da classe Entity e define a aparência e a posição
    dos objetos que podem ser coletados pelo jogador para
    aumentar sua pontuação.
    """
    def __init__(self, pos):
        super().__init__("asset/Flower.png", pos, (32, 44))

    def update(self):
        """
        Não realiza atualizações, pois o coletável é estático.
        """
        pass  