# Crie um novo dicionário, armazenando-o em uma nova variável
# e agora unifique este com outro dicionário criado anteriormente

aluno = {'Nome':"Lucas",'Idade':'31','Curso':'ADS','Período': 'Noite'}
escola = {'Universidade': 'FATEC', 'Campus': 'Zona Leste'}
dicionario = {}
dicionario.update(aluno)
dicionario.update(escola)
for k, v in dicionario.items():
    print(f'{k}: {v}')
