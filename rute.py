from flask import Flask, render_template, request
from cofactor import calcular_determinante_y_inversa
from resta import Resta

app = Flask(__name__)

@app.route('/')
def index():
    # Renderiza el index.html al cargar la ruta principal
    return render_template('index.html')

@app.route('/cofactor', methods=['GET', 'POST'])
def cofactor():
    if request.method == 'POST':
        try:
            # Obtener los valores ingresados por el usuario y formar la matriz
            a = [[float(request.form[f'cell{i}{j}']) for j in range(3)] for i in range(3)]
            
            # Llamar a la función del archivo matriz.py para calcular el determinante e inversa
            invM, det = calcular_determinante_y_inversa(a)
            
            if invM is None:
                return render_template('cofactor.html', error=det)  # Mostrar error si no hay inversa
            
            # Renderizar la plantilla con los resultados
            return render_template('cofactor.html', det=det, invM=invM)
        
        except ValueError:
            return render_template('cofactor.html', error="Por favor, ingrese números válidos.")
    
    # Si es un GET, simplemente muestra la página de cofactor
    return render_template('cofactor.html')

@app.route('/suma')
def suma():
    # Renderiza la página de suma de matrices (lógica se agregará más adelante)
    return render_template('suma.html')

@app.route('/resta', methods=['GET', 'POST'])
def resta():
    if request.method == 'POST':
        try:
            filas = int(request.form['filas'])
            columnas = int(request.form['columnas'])
            
            # Obtener las matrices desde el formulario
            matriz1 = obtener_matriz_formulario('mat1_', filas, columnas)
            matriz2 = obtener_matriz_formulario('mat2_', filas, columnas)
            
            # Calcular la resta de matrices
            resultado = calcular_resta(matriz1, matriz2)
            
            # Renderizar la plantilla con el resultado y las matrices persistidas
            return render_template('resta.html', resultado=resultado, filas=filas, columnas=columnas, matriz1=matriz1, matriz2=matriz2)
        
        except Exception as e:
            print("Error:", e)
            return render_template('resta.html', error="Error al calcular la resta de matrices.")
    
    # Si es una solicitud GET, simplemente mostrar la página con el formulario vacío
    return render_template('resta.html', filas=None, columnas=None, matriz1=None, matriz2=None)


def obtener_matriz_formulario(prefix, filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(request.form.get(f'{prefix}{i}_{j}', 0))  # Obtener el valor del input
            fila.append(valor)
        matriz.append(fila)
    return matriz

def calcular_resta(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz1[0])):
            fila_resultado.append(matriz1[i][j] - matriz2[i][j])
        resultado.append(fila_resultado)
    return resultado



if __name__ == '__main__':
    app.run(debug=True)
