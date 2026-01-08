# Exercício 4.6 Escreva um programa que pergunte a distância que um passageiro
# deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
# para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

# Ler a distância 
distancia = float(input("Qual a distância em km? "))

# Calcular o preço da passagem com condicionais
if distancia <= 200:
    valor = distancia * 0.5
else:
    valor = distancia * 0.45

# Imprimir o valor na tela
print(f"O valor da viagem é: {valor:g}")