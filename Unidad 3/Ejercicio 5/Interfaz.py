from zope.interface import Interface

class IClase(Interface):

    def insertarAlumno(alumno, posicion):
        pass
    
    def agregarAlumno(alumno):
        pass

    def mostrarAlumno(posicion):
        pass