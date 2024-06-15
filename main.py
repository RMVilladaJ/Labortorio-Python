#%% INTEGRANTES:

#@author: Daniel Cardona Carvajal
#        Isabella Muñoz Castro
#        Rosa Maria Villada Jaramillo
#Grupo:580506004-10          

    

#%% IMPORTANTE - Instrucciones

# Agregue a esta carpeta las implementaciones de:
#      Nodo Doble
#      Lista Doble
#
#      Nota: Estas implementaciones no deben variar con respecto a las desarrolladas en clase. 
#            En caso de encontrar implementaciones diferentes su nota será de 0

# Este archivo "main" no debe modificarlo.


#%% Importaciones

from Supermercado import Supermercado
from datetime import date

supermercado=Supermercado()

#%% Carga de Usuarios

archivoUsuarios=open("Usuarios.csv","r")
header=archivoUsuarios.readline()
line=archivoUsuarios.readline()

while line!="":
    data=line.split(";")
    dataFechaNacimiento=data[3].split("/")
    fechaNacimiento=date(int(dataFechaNacimiento[2]),int(dataFechaNacimiento[1]),int(dataFechaNacimiento[0]))
    supermercado.agregarUsuario(data[0], data[1], data[2], fechaNacimiento)
    line=archivoUsuarios.readline()

archivoUsuarios.close()

#%% Carga de Productos

archivoProductos=open("Productos.csv","r")
header=archivoProductos.readline()
line=archivoProductos.readline()

while line!="":
    data=line.split(";")
    supermercado.agregarProducto(data[0], data[1], float(data[2]), int(data[3]))
    line=archivoProductos.readline()

archivoProductos.close()
#%% Carga de Carritos

archivoCarrito=open("RegistrosCarrito.csv","r")
header=archivoCarrito.readline()
line=archivoCarrito.readline()

while line!="":
    data=line.split(";")
    dataProductos=data[1].split("/")
    for dP in dataProductos:
        detalle=dP.split("-")
        supermercado.agregarProductoAlCarrito(data[0], detalle[0], int(detalle[1]))
    line=archivoCarrito.readline()    
  
#%% Verificación de Búsqueda Usuario
Nodo=supermercado.buscarUsuario("3944979762")
if Nodo!=None:
    print(Nodo.data)
else:
    print("El usuario no se encuentra registrado")
    
Nodo=supermercado.buscarUsuario("3944979764")
if Nodo!=None:
    print(Nodo.data)
else:
    print("El usuario no se encuentra registrado")

print()

#%% Verificación de Eliminación Usuario
print(supermercado.eliminarUsuario("3574151819"))
print(supermercado.eliminarUsuario("3574151810"))
Nodo=supermercado.buscarUsuario("3574151819")
if Nodo!=None:
    print(Nodo.data)
else:
    print("El usuario no se encuentra registrado")

print()

#%% Verificación Búsqueda de Productos
Nodo=supermercado.buscarProducto("1071")
if Nodo!=None:
    print(Nodo.data)
else:
    print("El producto no se encuentra en el inventario")
    
Nodo=supermercado.buscarProducto("1200")
if Nodo!=None:
    print(Nodo.data)
else:
    print("El producto no se encuentra en el inventario")
print()

#%% Verificación Eliminacion de Productos
print(supermercado.eliminarProducto("1090"))
Nodo=supermercado.buscarProducto("1090")
if Nodo!=None:
    print(Nodo.data)
else:
    print("El producto no se encuentra en el inventario")
print()

#%% Verificación Agregar Inventario

#print("Agregar al inventario")
supermercado.agregarInventario("1090", 20)
print()
supermercado.agregarInventario("1071", 26)
Nodo=supermercado.buscarProducto("1071")
if Nodo!=None:
    print(Nodo.data)
else:
    print("El producto no se encuentra en el inventario")
print()
 

#%% Verificación Mostrar Carrito
print("Mostrando carrito del usuario")
supermercado.mostrarCarrito("4573054365")
print()
supermercado.mostrarCarrito("3952104987")

#%% Verificación Agregar Productos Al Carrito

supermercado.agregarProductoAlCarrito("3952104987", "1007", 80)
print()
supermercado.mostrarCarrito("3952104987")  #Preguntarle a Felipe
print()

#%%
supermercado.comprarCarrito("4573054365")
print()
supermercado.comprarCarrito("3952104987")
print()
supermercado.mostrarCarrito("3952104987")
print()



Nodo=supermercado.buscarUsuario("3952104987")
if Nodo!=None:
    print("Compras del Usuario: "+str(Nodo.data.compras.size()))
else:
    print("El usuario no se encuentra registrado")

#suma
print (supermercado.SumarNumeros(67866, 67899787))