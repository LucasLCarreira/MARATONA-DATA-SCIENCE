# Crie um algoritmo que receba 3 números como input do usuário
# e a seguir adicione-o dentro de um frozenset.
# Ao término, aplique algum atributo frozenset e printe na tela.
# Utilize dir(frozenset) para selecionar o atributo.

lista = list()
for x in range(1,4):
    lista.append(input(f'Digite o {x}º valor: '))
frozen = frozenset(lista)
y = 5
print(frozenset.copy(frozen))