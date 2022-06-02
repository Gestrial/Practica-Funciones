from function import calcularIva
from inputs import country, facturaTotal

alicuotas = {'argentina' : 21,'chile' : 19,'brasil' : 17,'peru' : 18,
'uruguay' : 22,'dominicana' : 18,'mexico' : 16,'colombia' : 16,
'honduras' : 15,'nicaragua' : 15,'bolivia' : 13,
'costarica' : 13,'elsalvador' : 13,'ecuador' : 12,
'guatemala' : 12,'venezuela' : 12,'puertorico' : 11.5,
'paraguay' : 10,'panama' : 7}

def ivaLatinoamericano():
    print("------------------")
    print("-------IVA--------")
    print("------------------")
    totalFactura = facturaTotal()
    while True:
        pais = country()
        if pais.lower() not in alicuotas:
            print("Pais invalido")
            continue
        totalIva = calcularIva(totalFactura,alicuotas[pais.lower()])
        print(f"La factura con el monto {totalFactura} tiene un iva de: {totalIva} ")
        return totalIva

