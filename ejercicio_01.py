def menu():
    print("\n--MENÚ--")
    print("1.Encontrar suma, promedio, multiplos de 3 de n numeros")
    print("2.Calcular el área y perimetro de un rectangulo")
    print("3.Verificar si un numero es primo o no")
    print("4.Calcular el promedio de n calificaciones")
    print("5.Calcular el numero mayor y el menor de n números ")
    print("6.Calculadora con operaciones básicas")
    print("7.Salir")

def suma_total(lista):
    suma_uno=sum(lista)
    print("\n--SUMA--")
    print(f"La suma de los números es: {suma_uno}")
def promedio(lista):
    prom=sum(lista)/len(lista)
    print("\n--PROMEDIO--")
    print(f"El promedio de los números ingresados es: {prom:.2f}")
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

def area():
    b=int(input("Ingrese el tamaño de la base del rectángulo:"))
    a=int(input("Ingrese la altura del rectángulo: "))
    print("\n--ÁREA--")
    print(f"El area del rectángulo es de: {a*b} unidades cuadradas")
def perimetro():
    b = int(input("Ingrese el tamaño de la base del rectángulo:"))
    a = int(input("Ingrese la altura del rectángulo: "))
    print("\n--PERIMETRO--")
    print(f"El perimetro del rectángulo es:{(2*a)+(2*b)} unidades")

def primo():
    num=int(input("Ingrese el numero que desea comprobar si es primo o no:"))
    if num<=1:
        print(f"{num} No es un numero primo")
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print(f"{num} no es un número primo")
                return
        print(f"{num} es un número primo")
def promedio_calificaciones(lista):
    g=sum(lista)/len(lista)
    print("\n--PROMEDIO--")
    print(f"El promedio de las calificaciones ingresadas es:{g:.2f}")
def mayores_85_60(lista):
    contador=0
    contador_dos=0
    for numero in lista:
        if numero>=85:
            contador+=1
        elif numero<60:
            contador_dos+=1
    print("\n--CONTADOR--")
    print(f"Hay {contador} notas mayores o igual a 85")
    print(f"Hay {contador_dos} en zona de riesgo")

def agregar_a_lista():
    q = int(input("\nIngrese la cantidad de numeros que quiere agregar : "))
    for i in range(q):
        p = int(input("Ingrese los numeros de los que desee: "))
        lista.append(p)

def agregar_a_lista_dos():
    q = int(input("\nIngrese la cantidad de calificaciones que quiere agregar: "))
    for i in range(q):
        p = int(input("Ingrese la calificación que desea agregar:"))
        lista_dos.append(p)

def agregar_a_lista_tres():
    q = int(input("\nIngrese la cantidad de numeros que quiere agregar a la lista : "))
    for i in range(q):
        p = int(input("Ingrese los numeros de los que desee: "))
        lista_tres.append(p)

def num_mayor(lista):
    mayor=max(lista)
    print("\n--MAYOR Y MENOR--")
    print("El numero mayor en la lista es:", mayor)
def num_menor(lista):
    menor=min(lista)
    print("El numero menor en la lista es:", menor)

def frecuencia(lista):
    print("\n--FRECUENCIA--")
    frecuencias = {}

    for numero in lista:
        if numero in frecuencias:
            frecuencias[numero] += 1
        else:
            frecuencias[numero] = 1

    for numero, cantidad in frecuencias.items():
        print("El número ",numero,f" se repite {cantidad} vez/veces")

def calculadora():
    print("\n--CALCULADORA--")
    a=int(input("Ingrese el primer numero: "))
    b=int(input("Ingrese el segundo numero: "))
    print(f"El resultado de {a}+{b} es: {a+b}")
    print(f"El resultado de {a}-{b} es: {a-b}")
    print(f"El resultado de {a}X{b} es: {a*b}")
    print(f"El resultado de {a}/{b} es: {a/b:.2f}")


while True:
    lista=[]
    lista_dos=[]
    lista_tres=[]
    menu()
    option=input("\nSeleccione una opción del menú: ")

    match option:
        case "1":
            agregar_a_lista()
            suma_total(lista)
            promedio(lista)
            numeros_positivos_ceros(lista)
            multiplos_tres(lista)

        case "2":
            area()
            perimetro()

        case "3":
            primo()

        case "4":
            agregar_a_lista_dos()
            promedio_calificaciones(lista_dos)
            mayores_85_60(lista_dos)
        case "5":
            agregar_a_lista_tres()
            num_mayor(lista_tres)
            num_menor(lista_tres)
            frecuencia(lista_tres)
        case "6":
            calculadora()
        case "7":
            print("Gracias por usar el programa.")
            break

