class Con:
    def __init__(self,name,age,college):
        print("Name",name)
        print("Age",age)
        print("College",college)

c=Con("sam","KCE",25)
class cc:
    def __init__(self,place,mail,company):
        self.p=place
        self.m=mail
        self.c=company
    def fun(self):
        print("place",self.p) 
        print("mail",self.m)
        print("company",self.c)
    def name(self):
        print("name",self.p)
c=cc("salem","sam@gmail.com","TCS")
c.fun()    

Senthil=cc("Senthil","abs",20)
Senthil.name()