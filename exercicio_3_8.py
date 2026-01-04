# Exercício 3.8 Escreva um programa que leia um valor em metros e o exiba con-
# vertido em milímetros.
# Ler um valor em metros
valor = float(input("Digite um valor em metros: "))
# Converter o valor em milímetros
valor_milimetros = valor * 1000
# Imprimir na tela
print(f"Valor convertido em milímetros: {valor_milimetros:.2f} mm")