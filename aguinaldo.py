from function import aguinaldos
from inputs import cantMeses, salario

#EJECUTAR DESDE MAIN

def aguinaldo():
    print("------------------------")
    print("-------AGUINALDO--------")
    print("------------------------")
    while True:
        cantMeses2 = cantMeses()
        salario2 = salario()
        if salario2 > 0:
            salario3 = aguinaldos(salario2,cantMeses2)
            print(f"Su salario mas alto fue de {salario2} en {cantMeses2} meses trabajados, y le corresponden: ${salario3} de aguinaldo ")
            return salario3
        else:
            print("Ingresa un salario positivo")
            continue
