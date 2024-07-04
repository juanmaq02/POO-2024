import os
from ClaseLista import Lista
from ClaseObjectEncoder import ObjectEncoder
from ClaseInterfaz import Interfaz
from ClaseCalefactorE import CalefactorE
from ClaseCalefactorG import CalefactorG

class Menu:
    __opcion: str

    def __init__(self):
        self.__opcion = None

    def Interfaz(self, listaI: Interfaz):
        if self.__opcion == '1' or self.__opcion == '2':
            a = None
            while a != 'n':
                os.system('cls')
                tipo = input("Ingrese datos del calefactor:\nTipo (Gas o Electrico): ")
                assert (tipo.capitalize() == 'Gas' or tipo.capitalize() == 'Electrico'), 'Tipo de calefactor no admitido.'
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                pais = input("País de fabricación: ")
                precio = float(input("Precio base: $"))
                formaP = input("Forma de pago: ")
                cantC = int(input("Cantidad de cuotas: "))
                promocion = input("¿El calefactor está en promoción? (Si / No): ")
                if tipo.upper() != 'Gas':
                    matricula = input("Matricula: ")
                    calorias = int(input("Calorias: "))
                    calefactor = CalefactorG(marca, modelo, pais, precio, formaP, cantC, promocion, matricula, calorias)
                else:
                    potMax = int(input("Potencia máxima: "))
                    calefactor = CalefactorE(marca, modelo, pais, precio, formaP, cantC, promocion, potMax)
                calefactor.setImporte()
                if self.__opcion == '1':
                    pos = int(input("Ingrese posición de la lista: "))
                    listaI.insertarCalefactor(calefactor, pos)
                else:
                    listaI.agregarCalefactor(calefactor)
                a = input("Calefactor agregado exitosamente. ¿Desea agregar otro calefactor? (s/n): ")
        elif self.__opcion == '3':
            pos = int(input("Ingrese posición de la lista: "))
            os.system('cls')
            listaI.mostrarCalefactor(pos)
            os.system('pause')

    def MenuDeOpciones(self, lista):
        jsonF = ObjectEncoder()
        diccionario = jsonF.leerJSONArchivo('calefactoresB.json')
        calefactores = jsonF.decodificarDiccionario(diccionario)
        print(calefactores)
        for calefactor in calefactores:
            calefactor.setImporte()
            lista.agregarCalefactor(calefactor)
        while self.__opcion != '0':
            os.system('cls')
            print('''
                  ---MENÚ DE OPCIONES---
                  1. Insertar calefactor.
                  2. Agregar calefactor al final de la lista.
                  3. Mostrar calefactor.
                  4. Mostrar calefactor con menor precio.
                  5. Mostrar calefactores de una marca.
                  6. Mostrar calefactores en promoción.
                  7. Guardar calefactores.
                  
                  0. Salir.''')
            self.__opcion = input(">>> ")
            if self.__opcion == '1' or self.__opcion == '2' or self.__opcion == '3':
                self.Interfaz(Interfaz(lista))
            elif self.__opcion == '4':
                os.system('cls')
                lista.calefactorMenorPrecio()
                os.system('pause')
            elif self.__opcion == '5':
                os.system('cls')
                marca = input("Ingrese marca de calefactor eléctrico: ")
                lista.calefactoresEUnaMarca(marca)
                os.system('pause')
            elif self.__opcion == '6':
                os.system('cls')
                lista.calefactoresEnPromocion()
                os.system('pause')
            elif self.__opcion == '7':
                os.system('cls')
                d = lista.toJSON()
                jsonF.guardarJSONArchivo(d, 'calefactores.json')
                print("Archivo guardado exitosamente.")
                os.system('pause')
            elif self.__opcion == '0':               
                os.system('cls')
                print("Saliendo...")
            else:
                os.system('cls')
                print("Opción invalida.")
                os.system('pause')