from ClaseMaterialR import MaterialR

class ManejadorMaterialR:
    __listaMaterialR: list

    def __init__(self);
        self.__listaMaterialR = []

    def agregarMaterialR(self):
        mat = input("Ingrese material: ")
        car = input("Ingrese caracteristicas: ")
        cantU = float(input("Ingrese la cantidad utilizada: "))
        cost = float(input("Ingrese el costo adicional: $"))
        self.__listaMaterialR.append(MaterialR(mat, car, cantU, cost))

    