from code.Collectable import Collectable
from code.Obstacle import Obstacle
from code.Flag import Flag

class EntityFactory:
    """
    Classe responsável pela criação de entidades do jogo.

    Centraliza a instanciação de coletáveis, obstáculos e bandeiras,
    retornando o objeto correspondente ao tipo informado.
    """
    @staticmethod
    def create(entity_type, pos):
        """
        Cria e retorna uma entidade de acordo com o tipo informado.
        Args:
            entity_type (str): Tipo da entidade a ser criada.
            pos (tuple): Posição inicial da entidade.
        Returns:
            Entity: Instância da entidade correspondente.
        Raises:
            ValueError: Se o tipo informado não for válido.
        """
        if entity_type == "collectables":
            return Collectable(pos)
        elif entity_type == "obstacles":
            return Obstacle(pos)
        elif entity_type == "flags":
            return Flag(pos)
        else:
            raise ValueError(f"Tipo inválido: {entity_type}")
        
