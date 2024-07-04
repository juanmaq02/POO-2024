from ClaseEdificio import Edificio
import csv
import os

class ManejadorEdificio:
    __listaEdificio: list

    def __init__(self):
        self.__listaEdificio = []
    
    def agregarEdificio(self, edificio):
        self.__listaEdificio.append(edificio)
    
    def cargaEdificiosYDepartamentos(self):
        archivo = open('EdificioNorte.csv')
        reader = csv.reader(archivo, delimiter=';')
        i = -1
        for fila in reader:
            if len(fila) == 7:
                print('a')
                self.agregarEdificio(Edificio(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5]))
                i += 1
            else:
                self.__listaEdificio[i].setDepartamento(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7])
        archivo.close()

    def buscaIndice(self, nom):
        bandera = False
        ValorDeRetorno = None
        indice = 0
        while indice < len(self.__listaEdificio) and bandera == False:
            if self.__listaEdificio[indice].getNombre() == nom:
                ValorDeRetorno = indice
                bandera = True
            else:
                indice += 1
        return ValorDeRetorno

    def propietarios(self):
        nom = input("Ingrese nombre del edificio: ")
        i = self.buscaIndice(nom)
        if i != None:
            print("Propietarios de los departamentos del edificio {}:\n--------------------------------------------".format(nom))
            j = 0
            while j < len(self.__listaEdificio[i].getDepartamentos()):
                print("Nombre y Apellido: {}".format(self.__listaEdificio[i].getDepartamentos()[j].getNomYApe()))
                j += 1
        else:
            print("No se ha encontrado el edificio con el nombre ingresado.")

    def consultarSuperficie(self):
        nom = input("Ingrese nombre del edificio: ")
        i = self.buscaIndice(nom)
        if i != None:
            j = 0
            tot = 0
            while j < len(self.__listaEdificio[i].getDepartamentos()):
                tot += float(self.__listaEdificio[i].getDepartamentos()[j].getSuperficie())
                j += 1
            print("La superficie total del edificio {} es de: {} metros cuadrados.".format(nom, tot))
        else:
            print("No se ha encontrado el edificio con el nombre ingresado.")

    def consultarSuperficieDepartamento(self):
        nom = input("Ingrese el nombre del propietario: ")
        i = 0
        bandera = False
        sup = []
        while i < len(self.__listaEdificio) and bandera == False:
            j = 0
            while j < len(self.__listaEdificio[i].getDepartamentos()) and bandera == False:
                if self.__listaEdificio[i].getDepartamentos()[j].getNomYApe() == nom:
                    bandera = True
                j += 1
            i += 1
        if bandera:
            i = 0
            ed = []
            dep = []
            print("Departamentos del propietario {}:".format(nom))
            while i < len(self.__listaEdificio):
                tot = 0
                j = 0
                print("\nEdificio {} {}:\n----------------------------------".format(i + 1, self.__listaEdificio[i].getNombre()))
                bandera2 = False
                while j < len(self.__listaEdificio[i].getDepartamentos()):
                    tot += float(self.__listaEdificio[i].getDepartamentos()[j].getSuperficie())
                    if nom == self.__listaEdificio[i].getDepartamentos()[j].getNomYApe():
                        print("ID del departamento: {}".format(self.__listaEdificio[i].getDepartamentos()[j].getID()))
                        bandera2 = True
                        ed.append(i)
                        dep.append(j)
                    j += 1
                if not bandera2:
                    print("No posee.")
                sup.append(tot)
                i += 1
            try:
                i = int(input("Ingrese el numero del edificio del departamento a consultar: "))
                j = int(input("Ingrese ID del departamento: "))
            except ValueError:
                print("Valor incorrecto.")
                return
            if i-1 in ed and j-1 in dep:
                por = (float(self.__listaEdificio[i-1].getDepartamentos()[j-1].getSuperficie()) * 100) / sup[i - 1]
                print("Superficie total del departamento ingresado: {} metros cuadrados y representa el {:.2f} porciento del total. ".format(self.__listaEdificio[i-1].getDepartamentos()[j-1].getSuperficie(), por))
            else:
                print("Los valores ingresados no corresponden a los solicitados.")
        else:
            print("No se ha encontrado el propietario ingresado.")
    
    def consultarDepartamentos(self):
        piso = input("Ingrese numero de piso: ")
        i = 0
        while i < len(self.__listaEdificio):
            j = 0
            cont = 0
            print("Edificio {}:".format(self.__listaEdificio[i].getNombre()))
            while j < len(self.__listaEdificio[i].getDepartamentos()):
                if self.__listaEdificio[i].getDepartamentos()[j].getNumPiso() == piso and int(self.__listaEdificio[i].getDepartamentos()[j].getCantDorm()) == 3 and int(self.__listaEdificio[i].getDepartamentos()[j].getCantBanios()) > 1:
                    cont += 1
                j += 1
            if cont != 0:
                print("Hay {} departamento/s con 3 dormitorios y más de un baño.".format(cont))
            else:
                print("No se encontraron departamentos con 3 dormitorios y más de un baño.")
            i += 1