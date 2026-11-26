from abc import ABC, abstractmethod


class Exercicio(ABC):
    """Classe abstrata: define o que todo exercício tem (não pode ser instanciada)."""

    def __init__(self, nome, series, repeticoes, peso):
        self.__nome = nome
        # Usa os setters abaixo para já validar os valores
        self.series = series
        self.repeticoes = repeticoes
        self.peso = peso

    @property
    def nome(self):
        return self.__nome

    @property
    def series(self):
        return self.__series

    @series.setter
    def series(self, valor):
        if valor <= 0:
            raise ValueError("Séries devem ser maiores que zero.")
        self.__series = valor

    @property
    def repeticoes(self):
        return self.__repeticoes

    @repeticoes.setter
    def repeticoes(self, valor):
        if valor <= 0:
            raise ValueError("Repetições devem ser maiores que zero.")
        self.__repeticoes = valor

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, valor):
        if valor < 0:
            raise ValueError("Peso não pode ser negativo.")
        self.__peso = valor

    def volume(self):
        # Volume = total de carga movimentada (kg)
        return self.series * self.repeticoes * self.peso

    @abstractmethod
    def resumo(self):
        """Cada tipo de exercício mostra seus dados de um jeito (polimorfismo)."""
        pass

    def __str__(self):
        return self.resumo()


class ExercicioComPeso(Exercicio):
    """Exercício com carga externa: halter, barra, máquina."""

    def resumo(self):
        return f"{self.nome}: {self.series}x{self.repeticoes} com {self.peso:g} kg"


class ExercicioPesoCorporal(Exercicio):
    """Exercício com o próprio corpo (flexão, barra fixa). O peso é a carga extra."""

    def resumo(self):
        carga = f"peso corporal + {self.peso:g} kg" if self.peso > 0 else "peso corporal"
        return f"{self.nome}: {self.series}x{self.repeticoes} ({carga})"
