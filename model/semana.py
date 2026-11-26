from model.treino import Treino


class SemanaTreino:
    """Singleton: existe uma única semana de treinos no sistema."""

    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.__treinos = []
        return cls._instancia

    @property
    def treinos(self):
        return list(self.__treinos)

    def adicionar_treino(self, treino):
        if not isinstance(treino, Treino):
            raise TypeError("Só é possível adicionar treinos.")
        self.__treinos.append(treino)

    def remover_treino(self, indice):
        return self.__treinos.pop(indice)

    def __str__(self):
        if not self.__treinos:
            return "Nenhum treino cadastrado na semana."
        return "\n\n".join(str(t) for t in self.__treinos)
