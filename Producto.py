"""

@author: Daniel Cardona Carvajal
         Isabella Muñoz Castro
         Rosa Maria Villada Jaramillo
Grupo:580506004-10          
"""


# Este archivo no es necesario modificarlo.
class Producto():
    def __init__(self, codigo, descripcion, valorUnitario, unidades):
        self.__codigo=codigo
        self.__descripcion=descripcion
        self.__valorUnitario=valorUnitario
        self.__unidades=unidades

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,codigo):
        self.__codigo=codigo

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self,descripcion):
        self.__descripcion=descripcion

    @property
    def valorUnitario(self):
        return self.__valorUnitario

    @valorUnitario.setter
    def valorUnitario(self,valorUnitario):
        self.__valorUnitario=valorUnitario

    @property
    def unidades(self):
        return self.__unidades

    @unidades.setter
    def unidades(self,unidades):
        self.__unidades=unidades

    def __str__(self):
        return str(self.codigo)+' '+str(self.descripcion)+' '+str(self.valorUnitario)+' '+str(self.unidades)

