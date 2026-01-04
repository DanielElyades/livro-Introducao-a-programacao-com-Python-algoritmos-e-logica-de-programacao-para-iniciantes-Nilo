# Exercício 3.15 Escreva um programa para calcular a redução do tempo de vida de
# um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos
# ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
# calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

# Ler a quantidade de de cigarros fumados num dia
cigarros = int(input("Informe a quantidade de cigarros fumados num dia: "))

# Ler a quantidade de anos que fumou
anos = int(input("Informe a quantidade de anos que fumou: "))

# Calcular a quantidade dias que o fumante perdeu
calculo_dias = (cigarros * anos * 365 * 10) / 1440

# Imprimir a quantidade de dias que a pessoa perdeu
print(f"A quantidade de dias que a pessoa perdeu foi: {calculo_dias:.0f}")