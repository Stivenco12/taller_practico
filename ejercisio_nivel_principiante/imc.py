nombre = ""
edad = 0
peso = 0.0
altura = 0.0
imc = 0.0
nombre = input("ingrese nombre del estudiante : ")
edad = int(input("ingrese la edad del estudiante : "))
peso = int(input("ingrese el peso del estudiante : "))
altura = float(input("ingrese la altura del estudiante : "))
imc = float(peso / (altura*2))
imc = int(input(f"el imc del estudiante es de {imc}: "))