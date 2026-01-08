# Exercício 4.10 Escreva um programa que calcule o preço a pagar pelo fornecimento
# de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de insta-
# lação: R para residências, I para indústrias e C para comércios. Calcule o preço a
# pagar de acordo com a tabela a seguir.

# Ler a quantidade de kwh consumida
energia = float(input("Qual a quantidade de energia em KWh consumida? "))

# Ler o tipo de instalação
tipo = input("Qual o tipo de instalação? 'R' para residências, 'I' para industrias e 'C' para comercios: " )

# Condicionais para os tipos de consumo e os cálculos
if tipo == 'R' and energia <= 500:
    resultado = energia * 0.40
elif tipo == 'R' and energia > 500:
    resultado = energia * 0.65
if tipo == 'C' and energia <= 1000:
    resultado = energia * 0.55
elif tipo == 'C' and energia > 1000:
    resultado = energia * 0.60
if tipo == 'I' and energia <= 5000:
    resultado = energia * 0.55
elif tipo == 'I' and energia > 5000:
    resultado = energia * 0.60

# Imprime o valor para pagar na tela
print(f"O valor da conta é: {resultado:g}")