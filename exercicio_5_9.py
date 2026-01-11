# Exercício 5.9 Escreva um programa que leia dois números. Imprima a divisão
# inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas
# os operadores de soma e subtração para calcular o resultado. Lembre-se de que
# podemos entender o quociente da divisão de dois números como a quantidade
# de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez
# que podemos subtrair 4 cinco vezes de 20.

# Ler o primeiro número
numero1 = int(input("Primeiro número: "))

# Ler o segundo número
numero2 = int(input("Segundo número: "))

# Calcular o resto
resto = numero1 % numero2

# Calcular a divisão
resultado = numero1 / numero2

# Definindo um contador
contador = 1

# Calcular usando while
while contador <= resultado:
    print(f"{numero2} +", end=" ")
    contador = contador + 1