from ClaseNodo import Nodo
from ClaseLibro import Libro
from ClaseCD import CD
import os

class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    
    def __iter__(self):
        self.__actual = self.__comienzo  
        self.__indice = 0
        return self

    def __next__(self):
        if self.__actual is None:
            raise StopIteration
        elif self.__indice == self.__tope:
            raise StopIteration
        else:
            self.__indice += 1
            publicacion = self.__actual.getPublicacion()
            self.__actual = self.__actual.getSiguiente()
            return publicacion

    def agregarPublicacion(self, publicacion):
        nodo = Nodo(publicacion)
        if self.__comienzo is None:
            self.__comienzo = nodo
        else:
            actual = self.__comienzo
            while actual.getSiguiente() is not None:
                actual = actual.getSiguiente()
            actual.setSiguiente(nodo)
            print(hex(id(actual)))
            print(hex(id(self.__comienzo)))
            os.system('pause')
        self.__tope += 1

    def mostrarTipo(self, posicion):
        contador = 0
        for actual in self:
            if contador == posicion:
                if isinstance(actual, Libro):
                    print("La publicación de la posición {} es un libro.".format(posicion))
                else:
                    print("La publicación de la posición {} es un CD.".format(posicion))
                return
            contador += 1
        raise IndexError("Índice fuera de rango")
    
    def cantPublicaciones(self):
        contL = 0
        contCD = 0
        for actual in self:
            if isinstance(actual, Libro):
                contL += 1
            else:
                contCD += 1
        print("En la lista se encuentran {} libros y {} CDs.".format(contL, contCD))
    
    def mostrarPublicaciones(self):
        pos = 1
        for actual in self:
            print("PUBLICACIÓN {}:\nTítulo: {}\nCategoría: {}\nImporte de venta: ${:.2f}".format(pos, 
                                                                                                 actual.getTitulo(), 
                                                                                                 actual.getCategoria(), 
                                                                                                 actual.getPrecio()))
            print("-------------------------------------\n")
            pos += 1
        