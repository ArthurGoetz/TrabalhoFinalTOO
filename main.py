from model.semana import SemanaTreino
from model.treino import Treino
from model.fabrica import ExercicioFactory


def ler_indice(mensagem, total):
    # Lê um número de 1 a total e devolve o índice da lista (começa em 0)
    numero = int(input(mensagem))
    if not 1 <= numero <= total:
        raise ValueError("Número fora da lista.")
    return numero - 1


def escolher_treino(semana):
    treinos = semana.treinos
    if not treinos:
        print("Nenhum treino cadastrado.")
        return None
    for i, t in enumerate(treinos, 1):
        print(f"{i} - {t.nome}")
    return treinos[ler_indice("Número do treino: ", len(treinos))]


def criar_treino(semana):
    nome = input("Nome do treino (ex.: A - Peito, tríceps e ombro): ").strip()
    semana.adicionar_treino(Treino(nome))
    print("Treino criado!")


def adicionar_exercicio(semana):
    treino = escolher_treino(semana)
    if treino is None:
        return
    tipo = input("Tipo (1 - Com peso | 2 - Peso corporal): ")
    nome = input("Nome do exercício: ").strip()
    series = int(input("Séries: "))
    repeticoes = int(input("Repetições: "))
    peso = float(input("Peso em kg (0 se não houver): ").replace(",", "."))
    treino.adicionar(ExercicioFactory.criar(tipo, nome, series, repeticoes, peso))
    print("Exercício adicionado!")


def remover_exercicio(semana):
    treino = escolher_treino(semana)
    if treino is None:
        return
    if not treino.exercicios:
        print("Treino sem exercícios.")
        return
    print(treino)
    removido = treino.remover(ler_indice("Número do exercício: ", len(treino.exercicios)))
    print(f"{removido.nome} removido.")


def carregar_exemplo(semana):
    """Monta uma semana A/B/C de exemplo."""
    dados = {
        "A - Peito, tríceps e ombro": [
            ("1", "Supino reto", 4, 10, 30),
            ("1", "Tríceps corda", 3, 12, 20),
            ("1", "Desenvolvimento", 3, 10, 14),
            ("2", "Flexão", 3, 15, 0),
        ],
        "B - Dorsal e bíceps": [
            ("2", "Barra fixa", 4, 8, 5),
            ("1", "Remada curvada", 4, 10, 40),
            ("1", "Rosca direta", 3, 12, 12),
        ],
        "C - Perna completa": [
            ("1", "Agachamento", 4, 10, 60),
            ("1", "Leg press", 4, 12, 150),
            ("1", "Cadeira extensora", 3, 12, 40),
        ],
    }
    for nome, exercicios in dados.items():
        treino = Treino(nome)
        for ex in exercicios:
            treino.adicionar(ExercicioFactory.criar(*ex))
        semana.adicionar_treino(treino)
    print("Semana de exemplo carregada!")


def main():
    semana = SemanaTreino()
    opcoes = {
        "1": criar_treino,
        "2": adicionar_exercicio,
        "3": remover_exercicio,
        "4": lambda s: print(s),
        "5": carregar_exemplo,
    }
    while True:
        print("\n=== ACADEMIA ===")
        print("1 - Criar treino")
        print("2 - Adicionar exercício")
        print("3 - Remover exercício")
        print("4 - Ver semana")
        print("5 - Carregar semana de exemplo")
        print("0 - Sair")
        op = input("Opção: ").strip()
        if op == "0":
            break
        acao = opcoes.get(op)
        if acao is None:
            print("Opção inválida.")
            continue
        try:
            acao(semana)
        except (ValueError, IndexError, TypeError) as erro:
            print(f"Erro: {erro}")


main()
