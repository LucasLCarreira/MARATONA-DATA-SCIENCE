# Em uma nova célula remova 1 Item chave/valor do dicionário criado anteriormente

dicionario = {'Nome':"Lucas",'Idade':'31','Curso':'ADS','Período': 'Noite'}
del dicionario['Período']
for k, v in dicionario.items():
    print(f'{k}: {v}')
