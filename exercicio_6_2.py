# Exercício 6.2 Faça um programa que leia duas listas e que gere uma terceira com
# os elementos das duas primeiras.

# Criar listas
a = [1, 2, 3]
b = [4, 5, 6]

# Gerar uma terceira lista como os elementos das duas primeiras
c = a[:] + b[:]

# Imprimir lista
print(c[:])