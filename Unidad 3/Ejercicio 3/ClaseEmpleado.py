class Empleado:
    __nya: str
    __id: int
    __puesto: str

    def __init__(self, nya, id, puesto):
        self.__nya = nya
        self.__id = id
        self.__puesto = puesto

    def __str__(self):
        return f'Nombre y Apellido: {self.__nya}       ID: {self.__id}\nPuesto: {self.__puesto}'
    
    def getID(self):
        return self.__id