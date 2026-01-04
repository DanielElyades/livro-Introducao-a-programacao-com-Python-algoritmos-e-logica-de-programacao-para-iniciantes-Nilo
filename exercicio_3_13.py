# Exercício 3.13 Escreva um programa que converta uma temperatura digitada em
# °C em °F.

# Ler a temperatura
temperatura = float(input("Informe a temperatura em °C: "))

# Transformar a temperatura em °C para °F
f = ((9 * temperatura) / 5) + 32

# Imprimir a temperatura convertida em °F na tela
print(f"A temperatura em °F é: {f:.2f}")