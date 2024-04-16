participantes = { "novato" : [], "intermedio": [], "experto" : [] }

def detcategoria(edad):
    if 15 <= edad <= 17:
        return "novato"
    elif 18 <= edad <= 20:
        return "Intermedio"
    elif 21 <= edad: 
        return "experto"
    else:
        return "no tiene la edad adecuada para jugar"
    
def registrojugadores():

    print ("al ingresar la edad se elijira en que categoria puede jugar el participante")
    print ("")
    print ("hay 3 categorias y estan categirisadas por edades")
    print ("15 a 16 años la categoria de novato")
    print ("17 a 20 años la categoria de intermedio")
    print ("20 en adelante la categoria de experto")
    idjugador = input(f"Ingrese el ID del jugador : ")
    nombre = input(f"Ingrese el nombre del jugador")
    edad = int(input("ingrese la edad del jugardor :"))
    categoria = detcategoria(edad)
    if categoria != "Fuera de rango":
        participantes[categoria].append({"id del jugador": idjugador, "Nombre": nombre, "Edad": edad, "Partidos Ganados": 0, "Partidos Empatados": 0, "Partidos Perdidos": 0})
        print(f"Jugador registrado en la categoría {categoria}.")
    else:
        print("Persona fuera del rango de participación.")

def mostrar_resultados():
    for categoria, listajugadores in participantes.items():
        if len(listajugadores) < 3:
            print(f"No se pueden mostrar resultados para la categoría {categoria} porque no tiene suficientes jugadores registrados.")
            return
    for categoria, listajugadores in participantes.items():
        listajugadores.sort(key=lambda x: (x["Partidos Ganados"] * 3 + x["Partidos Empatados"]), reverse=True)
        print(f"Resultados de la categoría {categoria}:")
        for jugador in listajugadores:
            print ("la informacion de los participantes es:  ")
            print(f"{jugador["Nombre"]} - ID: {jugador["ID"]}, Edad: {jugador["Edad"]}, Partidos Ganados: {jugador["Partidos Ganados"]}, Partidos Empatados: {jugador["Partidos Empatados"]}")

def registrar_puntos():
    print ("las categorias para ingresar son las sigueintes, novato, intermedio, experto")
    print ("al ingresar dependiendo de la edad se elijira en que categoria puede jugar el participante")
    categoria = input('Ingrese la categoria en la que el jugador participa: ')
    if categoria in participantes and len(participantes[categoria]) >= 3:
        idjugdor = input("Ingrese el ID del jugador para registrar puntos: ")
        print("el ID del jugador es ", idjugdor)
        jugador = next((jugador for jugador in participantes[categoria] if jugador["ID"] == idjugdor), None)
        if jugador:
            jugador["Partidos Ganados"] = int(input("Ingrese partidos ganados: "))
            jugador["Partidos Empatados"] = int(input("Ingrese partidos empatados: "))
            jugador["Partidos Perdidos"] = int(input("Ingrese partidos perdidos: "))
            print(f"Puntos actualizados para el jugador {jugador["Nombre"]}")
        else:
            print("el id del jugador no esta registrado ")
    else:
        print("faltan jugadores para iniciar las categorias")

eleccion = 0
while eleccion != 6:
    print("""
    indique la operacion
    1) añadir participantes 
    2) puntos y partidos ganados de los participantes y informacion de los participantes
    3) resultado final en las categorias
    4) salir
    """)
    
    eleccion = int(input("\t:)_"))

    if eleccion == 1:
        print ("registre los jugadores")
        print ("")
        registrojugadores()
    elif eleccion == 2:
        print ("ingrese los puntos de los jugadores en la diferentes categorias")
        print ("")
        registrar_puntos()
    elif eleccion == 3:
        print ("resultado de puntos en las diferentes categorias")
        print ("")
        mostrar_resultados()
    elif eleccion == 4:
        print ("saliendo del programa")
        print ("en unos momentos sale del programa")
        break
    else:
        print ("esta opcion no esta registrada vuelva a intentarlo")