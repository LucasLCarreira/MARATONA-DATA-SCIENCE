# CRIE UM ALGORITMO QUE SOLICITE 2 NÚMEROS E APRESENTA O MMC
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
mmc = 1
auxx = x
auxy = y
d = 2
while True:
    while True:
        if auxx % d == 0 and auxy % d == 0:
            auxx /= d
            auxy /= d
            mmc *= d
        elif auxx % d == 0:
            auxx /= d
            mmc *= d
        elif auxy % d == 0:
            auxy /= d
            mmc *= d
        else:
            d += 1
            break
    if auxx == 1 and auxy == 1:
        break
print(f'O MMC de {x} e {y} é {mmc}.')