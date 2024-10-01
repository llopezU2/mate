from flask import Flask, render_template, request
from cofactor import calcular_determinante_y_inversa
from regresion import calcular_regresion, graficar_regresion
from resta import Resta
from suma import Suma
from reduccion import resolver_sistema_lineal  # Importar la función correcta para la reducción de matrices
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la regresión lineal
@app.route('/regresion', methods=['GET', 'POST'])
def regresion():
    if request.method == 'POST':
        try:
            x_values = request.form['x_values']
            y_values = request.form['y_values']
            x = [float(i) for i in x_values.split(',')]
            y = [float(i) for i in y_values.split(',')]

            m, b, r = calcular_regresion(x, y)  # Incluimos el coeficiente de correlación 'r'
            plot_path = os.path.join('static', 'plot_regresion.png')
            graficar_regresion(x, y, m, b, r, plot_path)  # Pasamos 'r' para mostrar en la gráfica

            return render_template('regresion.html', m=m, b=b, r=r, plot_url=plot_path)
        
        except Exception as e:
            return render_template('regresion.html', error=str(e))
    
    return render_template('regresion.html')

@app.route('/cofactor', methods=['GET', 'POST'])
def cofactor():
    if request.method == 'POST':
        try:
            a = [[float(request.form[f'cell{i}{j}']) for j in range(3)] for i in range(3)]
            invM, det = calcular_determinante_y_inversa(a)
            if invM is None:
                return render_template('cofactor.html', error=det)
            return render_template('cofactor.html', det=det, invM=invM)
        
        except ValueError:
            return render_template('cofactor.html', error="Por favor, ingrese números válidos.")
    
    return render_template('cofactor.html')

@app.route('/suma', methods=['GET', 'POST'])
def suma():
    if request.method == 'POST':
        try:
            filas = int(request.form['filas'])
            columnas = int(request.form['columnas'])
            matriz1 = obtener_matriz_formulario('mat1_', filas, columnas)
            matriz2 = obtener_matriz_formulario('mat2_', filas, columnas)
            resultado = calcular_suma(matriz1, matriz2)
            return render_template('suma.html', resultado=resultado, filas=filas, columnas=columnas, matriz1=matriz1, matriz2=matriz2)
        
        except Exception as e:
            return render_template('suma.html', error="Error al calcular la suma de matrices.")
    
    return render_template('suma.html', filas=None, columnas=None, matriz1=None, matriz2=None)

def obtener_matriz_formulario(prefix, filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(request.form.get(f'{prefix}{i}_{j}', 0))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def calcular_suma(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz1[0])):
            fila_resultado.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila_resultado)
    return resultado

@app.route('/resta', methods=['GET', 'POST'])
def resta():
    if request.method == 'POST':
        try:
            filas = int(request.form['filas'])
            columnas = int(request.form['columnas'])
            matriz1 = obtener_matriz_formulario('mat1_', filas, columnas)
            matriz2 = obtener_matriz_formulario('mat2_', filas, columnas)
            resultado = calcular_resta(matriz1, matriz2)
            return render_template('resta.html', resultado=resultado, filas=filas, columnas=columnas, matriz1=matriz1, matriz2=matriz2)
        
        except Exception as e:
            return render_template('resta.html', error="Error al calcular la resta de matrices.")
    
    return render_template('resta.html', filas=None, columnas=None, matriz1=None, matriz2=None)

def calcular_resta(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz1[0])):
            fila_resultado.append(matriz1[i][j] - matriz2[i][j])
        resultado.append(fila_resultado)
    return resultado

# Nueva ruta para la reducción de sistemas de ecuaciones lineales
@app.route('/reduccion', methods=['GET', 'POST'])
def reduccion():
    if request.method == 'POST':
        try:
            # Obtener los valores ingresados por el usuario y formar la matriz A
            a11 = float(request.form.get('a11'))
            a12 = float(request.form.get('a12'))
            a13 = float(request.form.get('a13'))
            a21 = float(request.form.get('a21'))
            a22 = float(request.form.get('a22'))
            a23 = float(request.form.get('a23'))
            a31 = float(request.form.get('a31'))
            a32 = float(request.form.get('a32'))
            a33 = float(request.form.get('a33'))

            # Obtener los valores de la columna C (resultados)
            b1 = float(request.form.get('b1'))
            b2 = float(request.form.get('b2'))
            b3 = float(request.form.get('b3'))

            # Crear la matriz A y el vector B
            A = [[a11, a12, a13],
                 [a21, a22, a23],
                 [a31, a32, a33]]

            B = [b1, b2, b3]

            # Llamar a la función para resolver el sistema de ecuaciones
            resultado = resolver_sistema_lineal(A, B)

            # Redondear los resultados a 3 decimales
            x, y, z = round(resultado[0], 3), round(resultado[1], 3), round(resultado[2], 3)

            # Renderizar la plantilla con los resultados redondeados
            return render_template('reduccion.html', x=x, y=y, z=z)
        
        except ValueError:
            return render_template('reduccion.html', error="Por favor, ingrese números válidos.")
    
    return render_template('reduccion.html')



if __name__ == '__main__':
    app.run(debug=True)
