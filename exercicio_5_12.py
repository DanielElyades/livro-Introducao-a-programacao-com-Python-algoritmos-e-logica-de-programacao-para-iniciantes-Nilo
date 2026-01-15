# Exercício 5.12 Altere o programa anterior de forma a perguntar também o valor
# depositado mensalmente. Esse valor será depositado no início de cada mês, e você
# deve considerá-lo para o cálculo de juros do mês seguinte.

# Ler o deposito inicial
deposito = float(input("Qual o valor inicial: "))
saldo = deposito

# Ler a taxa de juros da poupança
taxa = float(input("Qual a taxa de juros da poupança: "))

# Converter para taxa de juros mensal
taxa_mensal = taxa / 12
taxa_mensal = taxa_mensal / 100

# Contador
mes = 0
resultado = 0

# Calculo usando while
while mes <= 24:
    saldo = saldo + (saldo * taxa_mensal)
    mes = mes + 1
    print(f"Resultado do mês {mes}: {saldo:.2f}")
    deposito_mensal = float(input(f"Quanto vai depositar no mês {mes}?"))
    saldo = saldo + deposito_mensal

print(f"Saldo inicial: {saldo - deposito:.2f}")
print(f"Saldo final: {saldo:.2f}")