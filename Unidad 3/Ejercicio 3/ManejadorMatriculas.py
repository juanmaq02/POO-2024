class ManejadorMatriculas:
    __listaMatriculas: list

    def __init__(self):
        self.__listaMatriculas = []
    
    def agregarMatricula(self, matricula):
        self.__listaMatriculas.append(matricula)

    def informarEmpleadosSinMatricula(self, b):
        print("Empleados sin matriculación:")
        bandera2 = True
        for empleado in b._ManejadorEmpleados__listaEmpleados:
            bandera = True
            for matricula in self.__listaMatriculas:
                    if empleado == matricula.getEmpleado():
                        bandera = False
            if bandera:
                print(empleado)
                bandera2 = False
            if bandera2:
                print("Todos los empleados están matriculados.")
                         
