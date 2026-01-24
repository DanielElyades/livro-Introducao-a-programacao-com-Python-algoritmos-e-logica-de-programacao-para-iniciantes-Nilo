# Exercício 6.3 Faça um programa que percorra duas listas e gere uma terceira sem
# elementos repetidos.

# criar listas
a = [1, 2, 3]
b = [1, 2, 3, 4, 5]

# Percorrer as listas
x = 0
c = []
while x < len(a):
    c.append(a[x])
    x += 1

x = 0
while x < len(b):
    if b[x] not in c:
        c.append(b[x])
    x += 1

# Imprimir a lista
print(c[:])
