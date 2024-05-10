from ClasePedido import Pedido
import csv
import os

class ManejadorPedido:
    __listaPedido: list
    def __init__(self):
        self.__listaPedido = []
    def agregarPedido(self, pedido):
        self.__listaPedido.append(pedido)
    def cargaPedido(self):
        archivo = open('datosPedidos.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for linea in reader:
            if bandera:
                bandera = False
            else:
                self.agregarPedido(Pedido(linea[0], linea[1], linea[2], linea[3], linea[5], linea[4]))
    def nuevoPedido(self, a):
        patente = input("Ingrese patente de la moto: ")
        i = a.buscaPatente(patente)
        if i != None:
            id = input("Ingrese ID del pedido: ")    
            pedido = input("Ingrese su pedido: ")
            tiempo = int(input("Ingrese el tiempo estimado (en minutos): "))
            precio = float(input("Ingrese el precio del pedido: $"))
            self.agregarPedido(Pedido(patente, id, pedido, tiempo, precio))
            print("Pedido agregado con exito.")
        else:
            print("No se ha encontrado una moto con la patente solicitada.")
        os.system('pause')
    def modificarTiempoR(self):
        patente = input("Ingrese patente del pedido a modificar: ")
        i = 0
        bandera = False
        print("---PEDIDOS CON PATENTE {}---".format(patente))
        while i < len(self.__listaPedido):
            if self.__listaPedido[i].getPatente() == patente:
                bandera = True
                print("ID: {} Pedido: {}".format(self.__listaPedido[i].getID(), self.__listaPedido[i].getComidas()))
            i += 1
        if bandera == False:
            print("No se encontraron pedidos con esa patente.")
            return
        else:
            id = input("Ingrese ID del pedido a modificar: ")
            i = 0
            while i < len(self.__listaPedido):
                if self.__listaPedido[i].getID() == id:
                    tiempo = int(input("Ingrese tiempo real del pedido (en minutos): "))
                    self.__listaPedido[i].setTiempoR(tiempo)
                    print("Tiempo cambiado exitosamente.")
                i += 1
        os.system('pause')
                    
