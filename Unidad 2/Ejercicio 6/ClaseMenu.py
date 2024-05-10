from ManejadorCuenta import ManejadorCuenta
from ManejadorTransaccion import ManejadorTransaccion
import os

class MenuDeOpciones:
    __opcion: str
    def __init__(self):
        self.__opcion = None
    def Menu(self, a, b):
        while self.__opcion != 'e':
            os.system('cls')
            print('''
                ---MENU DE OPCIONES---
                a. Consultar cliente.
                b. Actualizar saldo de los clientes.
                c. Establecer porcentaje anual de rendimiento.
                d. Incrementar saldo.
                
                e. Salir.''')
            self.__opcion = input('>>> ')
            if self.__opcion == 'a':
                os.system('cls')
                a.informarCliente(b)
                os.system('pause')
            elif self.__opcion == 'b':
                os.system('cls')
                b.actualizarSaldo(a)
                os.system('pause')
            elif self.__opcion == 'c':
                os.system('cls')
                a.establecerPorcentaje()
                os.system('pause')
            elif self.__opcion == 'd':
                os.system('cls')
                a.incrementarSaldo()
                os.system('pause')
            elif self.__opcion == 'e':
                os.system('cls')
                print("Saliendo...")
                return
            else:
                os.system('cls')
                print("Opcion invalida.")
                os.system('pause')
