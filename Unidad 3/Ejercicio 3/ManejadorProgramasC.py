from ClaseProgramaC import ProgramaC

class ManejadorProgramasC:
    __listaProgramasC: list

    def __init__(self):
        self.__listaProgramasC = []

    def agregarProgramaC(self):
        nom = input("Ingrese el nombre del Programa Capacitacion (0 para finalizar): ")
        while nom != '0':
            cod = input("Ingrese codigo del programa: ")
            dur = int(input("Ingrese la duracion del programa (en horas): "))
            self.__listaProgramasC.append(ProgramaC(nom, cod, dur))
            print("Programa agregado exitosamente.")
            nom = input("Ingrese el nombre del Programa Capacitacion (0 para finalizar): ")
    
    def mostrarProgramas(self):
        c = 1
        for programa in self.__listaProgramasC:
            print(str(c) + '. ' + str(programa))
            c += 1

    def informarDuracion(self):
        id = int(input("Ingrese identificador del empleado: "))
        bandera = True
        for programa in self.__listaProgramasC:
            for matricula in programa.getMatriculas():
                if matricula.getEmpleado().getID() == id:
                    print("El programa {} tiene una duración de {} horas.".format(programa.getNombre(), programa.getDuracion()))
                    bandera = False
        if bandera:
            print("No se ha encontrado un empleado con el identificador ingresado.")

    def informarEmpleados(self):
        nom = input("Ingrese nombre de un Programa: ")
        bandera, bandera2 = True
        for programa in self.__listaProgramasC:
            if programa == nom:
                bandera = False
                for matricula in programa.getMatriculas():
                    print(matricula.getEmpleado())
                    bandera2 = False
        if bandera:
            print("No se encontró el programa ingresado.")
        elif bandera2:
            print("No se han encontrado empleados matriculados en el programa ingresado.")