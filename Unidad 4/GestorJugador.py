from ClaseJugador import Jugador

class GestorJugador:
    __listaJugadores: list

    def __init__(self):
        self.__listaJugadores = []

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            jugadores = [jugador.toJSON() for jugador in self.__listaJugadores]
        )
        return d

    def guardarJugador(self, jugador):
        self.__listaJugadores.append(jugador)
        
    def getLista(self):
        self.__listaJugadores.sort(reverse=True)
        return self.__listaJugadores