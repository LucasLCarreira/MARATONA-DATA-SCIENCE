# Crie um algoritmo que solicite ao usuário 3 números e printe na tela a média destes
soma = 0
for nota in range (1, 4):
    n = float(input(f'Digite a nota {nota}: '))
    soma += n
print(f'A média é {soma/3:.2f}.')