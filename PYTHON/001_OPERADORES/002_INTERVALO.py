# CRIE UM ALGORITMO QUE SOLICITE 2 NÚMEROS E APRESENTA O INTERVALO
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
if x > y:
    z = x - y
elif y >= x:
    z = y - x

print(f'O intervalo dos números é {z}.')
