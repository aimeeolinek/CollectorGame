from code.Entity import Entity

"""
    Classe que representa a bandeira no jogo.
    Responsável por gerenciar a lógica da bandeira, 
    incluindo a exibição da imagem e a detecção de colisão com o jogador.
"""
class Flag(Entity):
    def __init__(self, pos):
        super().__init__("asset/Flag.png", pos, (64, 64))

    def update(self):
        pass  # Bandeira é estática