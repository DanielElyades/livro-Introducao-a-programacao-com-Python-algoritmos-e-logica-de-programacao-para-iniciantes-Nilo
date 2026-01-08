# Exercício 4.9 Escreva um programa para aprovar o empréstimo bancário para
# compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
# salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
# superior a 30% do salário. Calcule o valor da prestação como sendo o valor da
# casa a comprar dividido pelo número de meses a pagar.

# Ler o valor da casa
valor = float(input("Qual o valor da casa? "))

# Ler o valor do salário
salario = float(input("Qual o valor do salário? "))

# Ler quantos anos para ser pagos
anos = int(input("Quantos anos para pagar? "))

# Define o número de parcelas
parcelas = anos * 12

# Define o valor das parcelas
valor_parcelas = valor / parcelas

# Define os 30% do salário
porcento = 30 * salario / 100

# Condicional que define até 30% do salário
if valor_parcelas > porcento:
    print("O empréstimo foi negado")