# Exercício 4.8 Escreva um programa que leia dois números e que pergunte qual
# operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-),
# multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

# Ler o primeiro número
numero1 = float(input("Digite o primeiro número: "))

# Ler o segundo número
numero2 = float(input("Digite o segundo número: "))

# Perguntar qual operação vai executar
operacao = input("Digite '*' para multiplicação, '/' para divisão, '+' para adição e '-' para subtração: ")

# Condicionais para definir qual operação
if operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    resultado = numero1 / numero2
elif operacao == '+':
    resultado = numero1 + numero2
else:
    resultado = numero1 - numero2

# Imprimir o resultado na tela
print(f"O resultado é: {resultado:g}")