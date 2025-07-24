def menu():
    print("\n--MENÚ--")
    print("1.Encontrar suma, promedio, multiplos de 3 de n numeros")
    print("2.Calcular el área y perimetro de un rectangulo")
    print("3.Verificar si un numero es primo o no")
    print("4.Calcular el promedio de n calificaciones")
    print("5.Calcular el numero mayor y el menor de n números ")
    print("6.Calculadora")
    print("7.Salir")

def suma_total(lista):
    suma_uno=sum(lista)
    print("\n--SUMA--")
    print(f"La suma de los números es: {suma_uno}")
def promedio(lista):
    prom=sum(lista)/len(lista)
    print("\n--PROMEDIO--")
    print(f"El promedio de los números ingresados es:{prom:.2f}")
def numeros_positivos_ceros(lista):
    positivos = 0
    negativos = 0
    ceros = 0
    for numero in lista:
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        elif numero==0:
            ceros+=1
    print("\n--POSITIVOS, NEGATIVOS Y CEROS--")
    print("Cantidad de positivos:", positivos)
    print("Cantidad de negativos:", negativos)
    print("Cantidad de ceros:", ceros)

def multiplos_tres(lista):
    contador=0
    print("\n--MÚLTIPLOS--")
    for numero in lista:
        if numero%3==0:
            print(f"{numero} es múltiplo de 3.")
            contador+=1
    print("En total hay", contador, "multiplos de 3.")

while True:
    lista=[]
    menu()
    option=input("\nSeleccione una opción del menú: ")

    match option:
        case "1":
            q = int(input("\nIngrese la cantidad de numeros que quiere agregar : "))
            for i in range(q):
                p = int(input("Ingrese los numeros de los que desee: "))
                lista.append(p)
            suma_total(lista)
            promedio(lista)
            numeros_positivos_ceros(lista)
            multiplos_tres(lista)

        case "2":
            print()
        case "3":
            print()
        case "4":
            print()
        case "5":
            print()
        case "6":
            print()
        case "7":
            print("Gracias por usar el programa.")
            break

