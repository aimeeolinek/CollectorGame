from code.Collectable import Collectable
from code.Obstacle import Obstacle
from code.Flag import Flag
"""
    Classe que representa a fábrica de entidades do jogo.
    Responsável por criar instâncias de diferentes tipos de entidades,
    como coletáveis, obstáculos e bandeiras, com base no tipo fornecido.
"""
class EntityFactory:
    @staticmethod
    def create(entity_type, pos):
        if entity_type == "collectables":
            return Collectable(pos)
        elif entity_type == "obstacles":
            return Obstacle(pos)
        elif entity_type == "flags":
            return Flag(pos)
        else:
            raise ValueError(f"Tipo inválido: {entity_type}")
        
