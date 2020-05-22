# Insira 5 números e no final mostre o maior e o menor
lista = []
for l in range(0,5):
    lista.append(int(input('Digite um número: ')))
print(f'Menor: {min(sorted(lista))}\n'
      f'Maior: {max(sorted(lista))}')
