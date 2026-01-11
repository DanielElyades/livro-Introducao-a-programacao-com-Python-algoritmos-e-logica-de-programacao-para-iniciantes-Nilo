# Exercício 5.7 Modifique o programa anterior de forma que o usuário também
# digite o início e o fim da tabuada, em vez de começar com 1 e 10.

# Ler qual vai ser a tabuada
tabuada = int(input("Tabuada de: "))

# Inicio da tabuada
inicio = int(input("O inicio da tabuada: "))

# O fim da tabuada
fim = int(input("O fim da tabuada: "))

# Calcular a tabuada usando while
while inicio <= fim:
    resultado = inicio * tabuada
    print(f"{tabuada} x {inicio} = {resultado}")
    inicio = inicio + 1

print("Fim")