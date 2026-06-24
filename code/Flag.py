from code.Entity import Entity

class Flag(Entity):
    """
    Representa a bandeira que marca o objetivo da fase.

    Herda da classe Entity e define a aparência e a posição
    do ponto de chegada do jogador.
    """
    def __init__(self, pos):
        super().__init__("asset/Flag.png", pos, (64, 64))

    def update(self):
        """
        Não realiza atualizações, pois a bandeira é estática.
        """
        pass  