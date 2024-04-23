from ManejadorEquipo import ManejadorEquipo
from ManejadorFecha import ManejadorFecha
from ClaseMenu import MenuDeOpciones

def test():
    a = ManejadorEquipo()
    b = ManejadorFecha()
    a.cargaEquipos()
    b.cargaFechas()
    c = MenuDeOpciones()
    c.Menu(a, b)
if __name__ == '__main__':
    test()
