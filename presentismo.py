from function import antiguedades,presentismo2
from inputs import antiguedad, sueldoBasico

def presentismo():
    while True:
        sueldoBasico2 = sueldoBasico()
        if sueldoBasico2 > 0:
            antiguedad2 = antiguedad()
            totalAntiguedad = antiguedades(sueldoBasico2,antiguedad2)
            sueldoAntiguedad = sueldoBasico2 + totalAntiguedad
            totalPresentismo = presentismo2(sueldoAntiguedad)
            print(f"Su presentismo correspondiente es de : {totalPresentismo} ")
            return totalPresentismo
        else:
            print("Ingresa un sueldo positivo porfavor.")
            continue

