"""
Metodo de Euler;

Variable necesarias para ellos:
f = La funcion que define la derivida dy/dx = f(x,y).
x0 = El valor inicial de x
y0 = El valor inicial de y
h = El tamaño del cambio
n = El numero de nodos

Varible que duelve:

Copiar código
x_eje = Lista Valores en X
y_eje = Lista Valores en Y

"""

import matplotlib.pyplot as plt
import math

def Metodo_Euler(f, xo, yo, h, n):
    x_eje = [xo]
    y_eje = [yo]

    for _ in range(n):
        x = x_eje[-1] # ultimo valor de x para luego a evaluar
        y = y_eje[-1] # ultimo valor de y para luego a evaluar
        y_new = y + h * f(x, y)
        x_new = x + h

        x_eje.append(x_new)
        y_eje.append(y_new)





    return x_eje, y_eje

# datos del usuario
try:
    funcion = input("Introduce la función f(x, y): \n\n")
    funcion = "lambda x, y: " + funcion
    f = eval(funcion, {"math": math})
    
    xo = float(input("Introduce el valor inicial de x (xo): "))
    yo = float(input("Introduce el valor inicial de y (yo): "))
    xn = float(input("Introduce el valor final de x (xn): "))
    n = int(input("Introduce el número de nodos (n): "))
    h = (xn - xo) / n

    x_eje, y_eje = Metodo_Euler(f, xo, yo, h, n)

    # Imprimir
    for x, y in zip(x_eje, y_eje):
        print(f'x = {x:.2f}, y = {y:.4f}')

    # Graficar los resultados
    plt.plot(x_eje, y_eje, marker='o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Método de Euler')
    plt.grid(True)
    plt.show()

except Exception as e:
    print(f"Error: {e}")
