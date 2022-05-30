from function import aguinaldos
from inputs import cantMeses, salario

def aguinaldo():
    print("------------------------")
    print("-------AGUINALDO--------")
    print("------------------------")
    while True:
        salario2 = salario()
        cantMeses2 = cantMeses()
        if salario2 > 0:
            salario3 = aguinaldos(salario2,cantMeses2)
            print(f"Su aguinaldo correspondiente es de: {salario3} ")
            return salario3
        else:
            print("Ingresa un salario positivo")
            continue
