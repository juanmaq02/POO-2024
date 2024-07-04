from ManejadorEmpleados import ManejadorEmpleados
from ManejadorProgramasC import ManejadorProgramasC
from ManejadorMatriculas import ManejadorMatriculas
from ClaseMenu import Menu

def test():
    a = ManejadorProgramasC()
    b = ManejadorEmpleados()
    c = ManejadorMatriculas()
    d = Menu()
    d.MenuDeOpciones(a, b, c)

if __name__ == '__main__':
    test()