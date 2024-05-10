from ClaseTransaccion import Transaccion
import csv

class ManejadorTransaccion:

    __listaTransaccion: list

    def __init__(self):
        self.__listaTransaccion = []

    def agregarTransaccion(self, transaccion):
        self.__listaTransaccion.append(transaccion)
        
    def cargaTransacciones(self):
        archivo = open("transaccionesBilletera.csv")
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for linea in reader:
            if bandera:
                bandera = False
            else:
                self.agregarTransaccion(Transaccion(linea[0], linea[1], linea[2], linea[3]))

    def actualizarSaldo(self, a):
        i = 0
        while i < len(a._ManejadorCuenta__listaCuenta):
            j = 0
            saldo = 0
            while j < len(self.__listaTransaccion):
                if a._ManejadorCuenta__listaCuenta[i].getCVU() == self.__listaTransaccion[j].getCVU():
                    saldo += float(self.__listaTransaccion[j].getImporte())
                j += 1
            a._ManejadorCuenta__listaCuenta[i].setSaldo(float(a._ManejadorCuenta__listaCuenta[i].getSaldo()) + saldo)
            i += 1