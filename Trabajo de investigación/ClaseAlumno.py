class Alumno:

    __nombre: str
    __apellido: str
    __dni: int
    __registro: str
    __nota: float

    def __init__(self, nombre, apellido, dni, registro, nota):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__registro = registro
        self.__nota = nota
        
    def __str__(self):
        return f'Apellido y Nombre: {self.__apellido} {self.__nombre}   DNI: {self.__dni}\nN° de registro: {self.__registro}    Nota final: {self.__nota}'
    
    def __lt__(self, other):
        return self.__nota < other.__nota
    
    def __le__(self, other):
        return self.__nota <= other.__nota
    
    def __ge__(self, other):
        return self.__nota >= other.__nota
    
    