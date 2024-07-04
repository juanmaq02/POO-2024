import os

class Menu:
    __opcion: str

    def __init__(self):
        self.__opcion = None

    def MenuDeOpciones(self, a, b, c):
        while self.__opcion != '0':
            os.system('cls')
            print('''
                  ---MENÚ DE OPCIONES---
                  1. Cargar Programas Capacitación.
                  2. Cargar Personas.
                  3. Informar duracion de Programas de un empleado.
                  4. Mostrar empleados matriculados en un programa.
                  5. Informar empleados sin matricularse.
                  
                  0. Salir.''')
            self.__opcion = input(">>> ")
            if self.__opcion == '1':
                os.system('cls')
                a.agregarProgramaC()
                os.system('pause')
            elif self.__opcion == '2':
                os.system('cls')
                b.agregarEmpleado(a, c)
                os.system('pause')
            elif self.__opcion == '3':
                os.system('cls')
                a.informarDuracion()
                os.system('pause')
            elif self.__opcion == '4':
                os.system('cls')
                a.informarEmpleados()
                os.system('pause')
            elif self.__opcion == '5':
                os.system('cls')
                c.informarEmpleadosSinMatricula(b)
                os.system('pause')
            elif self.__opcion == '0':               
                os.system('cls')
                print("Saliendo...")
            else:
                os.system('cls')
                print("Opción invalida.")
                os.system('pause')