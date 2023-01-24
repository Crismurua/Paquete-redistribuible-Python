class Cliente:
    def __init__(self, nombre, apellido, domicilio, email, compras = 0):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.domicilio = domicilio
        self.compras = compras
        
    def __str__(self):
        return f'nombre: {self.nombre}, apellido: {self.apellido}, domcilio: {self.domicilio}, email: {self.email}, compras: {self.compras}'

    def compra_realizada(self):
      self.compras += 1

    def modificar_datos(self, nombre='', apellido='', domicilio='', email=''):
      #para modificar un dato en especifico se debe pasar el resto de los parametros como cadena de texto vacia
        if not nombre:
          self.nombre = self.nombre
        else:
          self.nombre = nombre
        if not apellido:
          self.apellido = self.apellido
        else:
          self.apellido = apellido
        if not domicilio:
          self.domicilio = self.domicilio
        else:
          self.domicilio = domicilio
        if not email:
          self.email = self.email
        else:
          self.email = email
    
    