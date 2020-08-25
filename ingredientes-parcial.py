ingredientesParcial = []

app_rodando = True

while app_rodando:
	ingredienteParcial = input("Qual o ingrediente: ")
	pesoParcial = input("Qual a quantidade utilizada deste ingrediente: ")
	#valorParcial = 

	id = 1

	if len(ingredientesParcial) > 0:
		ultimoId = ingredientesParcial[len(ingredientesParcial) - 1]['id']
		id = ultimoId + 1

	ingredienteParcial = {
		"id" : id,
		"Ingrediente" : ingredienteParcial,
		"Quanidade Parcial" : pesoParcial
	}

	ingredientesParcial.append(ingredienteParcial)

	print(ingredientesParcial)
	deve_continuar = input("Cadastrar outro cozinheiro? (S/n)")
	if deve_continuar.lower() == "n":
		print('Até mais')
		app_rodando = False
	elif deve_continuar.lower() != 's' and deve_continuar.strip() != '':
		print('Você digtou um valor errado, o app vai continuar')



