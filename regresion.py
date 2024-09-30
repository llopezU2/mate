# regresion.py
import matplotlib.pyplot as plt

def calcular_regresion(x, y):
    if len(x) != len(y):
        raise ValueError("Las listas de X e Y deben tener la misma longitud")
    
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x[i] * y[i] for i in range(n))
    sum_x2 = sum(xi ** 2 for xi in x)

    # Calcular la pendiente (m)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    x_media = sum_x / n
    y_media = sum_y / n

    # Calcular la intersección (b)
    b = y_media - m * x_media

    # Redondear resultados
    m = round(m, 2)
    b = round(b, 2)

    return m, b

def graficar_regresion(x, y, m, b, output_path):
    plt.scatter(x, y, color='red', label='Datos')
    plt.plot(x, [b + m * xi for xi in x], label=f'y = {b} + {m}x', color='blue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Regresión Lineal por Mínimos Cuadrados')
    plt.legend()
    plt.savefig(output_path)
    plt.close()
