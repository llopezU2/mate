from flask import Flask, render_template, request

app = Flask(__name__)

def resolver_sistema_lineal(A, B):
    # Elimina hacia adelante (método de Gauss)
    n = len(A)
    for i in range(n):
        pivote = A[i][i]
        for j in range(i, n):
            A[i][j] /= pivote
        B[i] /= pivote

        for k in range(i + 1, n):
            factor = A[k][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            B[k] -= factor * B[i]

    # Sustitución hacia atrás
    X = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        suma = sum(A[i][j] * X[j] for j in range(i + 1, n))
        X[i] = round(B[i] - suma, 2)  # Limitar a dos decimales

    return X

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
