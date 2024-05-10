from ManejadorCuenta import ManejadorCuenta
from ManejadorTransaccion import ManejadorTransaccion
from ClaseMenu import MenuDeOpciones

def test():
    a = ManejadorCuenta()
    b = ManejadorTransaccion()
    a.cargaCuentas()
    b.cargaTransacciones()
    c = MenuDeOpciones()
    c.Menu(a, b)
    
if __name__ == '__main__':
    test()
