# Exercício 8.4 Escreva uma função que receba a base e a altura de um triângulo e
# retorne sua área (A = (base x altura)/2).
# Valores esperados:
# área_triângulo(6, 9) == 27
# área_triângulo(5, 8) == 20

# Definindo a função
def area(base, altura):
    return (base * altura) / 2

print(area(6, 9))
print(area(5, 8))