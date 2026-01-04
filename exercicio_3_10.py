# Exercício 3.10 Faça um programa que calcule o aumento de um salário. Ele deve
# solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
# e do novo salário.

# Ler o valor do salário 
salario = float(input("Imforme o valor do salário: "))
# Ler a porcentagem do aumento
porcentagem_aumento = float(input("Informe a porcentagem do aumento: "))
# Calcular o valor do aumento
valor_aumento = (salario * porcentagem_aumento) / 100
# Calcular o novo salário
novo_salario = salario + valor_aumento 
# Imprimir valor do aumento
print(f"O valor do aumento é: {valor_aumento:.2f}")
# Imprimir o valor do novo salário
print(f"O valor do novo salário é: {novo_salario:.2f}")