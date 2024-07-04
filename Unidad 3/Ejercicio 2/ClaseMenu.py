from ManejadorLadrillo import ManejadorLadrillo
from ManejadorMaterialR import ManejadorMaterialR
import os

class Menu:
    __opcion: int

    def __init__(self):
        self.__opcion = None
    
    def MenuDeOpciones(self, a, b):
        while self.__opcion != '0':
            os.system('cls')
            print('''
                  ---MENÚ DE OPCIONES---
                  1. Realizar pedido.
                  2. Consultar costo y características de los materiales refractarios de un ladrillo.
                  3. Consultar costo total de pedidos de ladrillos.
                  4. Consultar costo adicional por pedido de ladrillos.
                  
                  0. Salir.''')
            self.__opcion = input(">>> ")
            if self.__opcion == '1':
                os.system('cls')
                a.cargaLadrillo(b)
            elif self.__opcion == '2':
                os.system('cls')
                a.detallarMaterialR()
                os.system('pause')
            elif self.__opcion == '3':
                os.system('cls')
                a.costoTotal()
                os.system('pause')
            elif self.__opcion == '4':
                os.system('cls')
                a.mostrarCostoAdi()
                os.system('pause')
            elif self.__opcion == '0':
                os.system('cls')
                print("Saliendo...")
            else:
                os.system('cls')
                print("Opción inválida.")
                os.system('pause')