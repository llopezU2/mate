from flask import Flask, render_template, request
from cofactor import calcular_determinante_y_inversa

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

if __name__ == '__main__':
    app.run(debug=True)
