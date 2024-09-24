# METODO COFACTORES
def calcular_determinante_y_inversa(a):
    # Calcular determinante
    dP = a[0][0]*a[1][1]*a[2][2] + a[1][0]*a[2][1]*a[0][2] + a[2][0]*a[0][1]*a[1][2]
    dS = a[0][2]*a[1][1]*a[2][0] + a[1][2]*a[2][1]*a[0][0] + a[2][2]*a[0][1]*a[1][0]
    det = dP - dS

    if det == 0:
        return None, "La matriz no tiene inversa (determinante = 0)"

    # Calcular matriz de cofactores
    aCof = [[0]*3 for _ in range(3)]
    #primera fila
    aCof[0][0] = a[1][1]*a[2][2] - a[1][2]*a[2][1]
    aCof[0][1] = -(a[1][0]*a[2][2] - a[2][0]*a[1][2])
    aCof[0][2] = a[1][0]*a[2][1] - a[1][1]*a[2][0]
    #segunda fila
    aCof[1][0] = -(a[0][1]*a[2][2] - a[2][1]*a[0][2])
    aCof[1][1] = a[0][0]*a[2][2] - a[2][0]*a[0][2]
    aCof[1][2] = -(a[0][0]*a[2][1] - a[2][0]*a[0][1])
    #tercera fila
    aCof[2][0] = a[0][1]*a[1][2] - a[1][1]*a[0][2]
    aCof[2][1] = -(a[0][0]*a[1][2] - a[1][0]*a[0][2])
    aCof[2][2] = a[0][0]*a[1][1] - a[1][0]*a[0][1]

    # Transponer matriz de cofactores
    aT = [[aCof[j][i] for j in range(3)] for i in range(3)]

    # Calcular inversa dividiendo la transpuesta de los cofactores por el determinante
    invM = [[round(aT[i][j] / det, 2) for j in range(3)] for i in range(3)]

    return invM, det
