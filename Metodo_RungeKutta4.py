"""
Metodo de Metodo_RungeKutta3;

Variable necesarias para ellos:
f = La funcion que define la derivida dy/dx = f(x,y).
x0 = El valor inicial de x
y0 = El valor inicial de y
h = El tamaño del cambio
n = El numero de nodos
k1 , k2 , k3 , k4
Varible que duelve:

x_eje = Lista Valores en X
y_eje = Lista Valores en Y

"""


import matplotlib.pyplot as plt
import math
def Metodo_RungeKutta4(f, xo, yo, h, n):
    x_eje = [xo]
    y_eje = [yo]

    for i in range(n):
        x = x_eje[-1] # Se extra el ultimo valor de x para luego a evaluar
        y = y_eje[-1] # Se extra el ultimo valor de y para luego a evaluar

        k1 = f(x, y)
        k2 = f(x + h/2, y + k1/2)
        k3 = f(x + h/2, y + k2/2)
        k4 = f(x + h, y + (h*k3))

        y_new = y + (h/6 *(k1 + 2*(k2 + k3) + k4))
        x_new = x + h

        x_eje.append(x_new)
        y_eje.append(y_new)



    return x_eje, y_eje

# Pedir datos al usuario
try:
    
    funcion = input("Introduce la función f(x, y): \n\n")
    funcion = "lambda x, y: " + funcion
    f = eval(funcion, {"math": math})
    
    xo = float(input("Introduce el valor inicial de x (xo): "))
    yo = float(input("Introduce el valor inicial de y (yo): "))
    xn = float(input("Introduce el valor final de x (xn): "))
    n = int(input("Introduce el número de nodos (n): "))
    h = (xn - xo) / n

    x_eje, y_eje = Metodo_RungeKutta4(f, xo, yo, h, n)

    # Imprimir los resultados finales
    print("\nResultados finales:")
    for x, y in zip(x_eje, y_eje):
        print(f'x = {x:.4f}, y = {y:.6f}')

    # Graficar los resultados
    plt.plot(x_eje, y_eje, marker='o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Método de Runge-Kutta de Cuarto Orden')
    plt.grid(True)
    plt.show()

except Exception as e:
    print(f"Error: {e}")
