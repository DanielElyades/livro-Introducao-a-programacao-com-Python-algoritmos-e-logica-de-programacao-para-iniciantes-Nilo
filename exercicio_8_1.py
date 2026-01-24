# Exercício 8.1 Escreva uma função que retorne o maior de dois números.
# Valores esperados:
# máximo(5,6) == 6
# máximo(2,1) == 2
# máximo(7,7) == 7

# Definindo a função
def maior(a, b):
    if a > b:
        return a
    elif a == b:
        return a
    else:
        return b