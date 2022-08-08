'''class Emp:
    def __init__(self,name,sal):
        self.n=name
        self.s=sal
        print("Name",self.n)
        print("college",self.s)
    def __mul__(self,other):
        print("Name",self.n)
        return self.s * other.days 

class payamount:
    def __init__(self,days):
        self.days=days

o=Emp("SAM",2000) 
o1=payamount(31)
print("total:",o*o1)       
'''
class Emp:
    def __init__(self,name,sal):
        self.n=name
        self.s=sal
        print("Name",self.n)
        print("college",self.s)
    def __mul__(self,other):
        print("Name",self.n)
        return self.s * other.days
class payamount:
    def __init__(self,days):
        self.days=days 
o=Emp("SAM",2000)
o1=payamount(31)
print("total:",o*o1)                  