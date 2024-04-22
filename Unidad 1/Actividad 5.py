class Producto:
    __codigo: int
    __descripcion: str
    __precio: float
    def __init__(self, codigo, descripcion, precio):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__precio = precio
    def actualizarPrecios(self, precio):
        self.__precio = float(input("Ingrese nuevo precio del articulo {} (precio actual: {}): ".format(self.__codigo, self.__precio)))
        print("Precio cambiado exitosamente.")
class Cliente:
    __dni: int
    __nombre: str
    __apellido: str
    __direccion: str
    __correo: str
    __telefono: int
    def __init__(self, dni, nombre, apellido, direccion, correo, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__correo = correo
        self.__telefono = telefono
    