#ARCHIVO PRINCIPAL
from inputs import choose, pregunta

def main():
    while True:
        opcion2 = choose()
        if opcion2 == 1:
            from aguinaldo import aguinaldo
            aguinaldo()
        elif opcion2 == 2:
            from iva import ivaLatinoamericano
            ivaLatinoamericano()
        elif opcion2 == 3:
            from presentismo import presentismo
            presentismo()

        opcion3 = pregunta()
        if opcion3 == "N":
            print("Hasta la proxima.")
            break
        elif opcion3 == "S":
            continue

main()


