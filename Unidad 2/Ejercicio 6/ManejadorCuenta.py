from ClaseCuenta import Cuenta
import numpy as np
import csv

class ManejadorCuenta:
    __listaCuenta: np.array
    __dimension: int
    __cantidad: int
    __incremento: int

    def __init__(self):
        self.__listaCuenta = np.empty([0], dtype=Cuenta)
        self.__dimension = 0
        self.__cantidad = 0
        self.__incremento = 1

    def agregarCuenta(self, cuenta):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaCuenta.resize(self.__dimension)
        self.__listaCuenta[self.__cantidad] = cuenta
        self.__cantidad += 1

    def cargaCuentas(self):
        archivo = open("cuentasBilletera.csv")
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for linea in reader:
            if bandera:
                bandera = False
            else:
                self.agregarCuenta(Cuenta(linea[0], linea[1], linea[2], linea[3], linea[4], linea[5]))

    def buscarIndice(self, dni):
        indice = 0
        bandera = False
        ValorDeRetorno = None
        while indice < len(self.__listaCuenta) and bandera == False:
            if dni == self.__listaCuenta[indice].getDNI():
                ValorDeRetorno = indice
                bandera = True
            else:
                indice += 1
        return ValorDeRetorno

    def informarCliente(self, b):
        dni = int(input("Ingrese DNI de la cuenta a consultar: "))
        i = self.buscarIndice(dni)
        print("---DATOS DEL CLIENTE---")
        print("Apellido y nombre: {} {}     CVU: {}\nSaldo: ${:.2f}".format(self.__listaCuenta[i].getApellido(), self.__listaCuenta[i].getNombre(), self.__listaCuenta[i].getCVU(), self.__listaCuenta[i].getSaldo()))
    
    def establecerPorcentaje(self):
        porcentaje = float(input("Ingrese el nuevo porcentaje anual de rendimiento: "))
        i = 0
        while i < len(self.__listaCuenta):
            self.__listaCuenta[i].setPorcentaje(porcentaje)
            i += 1
        print("Porcentaje establecido con exito.")

    def incrementarSaldo(self):
        pdiario = self.__listaCuenta[0].getPorcentaje() / 365
        i = 0
        while i < len(self.__listaCuenta):
            self.__listaCuenta[i].setSaldo(self.__listaCuenta[i].getSaldo() + (self.__listaCuenta[i].getSaldo() * pdiario / 100))
            i += 1
        print("Saldo actualizado exitosamente.")
