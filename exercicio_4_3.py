# Exercício 4.3 Escreva um programa que leia três números e que imprima o maior
# e o menor.

# Ler os três números
numeros = []
while len(numeros) < 3:
    numeros.append(int(input("Informe um número: ")))

# Imprime na tela o maior
print(f"O maior número é: {max(numeros)}")

# Imprime na tela o número maior
print(f"O menor número é: {min(numeros)}")

# Ler o primeiro número
numero1 = int(input("Primeiro número: "))
# Ler o segundo número
numero2 = int(input("Segundo número: "))
# Ler o terceiro número
numero3 = int(input("Terceiro número: "))

# Condicionais
if numero1 >= numero2 and numero1 >= numero3:
    maior = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    maior = numero2
else:
    maior = numero3
if numero1 <= numero2 and numero1 <= numero3:
    menor = numero1
elif numero2 <= numero1 and numero2 <= numero3:
    menor = numero2
else:
    menor = numero3

# Imprimir na tela o número maior
print(f"O maior número é: {maior:g}")

# Imprimir na tela o número menor
print(f"O número menor é: {menor:g}")