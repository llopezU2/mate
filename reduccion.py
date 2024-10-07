# Función para calcular el determinante de una matriz 3x3
def determinante(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) -
            a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0]) +
            a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))

# Función para calcular la matriz de cofactores de una matriz 3x3
def matriz_inversa(a):
    inversa = [[0, 0, 0] for _ in range(3)]

    inversa[0][0] = (a[1][1] * a[2][2] - a[1][2] * a[2][1])  # Cofactor A00
    inversa[0][1] = -(a[1][0] * a[2][2] - a[1][2] * a[2][0])  # Cofactor A01
    inversa[0][2] = (a[1][0] * a[2][1] - a[1][1] * a[2][0])  # Cofactor A02

    inversa[1][0] = -(a[0][1] * a[2][2] - a[0][2] * a[2][1])  # Cofactor A10
    inversa[1][1] = (a[0][0] * a[2][2] - a[0][2] * a[2][0])  # Cofactor A11
    inversa[1][2] = -(a[0][0] * a[2][1] - a[0][1] * a[2][0])  # Cofactor A12

    inversa[2][0] = (a[0][1] * a[1][2] - a[0][2] * a[1][1])  # Cofactor A20
    inversa[2][1] = -(a[0][0] * a[1][2] - a[0][2] * a[1][0])  # Cofactor A21
    inversa[2][2] = (a[0][0] * a[1][1] - a[0][1] * a[1][0])  # Cofactor A22

    return inversa

# Función para transponer una matriz (en este caso, la matriz de cofactores)
def transponer_matriz(a):
    return [[a[j][i] for j in range(3)] for i in range(3)]

# Función para calcular la inversa usando el método de cofactores
def inversa_por_cofactores(a):
    det = determinante(a)
    
    if det == 0:
        raise ValueError("La matriz no tiene inversa, su determinante es 0.")
    
    # Calcular la matriz de cofactores
    inversa = matriz_inversa(a)
    
    # Transponer la matriz de cofactores (adjunta)
    adjunta = transponer_matriz(inversa)
    
    # Dividir la adjunta por el determinante para obtener la inversa
    inversa = [[adjunta[i][j] / det for j in range(3)] for i in range(3)]
    
    return inversa, det

# Función para multiplicar una matriz 3x3 por un vector 3x1 (matriz inversa por C)
def multiplicar_matriz_vector(a, c):
    resultado = [0, 0, 0]
    
    # Cálculo del producto matriz por vector
    resultado[0] = a[0][0] * c[0] + a[0][1] * c[1] + a[0][2] * c[2]
    resultado[1] = a[1][0] * c[0] + a[1][1] * c[1] + a[1][2] * c[2]
    resultado[2] = a[2][0] * c[0] + a[2][1] * c[1] + a[2][2] * c[2]

    return resultado

# Función principal que sigue la lógica de la imagen proporcionada
def reducir_matrices(A, C):
    # Calcular la inversa de la matriz A y su determinante usando cofactores
    A_inversa, determinante = inversa_por_cofactores(A)
    
    # Multiplicar la inversa de A por el vector C
    resultado = multiplicar_matriz_vector(A_inversa, C)
    
    # Retornar los valores de x, Y, Z y el determinante
    x = resultado[0]
    Y = resultado[1]
    Z = resultado[2]
    
    return x, Y, Z, determinante
