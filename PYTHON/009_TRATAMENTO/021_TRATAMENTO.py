# Crie um código em Python que solicite do usuário o input de um número inteiro.
# Caso haja preenchimento diferente, a máquina deve guiar o usuário até ajustar sua resposta.

while True:
    try:
        n = int(input('Digite um número inteiro: '))
    except Exception as erro:
        print(f'Erro: {erro}')
    except KeyboardInterrupt:
        print(f'Usuário interrompeu o programa!')
        break
    else:
        break