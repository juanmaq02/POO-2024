from ManejadorMoto import ManejadorMoto
from ManejadorPedido import ManejadorPedido
from ClaseMenu import MenuDeOpciones

def test():
    a = ManejadorMoto()
    b = ManejadorPedido()
    a.cargaMoto()
    b.cargaPedido()
    c = MenuDeOpciones()
    c.Menu(a, b)
if __name__ == '__main__':
    test()