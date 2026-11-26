from model.exercicio import Exercicio


class Treino:
    """Um treino (ex.: 'A - Peito, tríceps e ombro') é composto de vários exercícios."""

    def __init__(self, nome):
        self.__nome = nome
        self.__exercicios = []

    @property
    def nome(self):
        return self.__nome

    @property
    def exercicios(self):
        # Retorna uma cópia para a lista não ser alterada por fora
        return list(self.__exercicios)

    def adicionar(self, exercicio):
        if not isinstance(exercicio, Exercicio):
            raise TypeError("Só é possível adicionar exercícios.")
        self.__exercicios.append(exercicio)

    def remover(self, indice):
        return self.__exercicios.pop(indice)

    def volume_total(self):
        return sum(e.volume() for e in self.__exercicios)

    def __str__(self):
        texto = f"Treino {self.nome}"
        if not self.__exercicios:
            return texto + "\n  (sem exercícios)"
        for i, e in enumerate(self.__exercicios, 1):
            texto += f"\n  {i}. {e}"  # chama resumo() de cada tipo
        return texto + f"\n  Volume total: {self.volume_total():g} kg"
