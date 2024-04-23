from ClaseFecha import Fecha
import csv

class ManejadorFecha:
    __listaFecha: list
    def __init__(self):
        self.__listaFecha = []
    def agregarFecha(self, fecha):
        self.__listaFecha.append(fecha)
    def cargaFechas(self):
        archivo = open("fechasFutbol.csv")
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for linea in reader:
            if bandera:
                bandera = False
            else:
                self.agregarFecha(Fecha(linea[0], linea[1], linea[2], linea[3], linea[4]))
    def actualizarTabla(self, a):
        i = 0
        while i < len(a._ManejadorEquipo__listaEquipo):
            tgaf = 0
            tgec = 0
            tpts = 0
            j = 0
            while j < len(self.__listaFecha):
                if a._ManejadorEquipo__listaEquipo[i].getIDEquipo() == self.__listaFecha[j].getIDEquipoL():
                    tgaf += int(self.__listaFecha[j].getGolesL())
                    tgec += int(self.__listaFecha[j].getGolesV())
                    if int(self.__listaFecha[j].getGolesL()) < int(self.__listaFecha[j].getGolesV()):
                        tpts += 0
                    elif int(self.__listaFecha[j].getGolesL()) > int(self.__listaFecha[j].getGolesV()):
                        tpts += 3
                    else:
                        tpts += 1
                elif a._ManejadorEquipo__listaEquipo[i].getIDEquipo() == self.__listaFecha[j].getIDEquipoV():
                    tgaf += int(self.__listaFecha[j].getGolesV())
                    tgec += int(self.__listaFecha[j].getGolesL())
                    if int(self.__listaFecha[j].getGolesL()) < int(self.__listaFecha[j].getGolesV()):
                        tpts += 3
                    elif int(self.__listaFecha[j].getGolesL()) > int(self.__listaFecha[j].getGolesV()):
                        tpts += 0
                    else:
                        tpts += 1
                j += 1
            a._ManejadorEquipo__listaEquipo[i].setGolesAF(tgaf)
            a._ManejadorEquipo__listaEquipo[i].setGolesEC(tgec)
            a._ManejadorEquipo__listaEquipo[i].setDifGoles()
            a._ManejadorEquipo__listaEquipo[i].setPuntos(tpts)
            i += 1
        print("Tabla actualizada exitosamente.")


