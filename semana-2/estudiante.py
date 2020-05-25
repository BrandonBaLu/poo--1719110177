class Banco:

  cajeros= 5
  ventanillas= 7
  empleados= 30
  camarasseguridad= 10
  alarmas= 3
  sucursales= 6
  oficinas= 6
 
  
  def servicioBanacario(self):
    print("servicioBanacario")
  def prestamos(self):
    print("prestamos")
  def seguridad(self):
    print("seguridad")

  def __init__(self):
    print("Banco Banamex")
    print(self.cajeros)
    print(self.ventanillas)
    print(self.empleados)
    print(self.camarasseguridad)
    print(self.alarmas)
    print(self.sucursales)
    print(self.oficinas)
    
objeto = Banco()
objeto.servicioBanacario()
objeto.seguridad()
objeto.prestamos()


