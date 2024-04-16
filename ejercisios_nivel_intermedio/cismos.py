cismos1 = 0
cismos2 = 0
cismos3 = 0
cismos4 = 0
cismos5 = 0
ciudad1 = ""
ciudad2 = ""
ciudad3 = ""
ciudad4 = ""
ciudad5 = ""
eleccion = 0
while eleccion != 5:

    print("""
    indique la operacion
    1) registrar ciudad
    2) registrar cismo
    3) buscar cismos por la ciudad  
    4) informe de riesgos
    5) salir
    """)
    eleccion = int(input())

    if eleccion == 1:
        ciudad1 = input("ingrese el nombre de la primera ciudad: ")
        ciudad2 = input("ingrese el nombre de la segunda ciudad: ")
        ciudad3 = input("ingrese el nombre de la tercera ciudad: ")
        ciudad4 = input("ingrese el nombre de la cuarta ciudad: ")
        ciudad5 = input("ingrese el nombre de la quinta ciudad: ")


    if eleccion == 2:
        cismos1 =+ float(input(f"ingresa el nivel de los cismos de la ciudad {ciudad1}: "))
        cismos2 =+ float(input(f"ingresa el nivel de los cismos de la ciudad {ciudad2}: "))
        cismos3 =+ float(input(f"ingresa el nivel de los cismos de la ciudad {ciudad3}: "))
        cismos4 =+ float(input(f"ingresa el nivel de los cismos de la ciudad {ciudad4}: "))
        cismos5 =+ float(input(f"ingresa el nivel de los cismos de la ciudad {ciudad5}: "))

    if eleccion == 3:
        cismo1 = print(f"cismo de nivel {cismos1}")
        cismo2 = print(f"cismo de nivel {cismos2}")
        cismo3 = print(f"cismo de nivel {cismos3}")
        cismo4 = print(f"cismo de nivel {cismos4}")
        cismo5 = print(f"cismo de nivel {cismos5}")

    if  eleccion == 4:
        if cismos1 <= 2.5:
            print (f"no ay riesgo en la ciudad {ciudad1}")
        elif ((cismos1 >=2.6) and (cismos1 <=4.5)):
            print (f"ay riesgo medio bajo en la ciudad {ciudad1}")
        elif cismos1 >= 4.6:
            print(f"riesgo alto en la ciudad {ciudad1}")
        else:
            print("valor erroneo")
        
        if cismos2 <= 2.5:
            print (f"no ay riesgo en la ciudad {ciudad2}")
        elif ((cismos2 >=2.6) and (cismos2 <=4.5)):
            print (f"ay riesgo medio bajo en la ciudad {ciudad2}")
        elif cismos2 >= 4.6:
            print(f"riesgo alto en la ciudad {ciudad2}")
        else:
            print("valor erroneo")

        if cismos3 <= 2.5:
            print (f"no ay riesgo en la ciudad {ciudad3}")
        elif ((cismos3 >=2.6) and (cismos3 <=4.5)):
            print (f"ay riesgo medio bajo en la ciudad {ciudad3}")
        elif cismos3 >= 4.6:
            print(f"riesgo alto en la ciudad {ciudad3}")
        else:
            print("valor erroneo")

        if cismos4 <= 2.5:
            print (f"no ay riesgo en la ciudad {ciudad4}")
        elif ((cismos4 >=2.6) and (cismos4 <=4.5)):
            print (f"ay riesgo medio bajo en la ciudad {ciudad4}")
        elif cismos4 >= 4.6:
            print(f"riesgo alto en la ciudad {ciudad4}")
        else:
            print("valor erroneo")

        if cismos5 <= 2.5:
            print (f"no ay riesgo en la ciudad {ciudad5}")
        elif ((cismos5 >=2.6) and (cismos5 <=4.5)):
            print (f"ay riesgo medio bajo en la ciudad {ciudad5}")
        elif cismos5 >= 4.6:
            print(f"riesgo alto en la ciudad {ciudad5}")
        else:
            print("valor erroneo") 
