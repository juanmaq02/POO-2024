from ClaseLadrillo import Ladrillo
import os, random

class ManejadorLadrillo:
    __listaLadrillo: list

    def __init__(self):
        self.__listaLadrillo = []

    def agregarLadrillo(self, Ladrillo):
        self.__listaLadrillo.append(Ladrillo)

    def cargaLadrillo(self, b):
        c = len(self.__listaLadrillo)
        cantl = int(input("Ingrese cantidad de ladrillos a encargar (0 para finalizar): "))
        while cantl != 0:
            matP = random.randint(0, 3)
            matP = float(matP)
            self.agregarLadrillo(Ladrillo(cantl, c + 1, matP, cantl * 60))
            os.system('cls')
            print("PEDIDO {}:\n--------------".format(c + 1))
            print("\nMateriales refractarios:")
            b.muestraMaterialesR()
            mat = int(input("Ingrese N° de material a agregar: "))
            assert mat > 0 and mat < (len(b._ManejadorMaterialR__listaMaterialR) + 1), "Numero de material incorrecto."
            while mat != 0:
                cantm = int(input("Ingrese cantidad: "))
                assert cantm != 0, "Cantidad incorrecta."
                self.__listaLadrillo[c].agregarMaterialR(b._ManejadorMaterialR__listaMaterialR[mat - 1], cantm)
                os.system('cls')
                print("Material/es agregado exitosamente.")
                os.system('pause')
                os.system('cls')
                print("\nMateriales refractarios:")
                b.muestraMaterialesR()
                mat = int(input("Ingrese N° de material (0 para finalizar): "))
                assert mat >= 0 and mat < (len(b._ManejadorMaterialR__listaMaterialR) + 1), "Numero de material incorrecto."
            os.system('cls')
            print("Pedido cargado exitosamente.")
            c += 1
            os.system('pause')
            os.system('cls')
            cantl = int(input("Ingrese cantidad de ladrillos a encargar (0 para finalizar): "))

    def detallarMaterialR(self):
        id = int(input("Ingrese identificador de ladrillo: "))
        band = False
        for ladrillo in self.__listaLadrillo:
            if ladrillo.getID() == id:s
                for materialR in ladrillo.getMaterialR():
                    print("Costo: ${}   Caracteristica: {}".format(materialR.getCostoAdi(), materialR.getCaracteristicas()))
        if not band:
            print("No se encontró el ladrillo con el identificador ingresado.")

    def costoTotal(self):
        for ladrillo in self.__listaLadrillo:
            ct = float(ladrillo.getCosto())
            for materialR in ladrillo.getMaterialR():
                ct += float(materialR.getCostoAdi())
            print("COSTO TOTAL PEDIDO {}: ${:.2f}".format(ladrillo.getID(), ct))

    def mostrarCostoAdi(self):
        print("N° Identificador         Material          Costo asociado")
        for ladrillo in self.__listaLadrillo:
            c = 0
            for materialR in ladrillo.getMaterialR():
                c += float(materialR.getCostoAdi())
            print("{:<25}{:<18}${:.2f}".format(ladrillo.getID(), len(ladrillo.getMaterialR()), c))