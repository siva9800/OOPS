#accecing private and public data                         *****1.we can access class through object
#we us __ to make private type variable or attribute
class student:
    college='AEC'#instant variable use this if its common for every method
    def __init__(self,name,age):
        self.__name=name#private name
        self.age=age
    def SetData(self,new):#to modify private data and access it we use another functions
        self.__name=new
    def GetData(self):#we cant print private data so we call in this function and print this functions
        print(self.__name,self.age)
s1=student('Ashok',98)   #<---This is object
s1.age=13
s1.SetData('don')
s2=student('sudir',32)
s1.GetData()
#print(s1.age)
#print(s1.college)
