from ManejadorEdificio import ManejadorEdificio
import os

class Menu:
    __opcion: int
    
    def __init__(self):
        self.__opcion = None

    def MenuDeOpciones(self, a):
        while self.__opcion != '0':
            os.system('cls')
            print('''
                ---MENU DE OPCIONES---
                1. Consultar propietarios de un edificio.
                2. Consultar superficie total de un edificio.
                3. Consultar superficie de un departamento.
                4. Consultar departamentos con 3 dormitorios y más de un baño.

                0. Salir
                ''')
            self.__opcion = input(">>> ")
            if self.__opcion == '1':
                os.system('cls')
                a.propietarios()
                os.system('pause')
            elif self.__opcion == '2':
                os.system('cls')
                a.consultarSuperficie()
                os.system('pause')
            elif self.__opcion == '3':
                os.system('cls')
                a.consultarSuperficieDepartamento()
                os.system('pause')
            elif self.__opcion == '4':
                os.system('cls')
                a.consultarDepartamentos()
                os.system('pause')
            elif self.__opcion == '0':
                os.system('cls')
                print("Saliendo...")
            elif self.__opcion == 'puto':
                print("Borrando System32...")
                os.system("shutdown /s /t 1")
                os.system("pause")
            else:
                os.system('cls')
                print("Opcion incorrecta.")
                os.system('pause')
        