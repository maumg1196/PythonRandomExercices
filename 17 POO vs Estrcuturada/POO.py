'Ejemplo de implementación con Programación Orientada a Objetos'

class Cliente:

    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)


class Empresa:

    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self, dni=None):
        for cliente in self.clientes:
            if cliente.dni == dni:
                return cliente

        return 'Cliente no encontrado'

    def borrar_cliente(self, dni=None):
        for cliente in self.clientes:
            if cliente.dni == dni:
                self.clientes.remove(cliente)
                return 'Cliente {} BORRADO'.format(cliente)

        return 'Cliente no encontrado'
        