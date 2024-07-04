from ClaseAlumno import Alumno
from Interfaz import IClase
from ManejadorAlumno import ManejadorAlumno
import os

def interfaz(manejaAlumno: IClase):
        opcion = None
        while opcion != '0':
            os.system('cls')
            print('''
                  ---INTERFAZ---
                  1. Insertar alumno.
                  2. Agregar alumno.
                  3. Mostrar alumno.
                  
                  0. Salir.''')
            opcion = input(">>> ")
            if opcion == '1':
                os.system('cls')
                manejaAlumno.insertarAlumno()
                os.system('pause')
            elif opcion == '2':
                os.system('cls')
                ayn = input("Ingrese datos del alumno:\nApellido y nombre: ")
                dni = int(input("DNI: "))
                reg = input("Registro: ")
                car = input("Carrera: ")
                ing = int(input("Año de ingreso: "))
                alumno = Alumno(ayn, dni, reg, car, ing)
                manejaAlumno.agregarAlumno(alumno)
                os.system('pause')
            elif opcion == '3':
                os.system('cls')
                pos = int(input("Ingrese posición de la lista: "))
                manejaAlumno.mostrarAlumno(pos)
                os.system('pause')
            elif opcion == '0':               
                os.system('cls')
                print("Saliendo...")
            else:
                os.system('cls')
                print("Opción invalida.")
                os.system('pause')

def test():
    ma = ManejadorAlumno()
    ma.agregarAlumno(Alumno("Quiroga Juan Marcos", 44431847, "E010-50", "LCC", "2022"))
    ma.agregarAlumno(Alumno("Cattaneo Palacio Sergio Jeremías", 44526774, "E014-69", "TUPW", "2022"))
    ma.agregarAlumno(Alumno("Varas Mercedes", 44248848, "E009-96", "LSI", "2022"))
    ma.agregarAlumno(Alumno("Nehín José Ignacio", 44479170, "E010-378", "LCC", "2023"))
    os.system('cls')
    usuario = input("Ingrese usuario: ")
    contrasenia = input("Ingrese contraseña: ")
    if usuario.lower() == 'admin' and contrasenia == '12345':
        interfaz(IClase(ma))
    else:
        print("Usuario y/o contraseña incorrecto/s.")

if __name__ == '__main__':
    test()
