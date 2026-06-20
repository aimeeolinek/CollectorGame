from code.Collectable import Collectable
from code.Obstacle import Obstacle
from code.Flag import Flag

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
        
