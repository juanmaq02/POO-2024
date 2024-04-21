def generar_factura(DNI, nombre, patente, vehiculo, reparaciones):
    factura = f"DNI: {DNI: <30}Apellido y nombre: {nombre}\n"
    factura += f"Patente: {patente: <25}Vehículo: {vehiculo}\n\n"
    factura += "Reparación                        precio repuesto          mano de obra        subtotal\n"
    
    total = 0
    for reparacion in reparaciones:
        descripcion, precio_repuesto, mano_obra, subtotal = reparacion
        factura += f"{descripcion: <30}${precio_repuesto: <25}${mano_obra: <20}${subtotal: <10}\n"
        total += subtotal
    
    factura += "\n" + " " * 77 + f"TOTAL A PAGAR ${total:.2f}"
    
    return factura

# Ejemplo de uso:
reparaciones = [
    ("Cambio de aceite", 50.00, 20.00, 70.00),
    ("Reparación de frenos", 80.00, 30.00, 110.00),
    ("Alineación y balanceo", 60.00, 25.00, 85.00)
]

factura = generar_factura("123", "Juan Pérez", "ABC123", "Toyota Corolla", reparaciones)
print(factura)