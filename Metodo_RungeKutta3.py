import matplotlib.pyplot as plt
import math
def Metodo_RungeKutta3_mejorado(f, xo, yo, h, n):
    x_eje = [xo]
    y_eje = [yo]

    for i in range(n):
        x = x_eje[-1]  # Se extrae el último valor de x para luego evaluar
        y = y_eje[-1]  # Se extrae el último valor de y para luego evaluar

        k = f(x, y)

        # Calculamos los valores intermediarios
        x_intermedio = x + (3/4) * h
        y_intermedio = y + (3/4) * k

        k2 = f(x_intermedio, y_intermedio)

        # Calculamos el nuevo valor de y usando la fórmula proporcionada
        y_new = y + (h/3) * (k + 2 * k2)
        x_new = x + h

        x_eje.append(x_new)
        y_eje.append(y_new)

        # Imprimir resultados de cada iteración

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

    x_eje, y_eje = Metodo_RungeKutta3_mejorado(f, xo, yo, h, n)

    # Imprimir los resultados finales
    print("\nResultados finales:")
    for x, y in zip(x_eje, y_eje):
        print(f'x = {x:.4f}, y = {y:.6f}')

    # Graficar los resultados
    plt.plot(x_eje, y_eje, marker='o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Método de Runge-Kutta Mejorado de Tercer Orden')
    plt.grid(True)
    plt.show()

except Exception as e:
    print(f"Error: {e}")
