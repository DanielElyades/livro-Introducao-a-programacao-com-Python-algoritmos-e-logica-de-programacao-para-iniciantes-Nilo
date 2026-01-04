# Exercício 3.11 Faça um programa que solicite o preço de uma mercadoria e o per-
# centual de desconto. Exiba o valor do desconto e o preço a pagar.

# Ler o preço da mercadoria
preco = float(input("Informe o preço da mercadoria: "))

# Ler o percentual do desconto
porcentagem_desconto = float(input("Informe a porcentagem do desconto: "))

# Calcular o valor do desconto
valor_desconto = (preco * porcentagem_desconto) / 100

# Calcular o preço a pagar
preco_pagar = preco - valor_desconto

# Imprimir o valor do desconto na tela
print(f"O valor do desconto é: {valor_desconto:.2f}")

# Imprimir o preço a pagar na tela
print(f"O valor a pagar é: {preco_pagar:.2f}")