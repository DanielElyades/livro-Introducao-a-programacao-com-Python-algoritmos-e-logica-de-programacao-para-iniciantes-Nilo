# Exercício 5.22 Escreva um programa que exiba uma lista de opções (menu): adição,
# subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida.
# Repita até que a opção saída seja escolhida.

# Definindo o contador
contador = 1
# Ler a opção do menu
menu = input("Menu: '+' adição, '-' subtração, '*' multiplicação, '/' divisão e 'sair' para sair: ")
numero = int(input("Digite o número da tabuada: "))

if menu == '+':
    while contador <= 10:
        print(f"{numero} + {contador} = {numero + contador}")
        contador += 1

if menu == '-':
    while contador <= 10:
        print(f"{numero} - {contador} = {numero - contador}")
        contador += 1

if menu == '*':
    while contador <= 10:
        print(f"{numero} * {contador} = {numero * contador}")
        contador += 1

if menu == '/':
    while contador <= 10:
        print(f"{numero} / {contador} = {numero / contador}")
        contador += 1

if menu == 'sair' or menu == 'Sair' or menu == 'SAIR':
    print("Operação finalizada")
    