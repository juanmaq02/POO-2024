from ClaseEquipo import Equipo
import csv
import os

class ManejadorEquipo:
    __listaEquipo: list
    def __init__(self):
        self.__listaEquipo = []
    def agregarEquipo(self, equipo):
        self.__listaEquipo.append(equipo)
    def cargaEquipos(self):
        archivo = open("equipos2024.csv")
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for linea in reader:
            if bandera:
                bandera = False
            else:
                self.agregarEquipo(Equipo(linea[0], linea[1], linea[2], linea[3], linea[4], linea[5]))
    def buscarIndice(self, nombre):
        bandera = False
        indice = 0
        ValorDeRetorno = None
        while indice < len(self.__listaEquipo) and bandera == False:
            if self.__listaEquipo[indice].getNombre() == nombre:
                ValorDeRetorno = indice
                bandera = True
            else:
                indice += 1
        return ValorDeRetorno
    def listadoEquipo(self, b):
        nombre = input("Ingrese el nombre del equipo a consultar: ")
        indice = self.buscarIndice(nombre)
        os.system('cls')
        if indice != None:
            print("Equipo: {}".format(nombre))
            print("Fecha         Goles a Favor   Goles en Contra   Diferencia de Goles   Puntos")
            i = 0
            tgaf = 0
            tgec = 0
            tdif = 0
            tpts = 0
            while i < len(b._ManejadorFecha__listaFecha):
                if self.__listaEquipo[indice].getIDEquipo() == b._ManejadorFecha__listaFecha[i].getIDEquipoL():
                    dif = int(b._ManejadorFecha__listaFecha[i].getGolesL()) - int(b._ManejadorFecha__listaFecha[i].getGolesV())
                    if dif < 0:
                        pts = 0
                    elif dif == 0:
                        pts = 1
                    else:
                        pts = 3
                    print("{:<14}{:<16}{:<18}{:<22}{}".format(b._ManejadorFecha__listaFecha[i].getFecha(), b._ManejadorFecha__listaFecha[i].getGolesL(), b._ManejadorFecha__listaFecha[i].getGolesV(), dif, pts))
                    tgaf += int(b._ManejadorFecha__listaFecha[i].getGolesL())
                    tgec += int(b._ManejadorFecha__listaFecha[i].getGolesV())
                    tdif += dif
                    tpts += pts
                elif self.__listaEquipo[indice].getIDEquipo() == b._ManejadorFecha__listaFecha[i].getIDEquipoV():
                    dif = int(b._ManejadorFecha__listaFecha[i].getGolesV()) - int(b._ManejadorFecha__listaFecha[i].getGolesL())
                    if dif < 0:
                        pts = 0
                    elif dif == 0:
                        pts = 1
                    else:
                        pts = 3
                    print("{:<14}{:<16}{:<18}{:<22}{}".format(b._ManejadorFecha__listaFecha[i].getFecha(), b._ManejadorFecha__listaFecha[i].getGolesV(), b._ManejadorFecha__listaFecha[i].getGolesL(), dif, pts))
                    tgaf += int(b._ManejadorFecha__listaFecha[i].getGolesV())
                    tgec += int(b._ManejadorFecha__listaFecha[i].getGolesL())
                    tdif += dif
                    tpts += pts
                i += 1
            print("----------------------------------------------------------------------------")
            print("Totales:      {:<16}{:<18}{:<22}{}".format(tgaf, tgec, tdif, tpts))
        else:
            print("No se ha encontrado el equipo con ese nombre.")
    def tablaDePosiciones(self):
        self.__listaEquipo.sort(reverse=True)
        i = 0
        print("Equipo                          GAF  GEC  +/-  PTS\n" + ('-' * 50))
        while i < len(self.__listaEquipo):
            print("{:<32}{:<5}{:<5}{:<5}{}".format(self.__listaEquipo[i].getNombre(), self.__listaEquipo[i].getGolesAF(), self.__listaEquipo[i].getGolesEC(), self.__listaEquipo[i].getDifGoles(), self.__listaEquipo[i].getPuntos()))
            i += 1
    def guardarTabla(self):
        self.__listaEquipo.sort(reverse=True)
        archivo = open("equipos2024N.csv", 'w', encoding='UTF8', newline='')
        writer = csv.writer(archivo, delimiter=';')
        i = 0
        writer.writerow(["Identificador", "Nombre", "Goles a Favor", "Goles en Contra", "Diferencia de Goles", "Puntos"])
        while i < len(self.__listaEquipo):
            writer.writerow([self.__listaEquipo[i].getIDEquipo(), self.__listaEquipo[i].getNombre(), self.__listaEquipo[i].getGolesAF(), self.__listaEquipo[i].getGolesEC(), self.__listaEquipo[i].getDifGoles(), self.__listaEquipo[i].getPuntos()])
            i += 1
        print("Tabla guardada exitosamente.")