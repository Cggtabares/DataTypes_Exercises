#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

amount = float(input('Cantidad que se desea invertir \n'))
annual_int = float(input('Interes anual el cual invertir \n'))
years = float(input('Ingrese el numero de annos que se desea invertir \n'))
annual_int = annual_int / 100

earned = (amount * ((1 + annual_int) ** years))

print(f'El capital que desea invertir es {amount}')
print(f'El interes anual es {annual_int}')
print(f'Los años que se desea invertir es {years}')
print(f'El capital obtenido es {earned}')
