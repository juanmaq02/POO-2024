import numpy as np
from ClaseAlumno import Alumno

class ManejadorAlumno:

    __listaAlumno: np.array

    def __init__(self):
        self.__listaAlumno = np.empty([0], dtype=Alumno)

    def agregarAlumno(self, alumno):
        self.__listaAlumno = np.append(self.__listaAlumno, alumno)

    def cargaAlumno(self):
        nombre = input("Ingrese nombre del alumno a cargar (0 para finalizar): ")
        while nombre != '0':
            apellido = input("Ingrese apellido del alumno: ")
            dni = int(input("Ingrese DNI del alumno: "))
            registro = input("Ingrese N° de registro del alumno: ")
            nota = float(input("Ingrese nota final del alumno: "))
            alumno = Alumno(nombre, apellido, dni, registro, nota)
            self.agregarAlumno(alumno)
            nombre = input("Ingrese nombre del alumno a cargar (0 para finalizar): ")
            
    def mostrarArregloOrdenado(self):
        i = 0
        self.__listaAlumno = np.sort(self.__listaAlumno)
        while i < len(self.__listaAlumno):
            print(self.__listaAlumno[i])
            i += 1

    def copiarArreglo(self):
        arreglo = self.__listaAlumno.copy()
        for i in arreglo:
            print(i)

    def maximoYMinimo(self):
        print("Los datos del alumno con la nota más alta encontrada es: \n{}".format(np.max(self.__listaAlumno)))
        print("Los datos del alumno con la nota más baja encontrada es: \n{}".format(np.min(self.__listaAlumno)))