"""
Metodo de Euler;

Variable necesarias para ellos:
f = La funcion que define la derivida dy/dx = f(x,y).
x0 = El valor inicial de x
y0 = El valor inicial de y
h = El tamaño del cambio
n = El numero de nodos
f(x, y) = se sustituye valor x , y en la funcion dada
(yi+1)* = y corregida
f(xi+1, (yi+1)*) = se sustituye valor xi+1 , (yi+1)* en la funcion dada
Varible que duelve:

x_eje = Lista Valores en X
y_eje = Lista Valores en Y

"""
import matplotlib.pyplot as plt
import math


def Metodo_Euler_Mejorado(f, xo, yo, h, n):
    x_eje = [xo]
    y_eje = [yo]

    for _ in range(n):
        x = x_eje[-1] # Se extra el ultimo valor de x para luego a evaluar
        y = y_eje[-1] # Se extra el ultimo valor de y para luego a evaluar

        # Paso de Euler
        f_actual = f(x, y)
        y_pred = y + h * f_actual
        
        # Paso de corrección
        f_pred = f(x + h, y_pred)
        y_corr = y + h/2 * (f_actual + f_pred)

        x_new = x + h
        y_new = y_corr
        
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
    n = int(input("Introduce el número de iteraciones (n): "))
    h = (xn - xo) / n

    x_eje, y_eje = Metodo_Euler_Mejorado(f, xo, yo, h, n)

    # Imprimir los resultados finales
    print("\nTabla de X , Y:")
    for x, y in zip(x_eje, y_eje):
        print(f'x = {x:.4f}, y = {y:.4f}')

    # Graficar los resultados
    plt.plot(x_eje, y_eje, marker='o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Método de Euler Mejorado')
    plt.grid(True)
    plt.show()

except Exception as e:
    print(f"Error: {e}")
