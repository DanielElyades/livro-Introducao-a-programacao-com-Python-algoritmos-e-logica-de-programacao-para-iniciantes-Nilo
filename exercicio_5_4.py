# Exercício 5.4 Modifique o programa anterior para imprimir de 1 até o número
# digitado pelo usuário, mas, dessa vez, apenas os números ímpares.

# Definindo o valor de x
x = 0
# Ler o número final da contagem
fim = int(input("Digite o último número a imprimir: "))

# Bloco while
while x <= fim:
    if x % 2 != 0:
        print(x)
    x = x + 1
