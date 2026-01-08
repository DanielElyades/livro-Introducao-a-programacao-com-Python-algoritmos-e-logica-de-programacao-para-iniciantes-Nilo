# Exercício 4.4 Escreva um programa que pergunte o salário do funcionário e calcule
# o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de
# 10%. Para os inferiores ou iguais, de 15%.

# Ler o valor do salário
salario = float(input("Qual o valor do salário? "))

# Cálculo usando condicionais
if salario <= 1250:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10

# Adiciona o aumento ao salário
salario = salario + aumento

# Valor do aumento
print(f"Valor do aumento: {aumento:g}")

# Imprimir na tela o valor do salario com reajuste
print(f"O salário com aumento é: {salario:g}")