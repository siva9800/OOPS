# OBJECT : Collection of data and its functionality(same as object in real life car,fan)

# CLASS : blue print of object using this class we can create many objects

# self  : it represent the current instance of class....whats the difference between ordinary function and methods of class, so in the methods we need to add a extra parameter
# inthe begining which refers to object itself,i.e the first parameter of any method is self self is not a keyword we can use any words
# other than self
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

#self parameter differtiate between instance variable (instance variable is variable belongs to a object) and 
#local variable) self refers to the current object
#init method is used to initalize the object it acts as a consturctore

#in the below code instance variable is self.name and local variable is name 
class person:
    def __init__(self,name):
        self.name=name # here self is nothing but person1 so person1.name = given name ('amul')
        name="ANVESH"
        print(name)
    def display(self):
        print("hello",self.name)
person1=person('SIVA')
person1.display()
#we can avoid self variable using static method
class person:
    @staticmethod
    def display():
        print('Hello')
p=person()
p.display()

#  OUTPUT:::::
# ANVESH
# hello SIVA
# Hello


# FIELDS : fields are nothing but these are the data belongs to a class,there are 2 types of fields they are instance variable(variable belongs to a object or instance)
#         and class varible(varible belongs to class,i.e a single variable belongs to all the objects in the class   ) 
class student:
    clg='aditya'  #here college is class variable
    
    def __init__(self,rollno,name):  #here rollno and name are instance or object varible
        self.rollno=rollno
        self.name=name
    def display(self):
        print("student name is :",self.name)
        print("student roll no is :",self.rollno)
        print("He is From the college:",student.clg)  #we call class varible with classname.class variable name
s1=student('21mh5a0351','Siva')
s2=student('21mh5a0322','sai')
s1.display()
print('....')
s2.display()
#  OUTPUT:::::
# student name is : Siva
# student roll no is : 21mh5a0351
# He is From the college: aditya
# ....
# student name is : sai
# student roll no is : 21mh5a0322
# He is From the college: aditya



# fundamenta features of object oriented programming
#            1.inheritance 2.encpsulation 3.polymorphism
