# Exercício 3.12 Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

# Ler a distância
distancia = float(input("Informe a distância: "))

# Ler a velocidade média
velocidade_media = float(input("Informe a velocidade média em km/h: "))

# Calcular a duração da viagem
duracao = distancia / velocidade_media

# Imprime a duração na tela
print(f"A duração da viagem foi: {duracao:.2f} horas")