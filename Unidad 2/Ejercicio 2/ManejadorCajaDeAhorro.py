from ClaseCajaDeAhorro import CajaDeAhorro

class Manejador:
    __listaCaja: list
    def __init__(self):
        self.__listaCaja = []
    def AgregaCaja(self, caja):
        self.__listaCaja.append(caja)
    def CargaCaja(self):
        for i in range(3):
            n = input("Ingrese su número de cuenta: ")
            c = input("Ingrese su CUIL: ")
            a = input("Ingrese su apellido: ")
            nom = input("Ingrese su nombre: ")
            s = float(input("Ingrese su saldo: $"))
            self.AgregaCaja(CajaDeAhorro(n,c,a,nom,s))
    def obtenerDatos(self, cuil):
        i = 0
        encontrado = bool
        while (i < len(self.__listaCaja)) and (encontrado != True):
            if self.__listaCaja[i].getCUIL() == cuil:
                encontrado = True
            else:
                i += 1
        if encontrado == True:
            datos = []
            datos.append(self.__listaCaja[i].getNombre())
            datos.append(self.__listaCaja[i].getApellido())
            datos.append(self.__listaCaja[i].getSaldo())
            return datos
        else:
            return "CUIL no valido."
        
    
    