class Suma:
    @staticmethod
    def sumar_matrices(mat1, mat2):
        filas = len(mat1)
        columnas = len(mat1[0])  # Obtener el número de columnas desde la primera fila
        # Inicializar una matriz vacía para almacenar el resultado
        resultado = [[0 for _ in range(columnas)] for _ in range(filas)]
        
        # Realizar la suma elemento por elemento
        for i in range(filas):
            for j in range(columnas):
                resultado[i][j] = mat1[i][j] + mat2[i][j]
        
        return resultado
