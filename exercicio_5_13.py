# Exercício 5.13 Escreva um programa que pergunte o valor inicial de uma dívida e
# o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número
# de meses para que a dívida seja paga, o total pago e o total de juros pago.

# Entrada de dados
divida_inicial = float(input("Valor inicial da dívida: R$ "))
juros_mensal = float(input("Juros mensal (ex: 3 para 3%): "))
pagamento_mensal = float(input("Valor mensal a ser pago: R$ "))

# Conversão da taxa
taxa_decimal = juros_mensal / 100

# Verificação de segurança para evitar loop infinito
if (divida_inicial * taxa_decimal) >= pagamento_mensal:
    print("\nERRO: O pagamento mensal é menor ou igual aos juros.")
    print("A dívida nunca será paga nessas condições!")
else:
    divida = divida_inicial
    mes = 0
    total_pago = 0

    while divida > 0:
        # 1. Calcula os juros do mês sobre o saldo atual
        juros_do_mes = divida * taxa_decimal
        
        # 2. Atualiza a dívida com os juros
        divida = divida + juros_do_mes
        
        # 3. Realiza o pagamento
        if divida > pagamento_mensal:
            pagamento = pagamento_mensal
        else:
            pagamento = divida # Paga apenas o que resta
            
        divida = divida - pagamento
        total_pago = total_pago + pagamento
        mes = mes + 1
        
        # Opcional: imprimir progresso mensal
        # print(f"Mês {mes}: Saldo restante R$ {divida:.2f}")

    total_juros_pago = total_pago - divida_inicial

    print("-" * 40)
    print(f"Quantidade de meses: {mes}")
    print(f"Total pago: R$ {total_pago:.2f}")
    print(f"Total de juros pago: R$ {total_juros_pago:.2f}")
