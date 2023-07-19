# fundamenta features of object oriented programming
#            1.inheritance 2.encpsulation 3.polymorphism

#INHERITANCE:ineritance allows a class to inherit the property from the other class or we can say we can create a new class by using
#             the properties of other class
#   in inheritance newly created class is called as derived class  or child class and the already existing class is called as 
#   base class or parent class
#inheritance helps ous to reuse the 
#i.e by using inheritance we can inherit variable and methods from the base class to derived class


EXAMPLE: BASE CLASS
          feature 1
          feature 2
             |
             V
        DERIVED CLASS      #i.e derived class can have properites of base class and new properties of its own
          feature 1
          feature 2
          feature 3
            
            
#eg1
class animal:             #here eating is common in both classes so we can use inherit the method eating from class animal,i.e we can reuse the code
    def eating(self):   
        print("eating")
class dog:
    def eating(self):
        print("eating")
    def bark(self):
        print("barking")
        
#how to use inheritance
class baseclass:
    base_class_body
class derivedclass(baseclass):
    derived_class_body

#implementing iheritance for eg1
class animal:
    def eating(self):   
        print("eating")
class dog(animal):
    def bark(self):
        print("barking")

d=dog()
d.eating()
d.bark()

#eg 2                 #i.e by using inheritance we can inherit variable and methods from the base class to derived class
class animal:
    def __init__(self,name):
        self.name=name
class dog(animal):
    def display(self):
        print(self.name)

d=dog('German shepherd')
d.display()

#upto now we are only having single base class and single derived class so this is called as single level inheritance


    #MULTI LEVEL INHERITANCE 

        BASE CLASS      #grand father
         feature 1
             |
             V
        DERIVED CLASS 1    #father
          feature 1
          feature 2
          (features of base class + its own features i.e feature 2)
             |
             V
        DERIVED CLASS 2   #child
          feature 1
          feature 2
          feature 3
          (features of BASE CLASS + features of DERIVED CLASS 1 + features of its own features i.e feature 3)

#here we can see many levels its multi level inheritance i.e single base class having a derived class and that derived class is
#againg having another derives class
