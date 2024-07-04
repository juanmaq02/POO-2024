from ManejadorLadrillo import ManejadorLadrillo
from ManejadorMaterialR import ManejadorMaterialR
from ClaseMenu import Menu

def test():
    b = ManejadorMaterialR()
    b.cargaMaterialR()
    a = ManejadorLadrillo()
    c = Menu()
    c.MenuDeOpciones(a, b)

if __name__ == '__main__':
    test()