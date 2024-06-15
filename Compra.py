"""

@author: Daniel Cardona Carvajal
         Isabella Muñoz Castro
         Rosa Maria Villada Jaramillo
Grupo:580506004-10          
"""

# Este archivo no es necesario modificarlo.
class Compra():
    numeroFactura=1000
    def __init__(self, fecha, carrito):
        self.numeroFactura=Compra.numeroFactura
        Compra.numeroFactura+=1
        self.carrito=carrito
        
    