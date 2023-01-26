'''
Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta La suma de los 
primeros enteros positivos puede ser calculada de la siguiente forma:
 '''

num = int(input('Introduzca un numero entero positivo \n'))
suma = float(((num*(num + 1))/2))

print(f'El numero dado es {num} y la suma de los primeros numeros enteros es {suma}')