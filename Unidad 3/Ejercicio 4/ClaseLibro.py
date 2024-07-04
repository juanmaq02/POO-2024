from ClasePublicaciones import Publicacion

class Libro(Publicacion):
    __autor: str
    __fecha: str
    __paginas: int
    
    def __init__(self, titulo, categoria, precio, autor, fecha, paginas):
        super().__init__(titulo, categoria, precio)
        self.__autor = autor
        self.__fecha = fecha
        self.__paginas = paginas