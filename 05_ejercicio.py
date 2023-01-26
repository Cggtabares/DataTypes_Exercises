#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

hours = float(input('Introducir numero de horas trabajadas, si son horas y media, colocarlo en decimal \n'))
cost = float(input('Costo por hora trabajada segun contrato \n'))

total = hours * cost

print(f'El total a cobrar por {hours} a un costo por hora de {cost} es', total)