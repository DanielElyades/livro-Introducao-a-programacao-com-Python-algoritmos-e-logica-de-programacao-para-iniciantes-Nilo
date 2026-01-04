# Exercício 3.9 Escreva um programa que leia a quantidade de dias, horas, minutos
# e segundos do usuário. Calcule o total em segundos.
# Ler a quantidade de dias
dias = int(input("Digite a quantidade de dias: "))
# Ler a quantidade de horas
horas = int(input("Digite a quantidade de horas: "))
# Ler a quantidade de minutos
minutos = int(input("Digite a quantidade de minutos: "))
# Ler a quantidade de segundos
segundos = int(input("Digite a quantidade de segundos: "))
# transformar dias em segundos
dias_segundos = dias * 86400
# Transformar horas em segundos
horas_segundos = horas * 3600
# transformar minutos em segundos
minutos_segundos = minutos * 60
# Calcular o total em segundos
total_segundos = dias_segundos + horas_segundos + minutos_segundos + segundos
# Imprime na tela o total de segundos
print(f"O total em segundos é: {total_segundos:.0f}")