'''Se recibe la fecha1 y fecha2
para conseguir el año se divide la variable en 10000
para conseguir los dias se sacar el modular de las fechas divididos en 100
para el mes entra en un ciclo while donde se compara la variable i si es menor a 3
	En el ciclo se crea la variable mes donde se sacar el residuo de la variable fecha
	A la variable fecha se le resta el mes extraido y se divide entre 10
	la variable i se suma 1
Se compara los meses para saber si ya paso ese mes en ese año
si no ha pasado se resta 1 
se compara los meses para saber cual es el menor y subarle 12 y se le resta el otro mes
Se compara los dias para saber cual es el mayor para restarlo 
para la variable final se multiplica la variable por 100 para guardar todos los datos
'''
fecha1 = int(input("Ingrese la primera fecha: "))
fecha2 = int(input("Ingrese la segunda fecha: "))
ano_fecha1 = fecha1//10000
ano_fecha2 = fecha2//10000
dia_fecha1 = fecha1%100 
dia_fecha2 = fecha2%100

i = 0
mes_fecha1 = 0
mes_fecha2 = 0
anofinal = 0
diafinal = 0
mesfinal = 0
fechafinal = 0
while i < 3:
    mes_fecha1 = fecha1%10
    mes_fecha2 = fecha2%10
    fecha1 = (fecha1-mes_fecha1)//10
    fecha2 = (fecha2-mes_fecha2)//10
    i = i+1
if (mes_fecha1 < mes_fecha2):
    anofinal = ano_fecha2-ano_fecha1
else:
    anofinal = (ano_fecha2-ano_fecha1)-1
if (mes_fecha1 > mes_fecha2):
    mesfinal = (mes_fecha2+12)-mes_fecha1
elif (mes_fecha1 == mes_fecha2):
    mesfinal = 0
else: 
    mesfinal = (mes_fecha1+12)-mes_fecha2
if (dia_fecha1 > dia_fecha2):
    diafinal = dia_fecha1-dia_fecha2
else:
    diafinal = dia_fecha2-dia_fecha1
fechafinal = ((anofinal*100)+mesfinal)
fechafinal = (fechafinal*100)+diafinal
print(fechafinal)

        
