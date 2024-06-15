"""

@author: Daniel Cardona Carvajal
         Isabella Muñoz Castro
         Rosa Maria Villada Jaramillo
Grupo:580506004-10          
"""
""" 
Este archivo tiene otras funcionalidades que debe desarrollar, por favor complete
el código de las funciones ubicadas en la parte inferior. 
"""

from DoubleList import DoubleList
from Compra import Compra
from datetime import datetime
from RegistroCarrito import RegistroCarrito
from datetime import datetime 

class Usuario():
    def __init__(self, cedula, nombre, apellido, fechaNacimiento):
        self.cedula=cedula
        self.nombre=nombre
        self.apellido=apellido
        self.fechaNacimiento=fechaNacimiento
        self.puntos=0
        self.carritoDeCompras=DoubleList()
        self.compras=DoubleList()

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self,cedula):
        self.__cedula=cedula

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self,apellido):
        self.__apellido=apellido

    @property
    def fechaNacimiento(self):
        return self.__fechaNacimiento

    @fechaNacimiento.setter
    def fechaNacimiento(self,fechaNacimiento):
        self.__fechaNacimiento=fechaNacimiento

    @property
    def puntos(self):
        return self.__puntos

    @puntos.setter
    def puntos(self,puntos):
        self.__puntos=puntos

    @property
    def carritoDeCompras(self):
        return self.__carritoDeCompras

    @carritoDeCompras.setter
    def carritoDeCompras(self,carritoDeCompras):
        self.__carritoDeCompras=carritoDeCompras

    @property
    def compras(self):
        return self.__compras

    @compras.setter
    def compras(self,compras):
        self.__compras=compras

    def __str__(self):
        return str(self.cedula)+' '+str(self.nombre)+' '+str(self.apellido)+' '+str(self.fechaNacimiento)+' '+str(self.puntos)

    def agregarAlCarrito(self, registro):# Vale (0.2)

        produto_existente = self.buscarEnCarrito(registro)
        if produto_existente == None:
            self.carritoDeCompras.addLast(registro)
        else:
             produto_existente.data.unidades += registro.unidades

            
        """
        Este método se encarga de agregar los registros de carrito a la lista 
        doble de carritoDeCompras del usuario. En caso de que en el carrito ya 
        se encuentre el producto, debe aumentarse la cantidad de unidades del
        registro que previamente existente. En caso contrario el nuevo registro
        se agrega al final de la lista doble
        """
  
        
    def buscarEnCarrito(self, producto):# Vale (0.2)

        temp = self.carritoDeCompras.first()

        while temp !=None and temp.data.producto != producto:
            temp=temp.next
        
        if temp == None:
            return None
        else:
            return temp
        """
        Este método realiza la búsqueda de un registro de carrito por producto
        en la lista de carritoDeCompras. Al finalizar debe retornar el Nodo Doble 
        donde se encuentra el registro o en su defecto un valor de None
        
        """
        
    def eliminarDelCarrito(self, producto):# Vale (0.2)

        temp = self.buscarEnCarrito(producto)
        if temp != None:
            self.carritoDeCompras.remove(temp)
       
        """
        Este método realiza la eliminación de un registro de carrito por producto
        en la lista de carritoDeCompras. En este caso no retornaremos ningun valor
        
        """             
    def comprarCarrito(self):# Vale (0.4)

        if (not self.carritoDeCompras.isEmpty()):
            fecha_actual = datetime.now()
            registro_Compra = RegistroCarrito(fecha_actual, self.carritoDeCompras)
            self.compras.addLast(registro_Compra)
            self.carritoDeCompras = DoubleList()
        else:
            print("El carrito de compras está vacío.")


        """
        Este método se encarga de realizar la compra del Carrito desde el usuario.
        En este punto si el carrito tiene elemento, debe crearse un objeto de tipo 
        compra, cuya fecha es la fecha actual y debe enviarse como segundo parámetro
        el carrito de compras del objeto actual. Una vez realizado este proceso
        el carrito de compras debe vaciarse por completo.
        
        """
    
    def calcularValorCarrito(self):# Vale (0.2)
        valor_Carrito = 0
        temp = self.carritoDeCompras.first()

        if temp is not None:

            while temp != None:
                valor_unitario = temp.data.producto.valorUnitario
                unidades_Por_Producto = temp.data.unidades
                total_Valor_Producto = valor_unitario * unidades_Por_Producto
                valor_Carrito += total_Valor_Producto
                #print (str (valor_unitario)+" "+ str(unidades_Por_Producto) + " " + str(total_Valor_Producto) + " " + str(valor_Carrito))
                temp = temp.next

            return  valor_Carrito
        
        else:
            return 0
        """
        Este método se encarga de calcular el valor total a pagar por todos los
        productos del carrito. Al final debe retornarse este valor. 
        """
        