def multiplicar_matrices(matriz1, matriz2):
    filas1 = len(matriz1)
    columnas2 = len(matriz2[0])
    resultado = [[0 for _ in range(columnas2)] for _ in range(filas1)]

    for i in range(filas1):
        for j in range(columnas2):
            resultado[i][j] = sum(matriz1[i][k] * matriz2[k][j] for k in range(len(matriz2)))

    return resultado
