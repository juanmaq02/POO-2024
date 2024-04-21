from ClaseCajaDeAhorro import CajaDeAhorro
def test():
    objeto = []
    for i in range(3):
        n = input("Ingrese su número de cuenta: ")
        c = input("Ingrese su CUIL: ")
        a = input("Ingrese su apellido: ")
        nom = input("Ingrese su nombre: ")
        s = float(input("Ingrese su saldo: $"))
        objeto.append(CajaDeAhorro(n, c, a, nom, s))
    for i in range(len(objeto)):
        objeto[i].mostrarDatos()
        importe = float(input("Ingrese importe a extraer: $"))
        objeto[i].extraer(importe)
        importe = float(input("Ingrese importe a depositar: $"))
        objeto[i].depositar(importe)

if __name__ == '__main__':
    test()