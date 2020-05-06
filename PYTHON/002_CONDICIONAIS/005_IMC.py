peso = float(input('Digite o peso (kg): '))
altura = float(input('Digite a altura (m): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}. Status: Abaixo do peso.')
elif imc < 25:
    print(f'Seu IMC é {imc:.2f}. Status: Peso normal.')
elif imc < 30:
    print(f'Seu IMC é {imc:.2f}. Status: Sobrepeso.')
elif imc < 35:
    print(f'Seu IMC é {imc:.2f}. Status: Obesidade grau 1.')
elif imc < 40:
    print(f'Seu IMC é {imc:.2f}. Status: Obesidade grau 2.')
else:
    print(f'Seu IMC é {imc:.2f}. Status: Obesidade grau 3.')
