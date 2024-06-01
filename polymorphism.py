class Base: 
    def __init__(self): 
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
    def showData(self):
        print(self.__c)    


class Derived(Base): 
    def __init__(self): 
  
        # Calling constructor of 
        # Base class 
        Base.__init__(self) 
        print("Calling private member of base class: ") 
        print(self.__c) 
  
  
# Driver code 
obj1 = Base() 
print(obj1.a)
obj =Base()
obj.showData()

