"""

@author: Daniel Cardona Carvajal
         Isabella Muñoz Castro
         Rosa Maria Villada Jaramillo
Grupo:580506004-10          
"""


# Este archivo no es necesario modificarlo.
class RegistroCarrito():
    def __init__(self, producto, unidades):
        self.producto=producto
        self.unidades=unidades
    
    def __str__(self):
        return self.producto.descripcion.ljust(30) + str(self.unidades).ljust(4)
        
