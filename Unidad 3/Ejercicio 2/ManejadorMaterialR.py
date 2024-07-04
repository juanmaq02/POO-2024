from ClaseMaterialR import MaterialR
import csv

class ManejadorMaterialR:
    __listaMaterialR: list

    def __init__(self):
        self.__listaMaterialR = []

    def agregarMaterialR(self, materialR):
        self.__listaMaterialR.append(materialR)

    def cargaMaterialR(self):
        archivo = open("materiales.csv")
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for linea in reader:
            if bandera:
                bandera = False
            else:
                self.agregarMaterialR(MaterialR(int(linea[0]), linea[1], float(linea[2]), float(linea[3])))
        archivo.close()

    def muestraMaterialesR(self):
        for materialR in self.__listaMaterialR:
            print(materialR)