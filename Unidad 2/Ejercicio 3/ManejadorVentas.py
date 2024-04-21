class ManejadorVentas:
    __listaVentas: list
    def __init__(self):
        self.__listaVentas = [[],[],[],[],[]]
        for i in range(5):
            for j in range(7):
                self.__listaVentas[i].append(0)
    def buscaIndice(self, dia):
        if dia == 'Lunes':
            return 0
        elif dia == 'Martes':
            return 1
        elif dia == 'Miercoles':
            return 2
        elif dia == 'Jueves':
            return 3
        elif dia == 'Viernes':
            return 4
        elif dia == 'Sabado':
            return 5
        elif dia == 'Domingo':
            return 6
        else:
            print("Dia no encontrado.")
    def agregarImporte(self, dia, suc, imp):
        i = self.buscaIndice(dia)
        self.__listaVentas[suc][i] += imp
    def totalFacturacion(self, suc):
        tot = 0
        for i in range(7):
            tot += self.__listaVentas[suc][i]
        print("El total de facturacion de la sucursal {} es de: ${}".format(suc + 1, tot))
    def sucursalMayorFacturacionXDia(self, dia):
        max = 0
        i = self.buscaIndice(dia)
        for j in range(5):
            if self.__listaVentas[j][i] > max:
                max = self.__listaVentas[j][i]
                maxsuc = j
        print("La sucursal que más facturó el día {} es la sucursal {}.".format(dia, maxsuc + 1))
    def sucursalMenorFacturacion(self):
        acum = 0
        min = 9999999999999999999999999
        for i in range(5):
            for j in range(7):
                acum += self.__listaVentas[i][j]
            if acum < min:
                min = acum
                suc = i
            acum = 0
        print("La sucursal que menos facturó durante la semana es la sucursal {} con un total de ${}.".format(i + 1, min))
    def totalAcumulado(self):
        tot = 0
        for i in range(5):
            for j in range(7):
                tot += self.__listaVentas[i][j]
        print("Total acumulado por todas las sucursales durante la semana: ${}".format(tot))
