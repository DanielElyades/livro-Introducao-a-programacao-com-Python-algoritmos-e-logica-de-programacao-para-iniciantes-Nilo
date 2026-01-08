# Exercício 4.2 Escreva um programa que pergunte a velocidade do carro de um
# usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário
# foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de
# 80 km/h.

# Ler a velocidade do carro do usuário
velocidade = float(input("Qual a velocidade do veículo? "))

# Condicionais para saber se o carro vai ser multado ou não
if velocidade <= 80:
    print("A velocidade está abaixo do máximo")
else:
    multa = (velocidade - 80) * 5
    print(f"A multa será no valor de {multa:.2f}")