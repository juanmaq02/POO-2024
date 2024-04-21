from ClaseMoto import Moto
import csv
import os

class ManejadorMoto:
    __listaMoto: list
    def __init__(self):
        self.__listaMoto = []
    def agregarMoto(self, moto):
        self.__listaMoto.append(moto)
    def cargaMoto(self):
        archivo = open('datosMotos.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for linea in reader:
            if bandera:
                bandera = False
            else:
                self.agregarMoto(Moto(linea[0], linea[1], linea[2], linea[3], linea[4]))
        self.__listaMoto.sort()
    def buscaPatente(self, patente):
        indice = 0
        bandera = False
        ValorDeRetorno = None
        while indice < len(self.__listaMoto) and bandera == False:
            if patente == self.__listaMoto[indice].getPatente():
                ValorDeRetorno = indice
                bandera = True
            else:
                indice += 1
        return ValorDeRetorno
    def datosConductor(self, b):
        acum = 0
        cont = 0
        j = 0
        patente = input("Ingrese patente: ")
        i = self.buscaPatente(patente)
        if i != None:
            while j < len(b._ManejadorPedido__listaPedido):
                if b._ManejadorPedido__listaPedido[j].getPatente() == patente:
                    acum += float(b._ManejadorPedido__listaPedido[j].getTiempoR())
                    cont += 1
                j += 1
            if cont != 0:
                print("Nombre y apellido: {} {}   Marca de la moto: {} \nKilometraje de la moto: {} km   Tiempo promedio real: {:.2f} min".format(self.__listaMoto[i].getNombre(), self.__listaMoto[i].getApellido(), self.__listaMoto[i].getMarca(), self.__listaMoto[i].getKm(), acum / cont))
            else:
                print("Nombre y apellido: {} {}   Marca de la moto: {} \nKilometraje de la moto: {} km   Tiempo promedio real: Sin pedidos realizados.".format(self.__listaMoto[i].getNombre(), self.__listaMoto[i].getApellido(), self.__listaMoto[i].getMarca(), self.__listaMoto[i].getKm()))
        else:
            print("Patente no encontrada.")
        os.system('pause')
    def listarMotos(self, b):
        b._ManejadorPedido__listaPedido.sort()
        i = 0
        while i < len(self.__listaMoto):
            j = 0
            print("Patente de Moto: {}\nConductor: {} {}".format(self.__listaMoto[i].getPatente(), self.__listaMoto[i].getNombre(), self.__listaMoto[i].getApellido()))
            print("Identificador de pedido   Tiempo Estimado   Tiempo real    Precio")
            tot = 0
            while j < len(b._ManejadorPedido__listaPedido):
                if self.__listaMoto[i].getPatente() == b._ManejadorPedido__listaPedido[j].getPatente():
                    print("{:<26}{:<19}{:<14}${:.2f}".format(b._ManejadorPedido__listaPedido[j].getComidas(), b._ManejadorPedido__listaPedido[j].getTiempoE(), b._ManejadorPedido__listaPedido[j].getTiempoR(), float(b._ManejadorPedido__listaPedido[j].getPrecio())))
                    tot += float(b._ManejadorPedido__listaPedido[j].getPrecio())
                j += 1
            print("Total:" + ' ' * 53 + "${:.2f}".format(tot))
            print("Comision:" + ' ' * 50 + "${:.2f}\n".format(tot * (20 / 100)))
            i += 1
        os.system('pause')
