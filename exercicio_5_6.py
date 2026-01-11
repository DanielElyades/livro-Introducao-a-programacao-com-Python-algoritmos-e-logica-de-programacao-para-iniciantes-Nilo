# Exercício 5.6 Altere o programa anterior para exibir os resultados no mesmo for-
# mato de uma tabuada: 2x1 = 2, 2x2=4, ...

# Ler qual vai ser a tabuada
n = int(input("Tabuada de: "))

# Define o valor de x
x = 1

# Calcular a tabuada com while
while x <= 10:
    resultado = x * n
    print(f"{n} x {x} = {resultado}")
    x = x + 1

print("Fim")