import random

class Borracho:

    def __init__(self, nombre):
        self.nombre = nombre


class BorrachoTradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):

        """Retorna una tupla.""" 
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])