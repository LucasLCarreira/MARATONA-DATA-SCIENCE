# Crie um algoritmo que solicite ao usuário um número
# e apresente o fatorial deste número como resultado

n = int(input('Digite um número: '))
c = fat= 1
while c <= n:
    fat *= c
    c += 1
print(f'O fatorial de {n} é igual a {fat}!')