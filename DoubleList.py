"""

@author: Daniel Cardona Carvajal
         Isabella Muñoz Castro
         Rosa Maria Villada Jaramillo
Grupo:580506004-10          
"""

from DoubleNode import DoubleNode

class DoubleList():
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0
    
    def size(self):
        return self.__size

    #retorna verdadero si es nulo
    def isEmpty(self):
        return self.size()==0
    
    #retorna cabecera
    def first(self):
        return self.__head
    
    #retorna cola
    def last(self):
        return self.__tail
    
    #Agregar al inicio de la lista
    def addFirst(self, obj):
        n = DoubleNode(obj)
        if self.isEmpty():
            self.__head = n
            self.__tail = n
        else:
            n.next=self.__head
            self.__head.prev = n
            self.__head = n
        self.__size += 1
        
    #Agregar al final
    def addLast(self, obj):
        n = DoubleNode(obj)
        if self.isEmpty():
             self.__head = n
             self.__tail = n
        else:
            self.__tail.next = n
            n.prev = self.__tail
            self.__tail = n
        self.__size+=1
    
    #Eliminar al inicio
    def removeFirst(self):
        if not (self.isEmpty()):
            temp_dato = self.__head.data
            if self.size() == 1:
                self.__head == None
                self.__tail == None
            else:
                temp = self.__head.next 
                self.__head.next = None
                temp.prev = None
                self.__head = temp
            self.__size-=1
            return temp_dato
        else:
            return None

    
    #Eliminar al final
    def removeLast(self):
        if not (self.isEmpty()):
            temp_Dato = self.__head.data
            if self.size() == 1:
                self.__head == None
                self.__tail == None
            else:
                temp = self.__tail.prev
                self.__tail.prev = None
                temp.next = None
                self.__tail = temp
            self.__size-=1
            return temp_Dato
        else:
            return None
    
    def remove(self,n):
        if n == self.__head:
            self.removeFirst()
        elif n == self.__tail:
            self.removeLast()
        else:
            temp_Dato = n.data
            temp_prev = n.prev
            temp_next = n.next
            temp_prev.next = temp_next
            temp_next.prev = temp_prev
            n.next = None
            n.prev = None
            self.__size-= 1
            return temp_Dato
        
    def addAfter(self, n, e):
        if n == self.__tail:
            self.addLast(e)
        else:
            m = DoubleNode(e)
            temp = n.next
            n.next = m
            m.prev = n
            m.next = temp
            temp.prev = m
            self.__size +=1
    
    def addBefore(self, n, e):
        if n == self.__tail:
            self.addFirst(e)
        else:
            m = DoubleNode(e)
            temp = n.prev
            temp.next = m
            m.prev = temp
            m.next = n
            n.prev = m
            self.__size +=1
    
    def print(self):
        if self.isEmpty():
            print("")
        else:
            temp = self.__head
            while temp != None:
                print(temp.data)
                temp = temp.next


        




        



        
    
