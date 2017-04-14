"Ejemplo de implementación con Programación Estructurada"

clientes=[{'Nombre': 'Hector', 'Apellidos':'Costa Guzman', 'dni':'11111111A'},
          {'Nombre': 'Juan', 'Apellidos':'González Márquez', 'dni':'22222222B'}]

def mostrar_cliente(clientes, dni):
    for cliente in clientes:
        if (dni == cliente['dni']):
            return '{} {}'.format(cliente['Nombre'],cliente['Apellidos'])

    return 'Cliente no encontrado'

def borrar_cliente(clientes, dni):
    for cliente in clientes:
        if dni == cliente['dni']:
            clientes.remove(cliente)
            return 'Cliente {} Eliminado'.format(cliente)

    return 'Cliente no encontrado'

while True:
    dni = input('DNI')
    print(mostrar_cliente(clientes, dni))
    print(borrar_cliente(clientes,dni))
