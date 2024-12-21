import matplotlib.pyplot as plt
import statistics

def calcular_regresion_simple(x, y):
    n = len(x)
    mean_x = statistics.mean(x)
    mean_y = statistics.mean(y)
    
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x2 = sum(xi**2 for xi in x)
    
    # Calcula la pendiente (m) y la intersección (b) de la línea de regresión
    m = (sum_xy - n * mean_x * mean_y) / (sum_x2 - n * mean_x**2)
    b = mean_y - m * mean_x
    
    # Calcula el coeficiente de determinación (R^2)
    y_pred = [m * xi + b for xi in x]
    ss_total = sum((yi - mean_y)**2 for yi in y)
    ss_residual = sum((yi - y_predi)**2 for yi, y_predi in zip(y, y_pred))
    r2 = 1 - (ss_residual / ss_total)
    
    return m, b, r2, y_pred




# Pedir datos al usuario
try:
    x = list(map(float, input("Ingrese los valores de x separados por comas: ").split(',')))
    y = list(map(float, input("Ingrese los valores de y separados por comas: ").split(',')))

    if len(x) != len(y):
        raise ValueError("Las listas de x e y deben tener la misma longitud.")

    m, b, r2, y_pred = calcular_regresion_simple(x, y)

    # Imprimir los resultados
    print("")
    print(f"Modelo de regresión lineal simple:")
    print(f"y = {m:.4f} * x + {b:.4f}")
    print("")
    
    print(f"Pendiente (m): {m:.4f}")
    print(f"Intersección (b): {b:.4f}")
    print(f"Coeficiente de determinación (R^2): {r2:.4f}")

    plt.scatter(x, y, color='green', label='Observaciones')
    plt.plot(x, y_pred, color='black', label='Regresión')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Regresión simple')
    plt.legend()
    plt.grid(True)
    plt.show()


except Exception as e:
    print(f"Error: {e}")
