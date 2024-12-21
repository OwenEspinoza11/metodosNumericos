import matplotlib.pyplot as plt
import math

def trapecio(func, a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [func(xi) for xi in x]
    
    integral = (y[0] + y[-1]) / 2 + sum(y[i] for i in range(1, n))
    integral *= h
    
    return integral

def plot_function(func, a, b):
    x_vals = [a + i * (b - a) / 1000 for i in range(1001)]
    y_vals = [func(x) for x in x_vals]

    plt.plot(x_vals, y_vals, label="f(x)")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Función f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()


# Pedir datos al usuario
try:
    funcion_str = input("Introduce la función f(x)")
    funcion = eval("lambda x: " + funcion_str)
    a = float(input("Introduce el límite inferior de integración (a): "))
    b = float(input("Introduce el límite superior de integración (b): "))
    n = int(input("Introduce el número de subintervalos (n): "))

    resultado = trapecio(funcion, a, b, n)
    print(f"Resultado de la integral: {resultado}")

    plot_function(funcion, a, b)

except Exception as e:
    print(f"Error: {e}")
