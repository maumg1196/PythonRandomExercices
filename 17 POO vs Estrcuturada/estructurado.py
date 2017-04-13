Ejemplo de implementación con Programación Estructurada \\\,

clientes=[{'Nombre': 'Hector', 'Apellidos':'Costa Guzman', 'dni':'11111111A'},
          {'Nombre': 'Juan', 'Apellidos':'González Márquez', 'dni':'22222222B'}]

def mostrar_cliente(clientes, dni):
        for cliente in clientes:
            if (dni == cliente['dni']):
                print('{} {}'.format(cliente['Nombre'],cliente['Apellidos']))
                return

        print('Cliente no encontrado')

def borrar_cliente():
    pass
