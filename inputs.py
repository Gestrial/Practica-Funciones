def salario():
    salario = float(input("Ingresa tu salario percibido mas alto hasta la fecha: "))
    return salario

def cantMeses():
    cantMeses = int(input("Ingresa la cantidad de meses trabajados: "))
    return cantMeses

def sueldoBasico():
    sueldobasico3 = float(input("Ingresa el monto total de tu sueldo basico: "))
    return sueldobasico3

def antiguedad():
    antiguedad2 = int(input("Ingresa tu antiguedad en meses: "))
    return antiguedad2

def choose():
    while True:
        opcion = int(input("Elija que desea calcular segun su numero: \n1)AGUINALDO\n2)IVA\n3)PRESENTISMO\n"))
        if opcion == 1 or opcion == 2 or opcion == 3:
            return opcion
        else:
            print("Ingrese una opcion correcta porfavor.")
            

def facturaTotal():
    total = float(input("Ingresa el monto total de tu factura: "))
    return total

def country():
    f = input("Ingresa un pais de latinoamerica: ")
    return f

def pregunta():
    while True:
        a = input("Desea calcular algo mas ? S/N ")
        if a.upper() == "S" or a.upper() == "N":
            return a.upper()
        else:
            print("Ingresa una opcion correcta.")
            continue