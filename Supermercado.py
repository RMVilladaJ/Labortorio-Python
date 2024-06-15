"""

@author: Daniel Cardona Carvajal
         Isabella Muñoz Castro
         Rosa Maria Villada Jaramillo
Grupo:580506004-10          
"""

"""
Este archivo representa la estructura general de la solución. Aquí y en el
módulo de usuario deben realizar la construcción de los diferentes métodos.
No agregue métodos ni cambie el nombre de los existentes. En cada método se
especifica la funcionalidad a desarrollar.
"""
from DoubleList import DoubleList
from Usuario import Usuario
from Producto import Producto
from RegistroCarrito import RegistroCarrito

class Supermercado():
    def __init__(self):
        self.usuarios  = DoubleList() # Inicialice este atributo como una Lista Doble
        self.productos = DoubleList() # Inicialice este atributo como una Lista Doble
        
    def agregarUsuario(self, cedula, nombre, apellido, fechaNacimiento):# Vale (0.2)

        usuario_Existente = self.buscarUsuario(cedula)

        if usuario_Existente == None:
            usuario_Nuevo = Usuario(cedula,nombre,apellido,fechaNacimiento)
            self.usuarios.addLast(usuario_Nuevo)
        else:
             print("El usuario ya existe")

        """
        Este método recibe la cedula, nombre, apellido y fecha de nacimiento de
        un objeto de tipo Usuario.
        
        Se deben agregar los nuevos usuarios de forma tal que:
            1. No existan usuarios repetidos
            2. Los nuevos usuarios queden al final de la lista doble
        """
        
    
    
    def buscarUsuario(self, cedula):# Vale (0.2)
        
        temp = self.usuarios.first()

        while temp !=None and temp.data.cedula!=cedula:
            temp=temp.next
        
        if temp == None:
            return None
        else:
            return temp
        
        """
        Este método realiza la búsqueda del usuario por cedula en la lista de usuarios
        Al finalizar debe retornar el Nodo Doble donde se encuentra el usuario 
        o en su defecto un valor de None
        
        """
               
     
    def eliminarUsuario(self, cedula):# Vale (0.2)

        temp = self.buscarUsuario(cedula)
        if temp != None:
            self.usuarios.remove(temp)
            return temp.data
        else:
            return None

        """
        Este método realiza la eliminación del usuario por cedula de la lista de usuarios
        Al finalizar debe retornar el objeto de tipo usuario eliminado o en su 
        defecto un valor de None
        
        """           
        
    
    def agregarProducto(self, codigo, descripcion, valorUnitario, unidades): # Vale (0.2)
        
        producto_Existente = self.buscarProducto(codigo)

        if producto_Existente == None:
            producto_Nuevo = Producto(codigo,descripcion,valorUnitario,unidades)
            self.productos.addFirst(producto_Nuevo)
        else:
             print("El producto ya existe")

        """
        Este método recibe el codigo, descripcion, valor unitario y número de unidades
        de un objeto de tipo Producto. 
        
        Se deben agregar los nuevos Productos de forma tal que:
            1. No existan productos repetidos
            2. Los nuevos productos queden al principio de la lista doble
        """
            
   
    def buscarProducto(self, codigo):# Vale (0.2)
        tempNode = self.productos.first()        

        while (tempNode !=None and tempNode.data.codigo!=codigo):
            tempNode=tempNode.next

        if tempNode == None:
            return None
        else:
            return tempNode
        """
        Este método realiza la búsqueda del producto por codigo en la lista de productos
        Al finalizar debe retornar el Nodo Doble donde se encuentra el producto 
        o en su defecto un valor de None
        
        """
    
    def eliminarProducto(self, codigo):# Vale (0.5)

        nodo_producto_Existente = self.buscarProducto(codigo)
        if nodo_producto_Existente != None:
            self.productos.remove(nodo_producto_Existente)
            temp_user_node = self.usuarios.first()      
            while (temp_user_node != None):
                temp_user = temp_user_node.data
                nodo_producto_En_Carrito = temp_user.buscarEnCarrito(nodo_producto_Existente.data)
                if nodo_producto_En_Carrito != None:
                    temp_user.eliminarDelCarrito(nodo_producto_Existente.data)
                temp_user_node = temp_user_node.next

            return nodo_producto_Existente.data
        else:
            return None
        """
        Este método realiza la eliminación del producto por codigo de la lista de productos
        
        Al eliminarse un producto de la lista de productos, éste debe eliminarse
        tambien de cada una de los carritos de compras de los usuarios.         
        
        Al finalizar debe retornar el objeto de tipo producto eliminado o en su 
        defecto un valor de None
        
        """   
    
    def agregarInventario(self, codigo, unidades):# Vale (0.2)

        producto_Existente = self.buscarProducto(codigo)

        if producto_Existente is not None:
            producto_Existente.data.unidades += unidades
        else:
            print("No existe un producto con el codigo " + codigo)
        """
        Este método realiza la agregación de nuevas unidades a las ya existentes
        de un producto en específico del cual se conoce su código.
        
        Si no se encuentra el producto debe imprimirse un mensaje de error
        """

        
    def agregarProductoAlCarrito(self, cedula, codigo, unidades):# Vale (0.5)

        nodo_Usuario_Existente = self.buscarUsuario(cedula)
        nodo_Producto_Existente = self.buscarProducto(codigo)

        if (nodo_Usuario_Existente != None and nodo_Producto_Existente != None):
            unidades_Disponibles = nodo_Producto_Existente.data.unidades
            registro_Carrito_Existente = nodo_Usuario_Existente.data.buscarEnCarrito(nodo_Producto_Existente.data)

            if (registro_Carrito_Existente != None): 
                unidades = unidades + registro_Carrito_Existente.data.unidades

                if unidades_Disponibles >= unidades:
                    registro_Carrito_Existente.unidades = unidades
                else:
                    registro_Carrito_Existente.data.unidades = unidades_Disponibles
                    print("El numero de unidades solicitadas, excede el limite de unidades disponibles, solo se agregaron "+ str(unidades_Disponibles) + " unidades de " + str(nodo_Producto_Existente.data.descripcion))
            else:           
                  
                if unidades_Disponibles >= unidades:
                    nuevo_registro = RegistroCarrito(nodo_Producto_Existente.data, unidades)
                else:
                    nuevo_registro = RegistroCarrito(nodo_Producto_Existente.data, unidades_Disponibles)
                    print("El numero de unidades solicitadas, excede el limite de unidades disponibles, solo se agregaron "+ str(unidades_Disponibles) + " unidades de " + str(nodo_Producto_Existente.data.descripcion))
                nodo_Usuario_Existente.data.carritoDeCompras.addLast(nuevo_registro)

        """ 
        Este método realiza la agregación de un producto al carrito de un usuario
        Si el usuario existe y el producto existe,debe crearse un nuevo RegistroCarrito
        el cual contiene la información del producto a comprar y las unidades requeridas.
        
        En caso tal de que las unidades requeridas excedan el total de unidades disponibles,
        el RegistroCarrito únicamente incluirá como número de unidades requeridas las que estén disponibles.
        SOLO en este caso debe imprimirse un mensaje anunciando la modificación, 
        mencionando cuantas unidades fueron agregadas al carrito
        
        En este punto NO se reducirá el número de unidades disponibles, este proceso 
        se realiza en el método de compraCarrito
        """
      
  
    def comprarCarrito(self, cedula):# Vale (0.8)

       usuario = self.buscarUsuario(cedula)
       

       if (usuario != None):
            producto_En_Carrito = usuario.data.carritoDeCompras.first()
            while (producto_En_Carrito != None):

                producto = self.buscarProducto(producto_En_Carrito.data.producto.codigo)
                unidades_Disponibles = producto.data.unidades
                unidades_Carrito = producto_En_Carrito.data.unidades

                if unidades_Disponibles < unidades_Carrito:
                    unidades_Carrito = unidades_Disponibles
                    print("El numero de unidades solicitadas, excede el limite de unidades disponibles, solo se agregaron "+ str(unidades_Carrito) + " unidades")
                
                producto.data.unidades = unidades_Disponibles - unidades_Carrito
                producto_En_Carrito = producto_En_Carrito.next

            self.mostrarCarrito(cedula)
            usuario.data.comprarCarrito()
            #self.mostrarCarrito(cedula)

                

       else:
            print("El usuario no existe")
      
    
    """ 
        Este método efectua la compra del carrito de compras de un usuario del cual se conoce
        su cédula. 
        
        En este método se debe validar nuevamente que las unidades requeridas 
        no superen la unidades disponibles en el carrito. Esto porque durante el proceso
        de llenado del carrito puede haber sucedido que otro usuario haya agotado las 
        existencias de un producto o que ya no hayan todas las que éste usuario requiere. 
        
        En caso de que las unidades requeridas no sean suficientes, se venderan
        al usuario las unidades en existencia. SOLO en este caso debe imprimirse
        un mensaje anunciando la modificación, mencionando cuantas unidades 
        fueron vendidas finalmente
        
        En este punto DEBE reducirse el número de unidades disponibles para el objeto comprado.

        Adicionalmente debe llamarse el método de mostrarCarrito y al método 
        comprarCarrito del usuario
        
        En caso de no encontrar al usuario, debe imprimirse el mensaje de error
        
        """     
            
                    
    def eliminarProductoDeCarrito(self, cedula, codigo):# Vale (0.2)
        usuario_Existente = self.buscarUsuario(cedula)
        Producto_Existente = self.buscarProducto(codigo)

        if usuario_Existente != None and Producto_Existente != None:
            usuario_Existente.eliminarDelCarrito(Producto_Existente)
        
        """
        Este método elimina un producto del carrito de compras de un usuario,
        en caso de que ambos existan.
        """
        
        
    def vaciarCarrito(self, cedula):# Vale (0.2)

        usuario_Existente = self.buscarUsuario(cedula)

        if usuario_Existente != None:
            usuario_Existente.carritoDeCompras = DoubleList()

        """
        Este método elimina TODOS los productos del carrito de compras de un usuario
        existente dada su cédula
        
        """
            
    def mostrarCarrito(self, cedula): # Vale (0.4)
        
        nodo_Usuario = self.buscarUsuario(cedula)

        if nodo_Usuario != None:
          print (nodo_Usuario.data.cedula + " " + nodo_Usuario.data.nombre + " " + nodo_Usuario.data.apellido) 

          temp_Carrito = nodo_Usuario.data.carritoDeCompras.first()

          while temp_Carrito != None:
              print(temp_Carrito.data) 
              temp_Carrito = temp_Carrito.next
          print("El valor total a pagar es: " + str(nodo_Usuario.data.calcularValorCarrito()))
        else:
            print("El usuario con cedula "+ cedula + "no existe")

        """
        Este método se encarga de mostrar el resumen del carrito de compras.
        Este resumen debe incluir la cedula del usuario, el nombre completo del usuario
        y debe mostrar todos los productos del carrito del usuario y el valor 
        total a pagar por todo el carrito. En caso de que no exista el usuario 
        el método debe imprimir el mensaje de error. 
        """

    def SumarNumeros(self,numero1 , numero2):

        suma = numero1 + numero2

        return suma

    

            
    
