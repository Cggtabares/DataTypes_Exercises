'''
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
'''

n = float(input('Ingresar un numero cualquiera \n'))
m = float(input('Ingrese un numero entero positivo \n'))

print(f'El numero ingresado es el dividendo: {n}')
print(f'El numero ingresado es el divisor: {m}')
print(f'El cociente de la division es: {n/m}')
print(f'El resto de la division es: {n%m}')