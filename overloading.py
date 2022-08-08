'''class sam:
    def aa(self,a):
        print(a)
    def aa(Self,a,b):
        print(a+b)
    def aa(self,a,b,c):
        print(a+b+c)
s=sam()
s.aa(10,30)'''       
class over:
    def load(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a 
o=over()
print("sum",o.load(10))
print("sum1",o.load(10,20))
print("sum",o.load(10,20,30))

#multiple args passing
class multiple:
    def add(self,*args):
        sum=0;
        for i in args:
            sum+=i
        print("add values:",sum)

m=multiple()
m.add(20)
m.add(40,50)
m.add(40,50,100)
m.add(40,50,100,200)
m.add(10,20,60,200,150)
m.add(10,20,30,40,50,60,70)