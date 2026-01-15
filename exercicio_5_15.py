# Exercício 5.15 Escreva um programa para controlar uma pequena máquina registra-
# dora. Você deve solicitar ao usuário que digite o código do produto e a quantidade

# comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto:

# Código Preço
# 1 0,50
# 2 1,00
# 3 4,00
# 5 7,00
# 9 8,00

# Seu programa deve exibir o total das compras depois que o usuário digitar 0.
# Qualquer outro código deve gerar a mensagem de erro “Código inválido”.

# definindo a variável quantidade e total_compras
total_compras = 0
quantidade = 0
# Ler os códigos e a quantidade comprada e fazer os cálculos
while True:
    codigo = int(input("Qual é o código do produto? "))
    if codigo == 0:
        break
    if codigo != 1 and codigo != 2 and codigo != 3 and codigo != 5 and codigo != 9:
        print("Código inválido")
        break
    quantidade = int(input("Qual a quantidade comprada? "))
    
   
    total_compras = total_compras + quantidade

print(f"Total de compras foi: {total_compras:.0f}")