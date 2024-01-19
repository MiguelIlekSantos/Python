points = 0
questions = [
    "Qual linguagem de programação é conhecida por sua simplicidade e legibilidade?",
    "Em programação web, qual framework é amplamente utilizado para o desenvolvimento de inteárfaces de usurio interativas?",
    "O que é um loop em programação?",
    "Qual é a principal função do Git em desenvolvimento de software?",
    "O que é um bug em programação?"
]

alternativesOne = ['Python', 'Java', 'C']
alternativesTwo = ['React', 'Bootstrap', 'Django']
alternativesThree = ['Uma função matemática', 'Uma estrutura de controle de fluxo', 'Um tipo de variável']
alternativesFour = ['Gerenciar bancos de dados', 'Criar interfaces de usuário', 'Controlar versões de código-fonte']
alternativesFive = ["Um tipo de linguagem de programação", "Uma ferramenta de depuração", "Um erro ou falha no código"]

answerNumbers = [1,1,2,3,3]

alternativesGeneral = [alternativesOne, alternativesTwo, alternativesThree, alternativesFour, alternativesFive]
game = True

while game:
    for i in range(0, 5):
        print(questions[i])
        for a in range(0, 3):
            print(a + 1, "-", alternativesGeneral[i][a])
        answer = int(input("Answer : "))
        if answer == answerNumbers[i]:
            points += 10
            print("Correto")
        else:
            print("Errado Respota Creto: {}".format(answerNumbers[i]))

    print("Seu total de pontos = ", points)
    print("Quer jogar outra vez ?")
    stat = input("If want stop (n) else (y) : ").upper()
    if stat == "N":
        game = False
    else:
        game = True
