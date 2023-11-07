# n = int(input())
n = 0

for i in range(n):
    print(i)

for i in range(3 * n):
    print(i)

# david balleza was here

# Ej de la clase pasada

numeros = [1, 2, 4, 6, 7, 8, 12, 3421, 4, 5, 6, 7]

sumas = []
sumas.append(numeros[0])

for i in range(1, len(numeros)):
    sumas.append(sumas[-1] + numeros[i])

queries = [(1, 5), (3, 6), (6, 9), (11, 11), (0, 2)]

for query in queries:
    if (query[0] <= query[1] and max(query[0], query[1]) < len(numeros) and min(query[0], query[1]) >= 0):
        print("Resultado: ", end="")
        resultado = sumas[query[1]]
        if (query[0] > 0):
            resultado -= sumas[query[0] - 1]
        print(resultado)
