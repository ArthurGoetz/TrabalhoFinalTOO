from model.exercicio import ExercicioComPeso, ExercicioPesoCorporal


class ExercicioFactory:
    """Factory: centraliza a criação dos exercícios a partir de um tipo."""

    TIPOS = {
        "1": ExercicioComPeso,
        "2": ExercicioPesoCorporal,
    }

    @staticmethod
    def criar(tipo, nome, series, repeticoes, peso=0):
        classe = ExercicioFactory.TIPOS.get(tipo)
        if classe is None:
            raise ValueError("Tipo de exercício inválido.")
        return classe(nome, series, repeticoes, peso)
