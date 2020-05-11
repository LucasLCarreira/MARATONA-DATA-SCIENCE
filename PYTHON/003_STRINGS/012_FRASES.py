# CRIE UMA LISTA VAZIA E RECEBA UM INPUT DE TRES FRASES
# ORDENE A LISTA EM ORDEM ALFABETICA DECRESCENTE
lista = []
lista.append(str(input('Digite a primeira frase: ')).upper())
lista.append(str(input('Digite a segunda frase: ')).upper())
lista.append(str(input('Digite a terceira frase: ')).upper())
print(sorted(lista, reverse=True))