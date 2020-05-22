# Crie um código em Python que solicite do usuário o input de 2 números inteiros
# e assim divida o primeiro número pelo segundo.
# Caso o input não seja um número inteiro,
# seu código deve guiar o usuário até o preenchimento correto.
# Caso o usuário preencha com 0, que apresente mensagem falando sobre a indivisibilidade por zero.
# Caso o usuário não digite um número, informar que um número deve ser digitado.
# Em outros casos de erro, apresente ao usuário uma mensagem de erro inesperado.

while True:
    try:
        x = int(input('Digite o numerador: '))
    except ValueError:
        print(f'Erro: Digite o um valor numérico inteiro!')
    except TypeError:
        print(f'Erro: Digite o um valor numérico inteiro!')
    except KeyboardInterrupt:
        print('O usuário interrompeu o programa!')
        break
    except Exception as erro:
        print(f'Erro: {erro}')
    else:
        while True:
            try:
                y = int(input('Digite o denominador: '))
                z = x / y
            except ValueError:
                print(f'Erro: Digite o um valor numérico inteiro!')
            except TypeError:
                print(f'Erro: Digite o um valor numérico inteiro!')
            except KeyboardInterrupt:
                print('O usuário interrompeu o programa!')
                break
            except ZeroDivisionError:
                print('O denominador não pode ser ZERO!')
            except Exception as erro:
                print(f'Erro: {erro}')
            else:
                print(f'A divisão de {x} por {y} é igual a {z}!')
                break
        break

