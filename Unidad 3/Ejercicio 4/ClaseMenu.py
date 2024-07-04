from ClaseLibro import Libro
from ClaseCD import CD
import os

class Menu:
    __opcion: str

    def __init__(self):
        self.__opcion = None

    def MenuDeOpciones(self, lista):
        while self.__opcion != '0':
            os.system('cls')
            print('''
                  ---MENÚ DE OPCIONES---
                  1. Agregar Publicacion.
                  2. Consultar tipo de publicación.
                  3. Contar publicaciones.
                  4. Consultar publicaciones.
                  
                  0. Salir.''')
            self.__opcion = input(">>> ")
            if self.__opcion == '1':
                opc = None
                while opc != '0':
                    os.system('cls')
                    print('''
                        Seleccione tipo de publicación a agregar:
                        1. Libro
                        2. CD
                        
                        0. Finalizar.''')
                    opc = input(">>> ")
                    if opc == '1' or opc == '2':
                        os.system('cls')
                        t = input("Ingrese titulo de la publicación: ")
                        c = input("Ingrese categoría: ")
                        pr = float(input("Ingrese precio: $"))
                        if opc == '1':
                            a = input("Ingrese autor: ")
                            f = input("Ingrese fecha de publicación (dd/mm/aaaa): ")
                            pa = int(input("Ingrese cantidad de páginas: "))
                            lista.agregarPublicacion(Libro(t, c, pr, a, f, pa))
                            print("Libro agregado exitosamente.")
                            os.system('pause')
                        elif opc == '2':
                            d = int(input("Ingrese duración en minutos: "))
                            n = input("Ingrese nombre del narrador: ")
                            lista.agregarPublicacion(CD(t, c, pr, d, n))
                            print("CD agregado exitosamente.")
                            os.system('pause')
                    elif opc == '0':
                        pass
                    else:
                        print("Opción inválida.")
            elif self.__opcion == '2':
                os.system('cls')
                pos = int(input("Ingrese posición de lista: "))
                lista.mostrarTipo(pos)
                os.system('pause')
            elif self.__opcion == '3':
                os.system('cls')
                lista.cantPublicaciones()
                os.system('pause')
            elif self.__opcion == '4':
                os.system('cls')
                lista.mostrarPublicaciones()
                os.system('pause')
            elif self.__opcion == '5':
                os.system('cls')
                
                os.system('pause')
            elif self.__opcion == '0':               
                os.system('cls')
                print("Saliendo...")
            else:
                os.system('cls')
                print("Opción invalida.")
                os.system('pause')