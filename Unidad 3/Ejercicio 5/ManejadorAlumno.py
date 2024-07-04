from ClaseAlumno import Alumno
from Interfaz import IClase
from zope.interface import implementer

@implementer(IClase)
class ManejadorAlumno:
    __listaAlumno: list
    
    def __init__(self):
        self.__listaAlumno = []

    def insertarAlumno(self):
        ayn = input("Ingrese datos del alumno:\nApellido y nombre: ")
        dni = int(input("DNI: "))
        reg = input("Registro: ")
        car = input("Carrera: ")
        ing = int(input("Año de ingreso: "))
        alumno = Alumno(ayn, dni, reg, car, ing)
        posicion = int(input("Ingrese posicion de la lista (0 - {}): ".format(len(self.__listaAlumno))))
        try:
            self.__listaAlumno.insert(posicion, alumno)
            print("Alumno ingresado exitosamente.")
        except IndexError:
            print("Posición de lista inválida.")

    def agregarAlumno(self, alumno):
        self.__listaAlumno.append(alumno)
        print("Alumno agregado exitosamente.")

    def mostrarAlumno(self, pos):
        print(self.__listaAlumno[pos])
        print("--------------------")

    
