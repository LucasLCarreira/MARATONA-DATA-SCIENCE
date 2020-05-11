Frase = str(input('\nDigite uma frase: ')).strip().upper()
palavras = Frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print(inverso)
if inverso == junto:
    print('É palíndromo!')
else:
    print('Não é palíndromo!')