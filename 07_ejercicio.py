'''
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
'''

kg = float(input('Ingrese su peso en kg \n'))
height = float(input('Ingrese su estatura en metros \n'))

imc = format(((kg)/(height ** 2)), ".2g")

print(f'Tu índice de masa corporal es {imc}')