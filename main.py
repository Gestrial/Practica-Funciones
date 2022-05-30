


from inputs import choose

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

        opcion3 = input("Desea calcular algo mas ? S/N ")
        if opcion3 == "N":
            print("Hasta la proxima.")
            break
        elif opcion3 == "S":
            continue

main()


