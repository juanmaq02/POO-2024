from ManejadorVentas import ManejadorVentas
import os

def test():
    a = ManejadorVentas()
    opc = None
    while opc != 'f':
        print('''---MENU DE OPCIONES---
              a. Ingresar importe.
              b. Consultar facturacion total por sucursal.
              c. Sucursal con mayor facturacion en un dia.
              d. Sucursal con menor facturacion.
              e. Consultar total de facturacion.
              
              f. Salir.''')
        opc = input('>>> ')
        if opc == 'a':
            dia = input("Ingrese dia de la semana del importe a ingresar: ")
            dia = dia.capitalize()
            suc = int(input("Ingrese numero de sucursal: "))
            suc -= 1
            imp = float(input("Ingrese importe de la sucursal {} del dia {}: $".format(suc, dia)))
            a.agregarImporte(dia, suc, imp)
        elif opc == 'b':
            suc = int(input("Ingrese numero de sucursal: "))
            suc -= 1
            a.totalFacturacion(suc)
        elif opc == 'c':
            dia = input("Ingrese dia de la semana: ")
            dia = dia.capitalize()
            a.sucursalMayorFacturacionXDia(dia)
        elif opc == 'd':
            a.sucursalMenorFacturacion()
        elif opc == 'e':
            a.totalAcumulado()
        elif opc == 'f':
            print("Saliendo...")
        else:
            print("Opcion invalida.")


if __name__ == '__main__':
    test()