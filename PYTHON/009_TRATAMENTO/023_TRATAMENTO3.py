# Crie um código em Python que peça um número ímpar do usuário.
# Caso o número seja par, apresente mensagem guiando o usuário até o preenchimento correto

while True:
    try:
        x = int(input('Digite um número ímpar: '))
        if x % 2 == 0:
            print('\033[1;31mERRO: Digite um número ímpar!\033[m')
        else:
            print(f'\033[1;31mVocê digitou o número {x}\033[m')
            break
    except Exception as erro:
        print(f'ERRO: {erro}')

