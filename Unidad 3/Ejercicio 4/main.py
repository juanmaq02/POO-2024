from ClaseLibro import Libro
from ClaseCD import CD
from ClaseLista import Lista
from ClaseMenu import Menu

def test():
    publicacion1 = Libro("Harry El Sucio Potter: En la Paja Eterna y el Debut de Harry", "Suspenso", 25000.0, "El Bananero", "23/10/2008", 230)
    publicacion2 = CD("El Hombre que Araña", "Comedia", 36750.0, 25, "Ricardo Darín")
    publicacion3 = CD("Iván el Trolazo", "Drama", 26500.0, 20, "El Bananero")
    publicacion4 = Libro("Diario de Ana Frank", "Suspenso", 40150.0, "Ana Frank", "12/05/1945", 350)
    lista = Lista()
    lista.agregarPublicacion(publicacion1)
    lista.agregarPublicacion(publicacion2)
    lista.agregarPublicacion(publicacion3)
    lista.agregarPublicacion(publicacion4)
    menu = Menu()
    menu.MenuDeOpciones(lista)

if __name__ == '__main__':
    test()