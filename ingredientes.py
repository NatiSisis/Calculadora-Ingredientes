'''
CALCULADORA DE INGREDIENTES

Cadastro de ingrediente
valor hora

Cadastrar ingredientes
Qtd pagou, Qtd peso

Cadastro de receita
Ingredientes, qtd
tempo de forno
tempo de cozimento
tempo de trabalho
'''

ingredientes = []

app_rodando = True

while app_rodando:
    ingrediente = input("Qual o ingrediente: ")
    peso_inicial = input("Qual o peso do ingrediente quando adquirido(em gramas): ")
    valor_inicial = input("Qual o valor do ingrediente quando adquirido: ")

    id = 1

    if len(ingredientes) > 0:
        ultimo_id = ingredientes[len(ingredientes) - 1]['id']
        id = ultimo_id + 1

    ingrediente = {
        "id": id,
        "ingrediente": ingrediente,
        "peso_inicial": peso_inicial,
        "valor_inicial": valor_inicial
    }

    ingredientes.append(ingrediente)

    print(ingredientes)
    deve_continuar = input("Cadastrar outro ingrediente? (S/n)")
    if deve_continuar.lower() == "n":
        print('Até mais')
        app_rodando = False
    elif deve_continuar.lower() != 's' and deve_continuar.strip() != '':
        print('Você digtou um valor errado, o app vai continuar')
