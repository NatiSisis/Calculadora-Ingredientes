tempos_parcial = []

app_rodando = True

while app_rodando:
	tempo_forno = input("Qual o tempo de forno(em minutos): ")
	tempo_cozimento = input("Qual o tempo de cozimento(em minutos): ")
	tempo_preparo = input("Qual o tempo de preparo manual(em minutos): ")
	#valorParcial = 
	'''considerar tempo para outros equipamentos para padarias, aba de configuração de insumos, como tamanho
	do botijão, consumo do fogao/forno industrial, batedeiras, masseiras.. '''
	id = 1

	if len(tempos_parcial) > 0:
		ultimoId = tempos_parcial[len(tempos_parcial) - 1]['id']
		id = ultimoId + 1

	tempo_parcial = {
		"id" : id,
		"Tempo de forno" : tempo_forno,
		"Tempo de cozimento" : tempo_cozimento,
		"Tempo de preparo" : tempo_preparo
	}

	tempos_parcial.append(tempo_parcial)

	print(tempos_parcial)
	deve_continuar = input("Cadastrar outro tempo? (S/n)")
	if deve_continuar.lower() == "n":
		print('Até mais')
		app_rodando = False
	elif deve_continuar.lower() != 's' and deve_continuar.strip() != '':
		print('Você digtou um valor errado, o app vai continuar')