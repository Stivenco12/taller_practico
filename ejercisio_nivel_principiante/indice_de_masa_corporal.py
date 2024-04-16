import os
os.system ("cls")

#variables
nombre = ""
edad = 0
peso = 0
altura = 0
imc = 0.0
pesoideal = 0
obecidad1 = 0
obecidad2 = 0
obecidad3 = 0
sobrepeso = 0

#todo del estudiante
#repeticion
for i in range (0,2):
    nombre = input(f"ingrese nombre del estudiante {i+1}: ")
    edad = int(input(f"ingrese la edad del estudiante {i+1}: "))
    peso =+ float(input(f"ingrese el peso del estudiante {i+1}: "))
    altura =+ float(input(f"ingrese la altura del estudiante {i+1}: "))
    imc = peso // (altura*2)
    print("el imc del estudiante es de : " ,imc)

#imc del estudiante y contaduria de personas y sus pesos
    if    18.0 <= imc < 24:
        print("la persona tiene un peso normal") ,pesoideal
        pesoideal = pesoideal + 1
    elif ((imc >= 25.0) and (imc <=29.9 )):
        print("la pers0na tiene sobre peso") ,obecidad1
        obecidad1 = obecidad1 + 1 
    elif ((imc >= 30.0) and (imc <= 34.9)):
        print("la persona tiene sobrepeso grado 1") ,obecidad2
        obecidad2 = obecidad2 + 1
    elif ((imc >= 35.0) and (imc <= 39.0)):
        print("la persona tiene sobrepeso grado 2") ,obecidad3
        obecidad3 = obecidad3 + 1
    elif ((imc >= 40.0) and (imc <= 1000)):
        print("la persona tiene sobrepeso grado 3") ,sobrepeso 
        sobrepeso = sobrepeso + 1
    else:
        print("la persona no cumple lo requisitos para entrar en la calificasion") 
    #cantidad de personas con sirtas tipos de peso
    print (f"la cantidad de personas con peso normal es de {pesoideal}")
    print (f"la cantidad de personas con obecidad 1 es de {obecidad1}")
    print (f"la cantidad de personas con obecidad 2 es de {obecidad2}")
    print (f"la cantidad de personas con obecidad 3 es de {obecidad3}")
    print (f"la cantidad de personas con sobrepeso es de {sobrepeso}")
    
