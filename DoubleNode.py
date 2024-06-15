"""

@author: Daniel Cardona Carvajal
         Isabella Muñoz Castro
         Rosa Maria Villada Jaramillo
Grupo:580506004-10          
"""

class DoubleNode():
     

    def __init__(self,obj=None):
        self.__data=obj
        self.__prev=None
        self.__next=None
       

    @property 
    def data(self):
        return self.__data
    
    @property 
    def prev(self):
        return self.__prev
    
    @property 
    def next(self):
        return self.__next

  
    @data.setter
    def data(self, obj):
        self.__data=obj
    
    @prev.setter
    def prev(self, n):
        self.__prev=n
        
         
    @next.setter
    def next(self, n):
        self.__next=n

   
        

        


        


        