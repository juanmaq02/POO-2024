from ClaseEmpleado import Empleado

class ManejadorEmpleados:
    __listaEmpleados: list

    def __init__(self):
        self.__listaEmpleados = []

    def agregarEmpleado(self, a, c):
        nya = input("Ingrese nombre y apellido del empleado (0 para finalizar): ")
        while nya != '0':
            cont = len(self.__listaEmpleados)
            puesto = input("Ingrese el puesto del empleado: ")
            id = a._ManejadorProgramasC__listaProgramasC[0].getID()
            self.__listaEmpleados.append(Empleado(nya, id, puesto))
            print("Seleccione Programa Capacitacion a matricularse:")
            a.mostrarProgramas()
            i = int(input("Ingrese numero del Programa a matricularse (0 para finalizar): "))
            while i != 0:
                fecha = input("Ingrese fecha de hoy (dd/mm/aaaa): ")
                a._ManejadorProgramasC__listaProgramasC[i - 1].matricularEmpleado(self.__listaEmpleados[cont], fecha, c)
                print("Seleccione Programa Capacitacion a matricularse:")
                a.mostrarProgramas()
                i = int(input("Ingrese numero del Programa a matricularse (0 para finalizar): "))
            nya = input("Ingrese nombre y apellido del empleado (0 para finalizar): ")