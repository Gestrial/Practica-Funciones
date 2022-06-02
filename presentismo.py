from function import antiguedades,presentismo2
from inputs import antiguedad, sueldoBasico

#EJECUTAR DESDE MAIN

def presentismo():
    while True:
        sueldoBasico2 = sueldoBasico()
        if sueldoBasico2 > 0:
            antiguedad2 = antiguedad()
            totalAntiguedad = antiguedades(sueldoBasico2,antiguedad2)
            sueldoAntiguedad = sueldoBasico2 + totalAntiguedad
            totalPresentismo = presentismo2(sueldoAntiguedad)
            print(f"El presentismo correspondiente a su sueldo basico {sueldoBasico2} es de: {totalPresentismo} ")
            return totalPresentismo
        else:
            print("Ingresa un sueldo positivo porfavor.")
            continue

