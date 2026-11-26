# Sistema de Academia
Trabalho prático da disciplina de Tecnologia Orientada a Objetos (TOO).

## Tema e objetivo
Sistema de console para montar a **semana de treinos** de academia. O usuário cria os treinos da semana (ex.: `A - Peito, tríceps e ombro`, `B - Dorsal e bíceps`, `C - Perna completa`) e escolhe os exercícios de cada um. Cada exercício tem **séries, repetições e peso**.

## Estrutura
main.py              # Menu
model/
    exercicio.py     # Classe abstrata (abstração), classes ExercicioComPeso, ExercicioPesoCorporal (herança).
    fabrica.py       # Factory Method
    treino.py        
    semana.py        # Singleton

## Classes

| Classe | Descrição |
|---|---|
| `Exercicio`| Classe **abstrata** base. Guarda nome, séries, repetições e peso, valida os valores e calcula o volume (`séries x repetições x peso`). Define o método abstrato `resumo()`. |
| `ExercicioComPeso` | Herda de `Exercicio`. Exercício com carga externa (barra, halter, máquina). Ex.: `Supino reto: 4x10 com 30 kg`. |
| `ExercicioPesoCorporal` | Herda de `Exercicio`. Exercício com o próprio corpo. O peso é a carga extra (opcional). Ex.: `Barra fixa: 4x8 (peso corporal + 5 kg)`. |
| `Treino` | Tem um nome e uma lista de exercícios. Permite adicionar e remover exercícios e calcula o volume total do treino. |
| `SemanaTreino` | Guarda todos os treinos da semana. É um **Singleton**: só existe uma instância no sistema. |
| `ExercicioFactory` | **Factory**: cria o tipo correto de exercício a partir da opção escolhida pelo usuário. |

## Pilares da POO

- **Abstração:** `Exercicio` é uma classe abstrata (`ABC`) com o método abstrato `resumo()`. Ela define o que todo exercício precisa ter e não pode ser instanciada.
- **Encapsulamento:** os atributos são privados (`__nome`, `__series`, `__peso`, `__exercicios` etc.) e o acesso é feito por `@property`. Os setters validam os dados: séries e repetições precisam ser maiores que zero e o peso não pode ser negativo. As listas de `Treino` e `SemanaTreino` são devolvidas como cópia, então não podem ser alteradas por fora.
- **Herança:** `ExercicioComPeso` e `ExercicioPesoCorporal` herdam atributos, validações e o cálculo de volume de `Exercicio`.
- **Polimorfismo:** cada subclasse implementa `resumo()` do seu jeito. O `Treino` percorre a lista chamando `resumo()` (via `__str__`) sem precisar saber o tipo de cada exercício.

## Padrões de projeto

### Factory
`ExercicioFactory.criar(tipo, nome, series, repeticoes, peso)` recebe o tipo (`"1"` = com peso, `"2"` = peso corporal) e devolve o objeto da classe certa. Assim o `main.py` não precisa conhecer as subclasses nem ter `if/else` para escolher qual criar. Para adicionar um novo tipo de exercício, basta criar a classe e registrá-la no dicionário `TIPOS` da fábrica.

### Singleton
`SemanaTreino` sobrescreve `__new__` para que toda chamada `SemanaTreino()` devolva **a mesma instância**. Isso garante que exista uma única semana de treinos no sistema, acessível de qualquer lugar sem criar cópias com dados diferentes.

## Funcionalidades

1. Criar treino (ex.: `A - Peito, tríceps e ombro`)
2. Adicionar exercício a um treino (tipo, nome, séries, repetições e peso)
3. Remover exercício de um treino
4. Ver a semana completa, com o volume total de cada treino
5. Carregar uma semana de exemplo (treinos A, B e C)
0. Sair

Entradas inválidas (texto no lugar de número, séries zeradas, peso negativo, opção fora da lista) mostram uma mensagem de erro e o programa continua.

## Execução e testes

É necessário ter o Python 3 instalado. Dentro da pasta `SistemaAcademia`:

```bash
python main.py
```

Para testar rapidamente, escolha a opção **5** (carrega a semana A/B/C de exemplo) e depois a **4** (mostra a semana). Em seguida, use as opções 1 a 3 para criar treinos e adicionar ou remover exercícios.

## Detalhamento de Aprendizado

- **Dificuldades encontradas:** Aplicar o padrão de projeto, pra mim foi difícil entender de forma objetiva em que situações devo aplicar cada padrão de projeto. Sintaxe do python, como não tenho costume de usar essa linguagem, a falta de conhecimento de algumas ferramentas do python atrapalha um pouco.
- **Como resolvi:** Tentei pensar em situações hipotéticas que poderiam ocorrer e não fariam sentido, como no caso de haver 2 semanas de treino, sendo que geralmente a semana se repete. Sobre a sintaxe da linguagem, a IA auxiliou com isso.
- **Principal aprendizado:** A utilização de uma ferramenta se torna fácil quando surge a necessidade de utilizá-la para corrigir um problema, e não o contrário.

## Declaração de Uso de IA

- **Ferramenta e modelo:** Claude Code, modelo Claude Opus 5.5.
- **Partes em que foi usada:** estruturação das classes, implementação do código (classes, padrões Factory e Singleton, menu), escrita do README.
- **Aprendizado com o uso:** É necessário uma supervisão sobre o projeto com a utilização da IA. É importante saber exatamente o que pretende fazer, para não criar complexidade desnecessária. Também, ao utilizar IA, a estrutura base e o corpo do projeto devem ser muito bem definidos pelo desenvolvedor.
