from ClasePibe import Pibe

class ManejadorPibe:
    __listaPibe = list
    def __init__(self):
        self.__listaPibe = []
    def AgregaPibe(self, pibe):
        self.__listaPibe.append(pibe)
    def CargaPibe(self):
        Pibe1 = Pibe("Juan Marcos", "Quiroga", 21, 44431847, 1.80)
        Pibe2 = Pibe("Jeremías", "Cattaneo", 21, 44489112, 1.82)
        Pibe3 = Pibe("José Ignacio", "Nehín", 21, 44479170, 1.80)
        self.AgregaPibe(Pibe1)
        self.AgregaPibe(Pibe2)
        self.AgregaPibe(Pibe3)
    def MostrarDatos(self):
        print("---PIBES CARGADOS---")
        for i in range(len(self.__listaPibe)):
            print("\nPibe {}:".format(i+1))
            print("Nombre: {}\nApellido: {}\nEdad: {}\nDNI: {}\nAltura: {}".format(self.__listaPibe[i].getNombre(), self.__listaPibe[i].getApellido(), self.__listaPibe[i].getEdad(), self.__listaPibe[i].getDNI(), self.__listaPibe[i].getAltura()))
    