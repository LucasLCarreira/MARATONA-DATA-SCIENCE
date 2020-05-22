# Crie um algoritmo que pede ao usuário para digitar 3 números, diferentes entre sí, um de cada vez.
# A cada input do usuário insira o input dentro de um set e ao término printe na tela o output de seu set.

set = set()
for x in range(1,4):
    n = int(input(f'Digite o {x}º valor: '))
    set.add(n)
print(f'O Set é {set}!')
