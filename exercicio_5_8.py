# Exercício 5.8 Escreva um programa que leia dois números. Imprima o resultado da
# multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
# subtração para calcular o resultado. Lembre-se de que podemos entender a mul-
# tiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5
# + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

# Leitura dos dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = 0
contador = 1
contador2 = 1

# Calculo do primeiro número
while contador <= num2:
    print(f"{num1} +", end=" ")
    contador = contador + 1
print(" ")
while contador2 <= num1:
    print(f"{num2} +", end=" ")
    contador2 = contador2 + 1