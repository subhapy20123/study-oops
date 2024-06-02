# #inheritance by multiple inheritance
#Method 1 

class A:
    def displayA(self):
        print("How r you")

class B:
    def displayB(self):
        print("Hello World")

class C(A,B):
    def displayC(self):
        print("My name is raj")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()

#Method 2

class mother:

     def mother(self):
         print(self.mothername)


class father:
    
     def father(self):
         print(self.fathername)


class son(mother,father):
     def son(self):
          print("mother",self.mothername)
          print("father",self.fathername)
          print("son",self.sonname)

obj=son()
obj.mothername="dipali majumdar"
obj.fathername="khokan majumdar"
obj.sonname="biswnath"
obj.son()





                        

