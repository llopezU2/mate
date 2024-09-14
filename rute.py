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
            # Obtener el número de filas y columnas ingresados por el usuario
            filas = int(request.form['filas'])
            columnas = int(request.form['columnas'])
            
            # Obtener los valores de las matrices desde el formulario según el tamaño seleccionado
            mat1 = []
            mat2 = []
            for i in range(filas):
                row1 = [float(request.form.get(f'mat1_{i}_{j}', 0)) for j in range(columnas)]
                row2 = [float(request.form.get(f'mat2_{i}_{j}', 0)) for j in range(columnas)]
                mat1.append(row1)
                mat2.append(row2)
            
            # Usar la clase Resta para realizar la resta de las matrices
            resultado = Resta.restar_matrices(mat1, mat2)
            
            # Renderizar la página con el resultado
            return render_template('resta.html', resultado=resultado)
        
        except ValueError as e:
            return render_template('resta.html', error="Por favor, ingrese números válidos.")
    
    # Si es un GET, mostrar la página sin resultado
    return render_template('resta.html')



if __name__ == '__main__':
    app.run(debug=True)
