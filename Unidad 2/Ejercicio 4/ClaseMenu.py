from ManejadorMoto import ManejadorMoto
from ManejadorPedido import ManejadorPedido
import os

class MenuDeOpciones:
    __opcion: int
    def __init__(self):
        self.__opcion = None
    def Menu(self, a, b):
        os.system('cls')
        print('''
              ---MENU DE OPCIONES---
              1. Cargar nuevo pedido.
              2. Modificar pedido.
              3. Consultar datos.
              4. Listar Motos.
              
              0. Salir.''')
        self.__opcion = input('>>> ')
        self.Opciones(a, b)
    def Opciones(self, a, b):
        if self.__opcion == '1':
            os.system('cls')
            b.nuevoPedido(a)
        elif self.__opcion == '2':
            os.system('cls')
            b.modificarTiempoR()
        elif self.__opcion == '3':
            os.system('cls')
            a.datosConductor(b)
        elif self.__opcion == '4':
            os.system('cls')
            a.listarMotos(b)
        elif self.__opcion == '0':
            os.system('cls')
            print("Saliendo...")
            return
        else:
            os.system('cls')
            print("Opcion invalida.")
            os.system('pause')
        self.Menu(a, b)
