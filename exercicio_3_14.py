# Exercício 3.14 Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
# o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por
# dia e R$ 0,15 por km rodado.

# Ler a quantidade de km percorridos 
km_percorridos = float(input("Informe a quantidade de km percorridos: "))

# Ler quantos dias o carro foi alugado
dias = int(input("Informe a quantidade de dias que o carro foi alugado: "))

# Calcular o preço a pagar
preco_pagar = (60 * dias) + (0.15 * km_percorridos)

# Imprimir o preço a pagar na tela
print(f"O preço a pagar é: {preco_pagar:.2f}")