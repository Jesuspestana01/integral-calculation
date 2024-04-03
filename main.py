#importamos librerias que se usaran:
import numpy as np
import matplotlib.pyplot as plt
import math
import time
from sympy import *
from intersect import intersection

#se usa sympy para indicar que x sera igual a la variable x de una ecuacion
x = Symbol("x")

#Iniciamos el programa
print("Hola. A continuacion, el programa le pedira colocar las variables de ambas funciones parabolas.\n")
print("Coloque las variables A, B, C de la funcion f(x): \n")

#Se pide que se coloque los valores de las variables de la primera funcion parabola. Se hace validaciones.
def entrada_coeficiente(prompt):
    while True:
        try:
            coeficiente = float(input(prompt + ": "))
            return coeficiente
        except ValueError:
            print("Ingrese un numero valido.")

#Se pide que se coloque los valores de las variables de la primera funcion parabola.
coeficiente_a = entrada_coeficiente("a")
coeficiente_b = entrada_coeficiente("b")
coeficiente_c = entrada_coeficiente("c")

#Se pide que se coloque los valores de las variables de la segunda funcion parabola.
print("Ahora coloque las variables E, F, G de la funcion parabola g(x):\n ")
coeficiente_e = entrada_coeficiente("e")
coeficiente_f = entrada_coeficiente("f")
coeficiente_g = entrada_coeficiente("g")


#Se hace validaciones para mostrar la primera funcion al usuario
if (coeficiente_b < 0): 
    print("Esta es tu funcion f(x) = ",coeficiente_a, "x^2 -",coeficiente_b,"x +",coeficiente_c)
elif (coeficiente_b < 0 and coeficiente_c < 0):
    print("Esta es tu funcion f(x) = ",coeficiente_a, "x^2 -",coeficiente_b,"x -",coeficiente_c)
elif (coeficiente_b >= 0 and coeficiente_c < 0):
    print("Esta es tu funcion f(x) = ",coeficiente_a, "x^2 +",coeficiente_b,"x -",coeficiente_c)
else:
    print("Esta es tu funcion f(x) = ",coeficiente_a, "x^2 +",coeficiente_b,"x +",coeficiente_c)

if (coeficiente_f < 0): 
    print("Esta es tu funcion g(x) = ",coeficiente_e, "x^2 -",coeficiente_f,"x +",coeficiente_g)
elif (coeficiente_f < 0 and coeficiente_g < 0):
    print("Esta es tu funcion g(x) = ",coeficiente_e, "x^2 -",coeficiente_f,"x -",coeficiente_g)
elif (coeficiente_f >= 0 and coeficiente_g < 0):
    print("Esta es tu funcion g(x) = ",coeficiente_e, "x^2 +",coeficiente_f,"x -",coeficiente_g)
else:
    print("Esta es tu funcion g(x) = ",coeficiente_e, "x^2 +",coeficiente_f,"x +",coeficiente_g)

#despeje de g(x) para que f(x) = g(x)
if (coeficiente_e > 0):
    coeficiente_e = -abs(coeficiente_e)
elif (coeficiente_e < 0):
    coeficiente_e = abs(coeficiente_e)

if (coeficiente_f > 0):
    coeficiente_f = -abs(coeficiente_f)
elif (coeficiente_f < 0):
    coeficiente_f = abs(coeficiente_f)

if (coeficiente_g > 0):
    coeficiente_g = -abs(coeficiente_g)
elif (coeficiente_g < 0):
    coeficiente_g = abs(coeficiente_g)


#Se calcula la funcion donde f(x) = g(x)
a1 = (coeficiente_a + coeficiente_e)
b1 = (coeficiente_b + coeficiente_f)
c1 = (coeficiente_c + coeficiente_g)


# Se calcula el discriminante 
d = b1**2 - 4*a1*c1

#Se valida el valor del discriminante
print("Este es el discriminante: ", d)
if d < 0:
    print("No hay interseccion entre ambas funciones. Vuelva coeficiente_a colocar los valores de ambas funciones.")
elif (d == 0):
    print("Solamente se interseccionan en 1 punto. Por lo que no se puede encontrar el area.")
else:
    #Se encuentran los limites
    l1 = (-b1 - math.sqrt(d)) / (2*a1)
    print("Limite superior:", l1)
    l2 = (-b1 + math.sqrt(d)) / (2*a1)
    print("Limite inferior:", l2)

#Calculo del area debajo de las curvas
f = a1*x**2 + b1*x + c1
#limites de integracion a y b
la = l1
lb = l2

print(a1, b1, c1)
def contador(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        # print("Calculando area. Por favor espere: \r", end="\r")
        # print(timer, end="\r") 
        print("Calculando area. Por favor espere: ", timer, end="\r")
        time.sleep(1) 
        t -= 1
        integral_de_area = integrate(f, (x, la, lb))
        if t == 0:
            print("Este es el area:", integral_de_area, end="\r")
contador(5)
 
#valores de g(x)
coeficiente_g = abs(coeficiente_g)
coeficiente_f = abs(coeficiente_f)
coeficiente_e = abs(coeficiente_e)

#inicio de programa para mostrar la grafica.
def funcf(x):
    return coeficiente_a*x**2 + coeficiente_b*x + coeficiente_c

def funcg(x):
    return coeficiente_e*x**2 + coeficiente_f*x + coeficiente_g 


# Creando los vectores Y y X
valor_x = np.linspace(-2.5, 2.5, 100)
valor_y_f = funcf(valor_x)
valor_y_g = funcg(valor_x)

x_intersection, y_intersection = intersection(valor_x, valor_y_f, valor_x, valor_y_g)

 
fig = plt.figure(figsize = (10, 5))
#creacion de la grafica
plt.grid(True)
plt.plot(valor_x, valor_y_f, c="b")
plt.plot(valor_x, valor_y_g, c="r")
plt.plot(x_intersection, y_intersection, "o", c="k")
plt.axvline(x= 0, ls="--" , c="k")
plt.axhline(y= 0, ls="--" , c="k")
plt.fill_between(valor_x, valor_y_f, valor_y_g, where=(valor_y_f > valor_y_g), color='gray', alpha=0.3)
# mostrar grafica
plt.show()