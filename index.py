'''
CALCULADORA DE INGREDIENTES

Cadastro de cozinheiro
valor hora

Cadastrar ingredientes
Qtd pagou, Qtd peso

Cadastro de receita
Ingredientes, qtd
tempo de forno
tempo de cozimento
tempo de trabalho
'''

cozinheiros = []

app_rodando = True

while app_rodando:
    nome = input("Qual o nome do cozinheiro: ")
    valor_hora = input("Qual o valor por hora do cozinheiro: ")

    id = 1

    if len(cozinheiros) > 0:
        ultimo_id = cozinheiros[len(cozinheiros) - 1]['id']
        id = ultimo_id + 1

    cozinheiro = {
        "id": id,
        "nome": nome,
        "valor_hora": valor_hora
    }

    cozinheiros.append(cozinheiro)

    print(cozinheiros)
    deve_continuar = input("Cadastrar outro cozinheiro? (S/n)")
    if deve_continuar.lower() == "n":
        print('Até mais')
        app_rodando = False
    elif deve_continuar.lower() != 's' and deve_continuar.strip() != '':
        print('Você digtou um valor errado, o app vai continuar')
