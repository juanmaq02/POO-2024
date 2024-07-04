from ManejadorEdificio import ManejadorEdificio
from ClaseMenu import Menu

def test():
    a = ManejadorEdificio()
    a.cargaEdificiosYDepartamentos()
    b = Menu()
    b.MenuDeOpciones(a)
    
if __name__ == '__main__':
    test()