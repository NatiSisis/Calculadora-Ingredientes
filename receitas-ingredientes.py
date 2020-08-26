ingredientes_parcial = []

app_rodando = True

while app_rodando:
	ingrediente_parcial = input("Qual o ingrediente: ")
	peso_parcial = input("Qual a quantidade utilizada deste ingrediente: ")

	id = 1

	if len(ingredientes_parcial) > 0:
		ultimoId = ingredientes_parcial[len(ingredientes_parcial) - 1]['id']
		id = ultimoId + 1

	ingrediente_parcial = {
		"id" : id,
		"Ingrediente" : ingrediente_parcial,
		"Quantidade Parcial" : peso_parcial,
		"Tempo de forno" : tempo_forno,
		"Tempo de cozimento" : tempo_cozimento,
		"Tempo de preparo" : tempo_preparo
	}

	ingredientes_parcial.append(ingrediente_parcial)

	print(ingredientes_parcial)
	deve_continuar = input("Cadastrar outro ingrediente? (S/n)")
	if deve_continuar.lower() == "n":
		print('Até mais')
		app_rodando = False
	elif deve_continuar.lower() != 's' and deve_continuar.strip() != '':
		print('Você digtou um valor errado, o app vai continuar')