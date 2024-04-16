
numeros = []
eleccion = 0

def total_numeros_pares(lista):
    return sum(1 for num in lista if num % 2 == 0)

def promedio_numeros_pares(lista):
    pares = [num for num in lista if num % 2 == 0]
    if pares:
        return sum(pares) / len(pares)
    else:
        return 0

def promedio_numeros_impares(lista):
    impares = [num for num in lista if num % 2 != 0]
    if impares:
        return sum(impares) / len(impares)
    else:
        return 0

def contar_menores_que_10(lista):
    return sum(1 for num in lista if num < 10)

def contar_entre_20_y_50(lista):
    return sum(1 for num in lista if 20 <= num <= 50)

def contar_mayores_que_100(lista):
    return sum(1 for num in lista if num > 100)

while eleccion != 8:

    print("""
    Indique la operacion:
    1) Ingresar un número
    2) Total de números pares ingresados
    3) Promedio de los números pares
    4) Promedio de los números impares
    5) Cuántos números son menores que 10
    6) Cuántos números están entre 20 y 50
    7) Cuántos números son mayores que 100
    8) Salir
    """)
    eleccion = int(input())

    if eleccion == 1:
        numero = int(input("Ingrese un número: "))
        numeros.append(numero)

    elif eleccion == 2:
        print("Total de números pares ingresados:", total_numeros_pares(numeros))

    elif eleccion == 3:
        print("Promedio de los números pares:", promedio_numeros_pares(numeros))

    elif eleccion == 4:
        print("Promedio de los números impares:", promedio_numeros_impares(numeros))

    elif eleccion == 5:
        print("Cuantos números son menores que 10:", contar_menores_que_10(numeros))

    elif eleccion == 6:
        print("Cuantos números están entre 20 y 50:", contar_entre_20_y_50(numeros))

    elif eleccion == 7:
        print("Cuantos números son mayores que 100:", contar_mayores_que_100(numeros))

print("¡Hasta luego!")
