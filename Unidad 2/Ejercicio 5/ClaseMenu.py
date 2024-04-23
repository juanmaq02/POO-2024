from ManejadorEquipo import ManejadorEquipo
from ManejadorFecha import ManejadorFecha
import os

class MenuDeOpciones:
    __opcion: int
    def __init__(self):
        self.__opcion = None
    def Menu(self, a, b):
        os.system('cls')
        print('''
              ---MENU DE OPCIONES---
              a. Listar fechas de un equipo.
              b. Tabla de posiciones.
              c. Actualizar tabla.
              d. Guardar tabla de posiciones.
              
              e. Salir.''')
        self.__opcion = input('>>> ')
        self.Opciones(a, b)
    def Opciones(self, a, b):
        if self.__opcion == 'a':
            os.system('cls')
            a.listadoEquipo(b)
            os.system('pause')
        elif self.__opcion == 'b':
            os.system('cls')
            a.tablaDePosiciones()
            os.system('pause')
        elif self.__opcion == 'c':
            os.system('cls')
            b.actualizarTabla(a)
            os.system('pause')
        elif self.__opcion == 'd':
            os.system('cls')
            a.guardarTabla()
            os.system('pause')
        elif self.__opcion == 'e':
            os.system('cls')
            print("Saliendo...")
            return
        else:
            os.system('cls')
            print("Opcion invalida.")
            os.system('pause')
        self.Menu(a, b)
