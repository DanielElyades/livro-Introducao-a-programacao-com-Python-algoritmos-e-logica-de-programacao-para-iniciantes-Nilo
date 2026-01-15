# Exercício 5.14 Escreva um programa que leia números inteiros do teclado. O pro-
# grama deve ler os números até que o usuário digite 0 (zero). No final da execução,
# exiba a quantidade de números digitados, assim como a soma e a média aritmética.

# Definindo a variável soma e contador
contador = 0
soma = 0
# Ler os números e fazer os cálculos
while True:
    numeros = int(input("Informe um número inteiro: "))
    if numeros == 0:
        break

    soma = numeros + soma
    contador = contador + 1

media = soma / contador

# Imprimir os resultados na tela
print(f"Quantidade de números digitados: {contador:.2f}")
print(f"Soma dos números digitados: {soma:.2f}")
print(f"Média dos números digitados: {media:.2f}")