class CajaDeAhorro:
    __nroCuenta: str
    __cuil: str
    __apellido: str
    __nombre: str
    __saldo: float
    def __init__(self, nroCuenta, cuil, apellido, nombre, saldo):
        self.__nroCuenta = nroCuenta
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__saldo = saldo
    def mostrarDatos(self):
        print("---DATOS DEL CLIENTE---")
        print("Número de cuenta: {}\nCUIL: {}\nApellido: {}\nNombre: {}\nSaldo: ${}".format(self.__nroCuenta, self.__cuil, self.__apellido, self.__nombre, self.__saldo))
    def extraer(self, importe):
        if importe <= self.__saldo:
            self.__saldo -= importe
            print("¡Extracción realizada con éxito!\nSaldo actual: ${}".format(self.__saldo))
        else:
            print("No hay suficiente saldo en la cuenta para poder llevar a cabo la extracción.")
    def depositar(self, importe):
        if importe > 0:
            self.__saldo += importe
            print("¡Deposito realizado con éxito!\nSaldo actual: ${}".format(self.__saldo))
        else:
            print("Ingrese un valor positivo.")
    def validarCUIL(self):
        s = int(input("Ingrese el Tipo (1.Hombre 2.Mujer 3.Sociedad/Empresa): "))
        if s == 1:
            if self.__cuil[0:2:] == "20":
                pass
            else:
                print("CUIL invalidado.")
                return False
        elif s == 2:
            if self.__cuil[0:2:] == "27":
                pass
            else:
                print("CUIL invalidado.")
                return False
        elif s == 3:
            if self.__cuil[0:2:] == "30":
                pass
            else:
                print("CUIL invalidado.")
                return False
        else:
            print("Valor incorrecto.")
            return False
