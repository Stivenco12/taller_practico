#variables
Co2 = 0
KvH = 0
FeME = 0.7
eleccion = 0
maximo = 0
consumo1 = 0.0
consumo2 = 0.0
consumo3 = 0.0
consumo4 = 0.0
consumo5 = 0.0
max_dependencia = float ("inf")
while eleccion != 5:
    print("""
    indique la operacion
    1) registrar dependecia
    2) registrar consumo por dependencia
    3) ver Co2 producido
    4) dependencia que produce mayor Co2
    5) salir
    """)
    eleccion = int(input("\t:)_"))
    

    if eleccion == 1:
        dependecia1 = input("ingrese el nombre de la primera dependencia ")
        dependecia2 = input("ingrese el nombre de la segunda dependencia ")
        dependecia3 = input("ingrese el nombre de la tercera dependencia ")
        dependecia4 = input("ingrese el nombre de la cuarta dependencia ")
        dependecia5 = input("ingrese el nombre de la quinta dependencia ")
    if eleccion == 2:
        consumo1 = float(input("ingresar el consumo de la dependencia 1 "))
        consumo2 = float(input("ingresar el consumo de la dependencia 2 "))
        consumo3 = float(input("ingresar el consumo de la dependencia 3 "))
        consumo4 = float(input("ingresar el consumo de la dependencia 4 "))
        consumo5 = float(input("ingresar el consumo de la dependencia 5 "))
    if eleccion == 3:
        consumo1 = consumo1*FeME
        consumo2 = consumo2*FeME
        consumo3 = consumo3*FeME
        consumo4 = consumo4*FeME
        consumo4 = consumo5*FeME
        Co2 = consumo1+consumo2+consumo3+consumo4+consumo5
        print ("la generacion de co2 de es de ",consumo1)
        print ("la generacion de co2 de es de ",consumo2)
        print ("la generacion de co2 de es de ",consumo3)
        print ("la generacion de co2 de es de ",consumo4)
        print ("la generacion de co2 de es de ",consumo5)
        print(f"el Co2 produccido es de {Co2}")
    if eleccion == 4:
        if consumo1 > consumo2 and consumo1 > consumo3 and consumo1 > consumo4 and consumo1 > consumo5 :
            print ("el numero mayor es: ",consumo1)
        elif consumo2 > consumo1 and consumo2 > consumo3 and consumo2 > consumo4 and consumo2 > consumo5 :
            print ("el numero mayor es: ",consumo2)
        elif consumo3 > consumo1 and consumo3 > consumo2 and consumo3 > consumo4 and consumo3 > consumo5 :
            print ("el numero mayor es: ",consumo3)
        elif consumo4 > consumo1 and consumo4 > consumo2 and consumo4 > consumo3 and consumo4 > consumo5 :
            print ("el numero mayor es: ",consumo4)
        elif consumo5 > consumo1 and consumo5 > consumo2 and consumo5 > consumo3 and consumo5 > consumo4 :
            print ("el numero mayor es: ",consumo5)
        else :
            print ("nose encontro el numero mayor")