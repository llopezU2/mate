from flask import Flask, render_template, request
from cofactor import calcular_determinante_y_inversa
from regresion import calcular_regresion, graficar_regresion
from resta import restar_matrices
from suma import sumar_matrices
from multiplicacion import multiplicar_matrices
from reduccion import reducir_matrices  # Importar la función de reducción de matrices

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
            # Obtener las matrices desde el formulario
            matriz1 = [[int(request.form[f'matriz1_{i}_{j}']) for j in range(3)] for i in range(3)]
            matriz2 = [[int(request.form[f'matriz2_{i}_{j}']) for j in range(3)] for i in range(3)]

            # Calcular la suma de las matrices
            resultado = sumar_matrices(matriz1, matriz2)

            return render_template('suma.html', resultado=resultado)

        except Exception as e:
            return render_template('suma.html', error="Error al realizar la suma de matrices.")
    
    # Si es GET, renderizar la página en blanco
    return render_template('suma.html')

@app.route('/resta', methods=['GET', 'POST'])
def resta():
    if request.method == 'POST':
        try:
            # Obtener las matrices desde el formulario
            matriz1 = [[int(request.form[f'matriz1_{i}_{j}']) for j in range(3)] for i in range(3)]
            matriz2 = [[int(request.form[f'matriz2_{i}_{j}']) for j in range(3)] for i in range(3)]

            # Calcular la resta de las matrices
            resultado = restar_matrices(matriz1, matriz2)

            return render_template('resta.html', resultado=resultado)

        except Exception as e:
            return render_template('resta.html', error="Error al realizar la resta de matrices.")
    
    # Si es GET, renderizar la página en blanco
    return render_template('resta.html')


@app.route('/multiplicacion', methods=['GET', 'POST'])
def multiplicacion():
    if request.method == 'POST':
        try:
            # Obtener las matrices desde el formulario
            matriz1 = [[int(request.form[f'matriz1_{i}_{j}']) for j in range(3)] for i in range(3)]
            matriz2 = [[int(request.form[f'matriz2_{i}_{j}']) for j in range(3)] for i in range(3)]

            # Calcular la multiplicación de las matrices
            resultado = multiplicar_matrices(matriz1, matriz2)

            return render_template('multiplicacion.html', resultado=resultado)

        except Exception as e:
            return render_template('multiplicacion.html', error="Error al realizar la multiplicación de matrices.")
    
    # Si es GET, renderizar la página en blanco
    return render_template('multiplicacion.html')

@app.route('/reduccion', methods=['GET', 'POST'])
def reduccion():
    if request.method == 'POST':
        try:
            # Obtener la matriz A y el vector C desde el formulario
            matriz1 = [[int(request.form[f'matriz1_{i}_{j}']) for j in range(3)] for i in range(3)]
            vector_c = [int(request.form[f'vector_c_{i}']) for i in range(3)]

            # Calcular la reducción de matrices (inversa de A multiplicada por C) y el determinante
            x, Y, Z, determinante = reducir_matrices(matriz1, vector_c)

            return render_template('reduccion.html', x=x, Y=Y, Z=Z, determinante=determinante)

        except Exception as e:
            return render_template('reduccion.html', error="Error al realizar la reducción de matrices.")
    
    # Si es GET, renderizar la página en blanco
    return render_template('reduccion.html')


if __name__ == '__main__':
    app.run(debug=True)
