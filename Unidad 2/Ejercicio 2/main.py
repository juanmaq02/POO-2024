from ManejadorCajaDeAhorro import Manejador
def test():
    a = Manejador()
    a.CargaCaja()
    cuil = input("Ingrese CUIL: ")
    datos = a.obtenerDatos(cuil)
    print("Nombre: {}\nApellido: {}\nSaldo: ${}".format(datos[0], datos[1], datos[2]))

if __name__ == '__main__':
    test()