'''
a=[1,2,'soft','hard']
a.append('harish')
print(a)
a.insert(2,'type')
print(a)
print(len(a))
print(a)
a[0]=0
print(a)
a.reverse()
print(a)
a.remove(2)
print(a)
print(len(a))
print(a.pop())
print(a.pop(1))
b=a.copy()
print(b)
c=b.count('soft')
print(c)
n=int(input("Enter the list"))
list1=[]
for i in range(n):
       m=int(input("enter the list"))
       list1.append(m)
print(list1)
'''


a=[3,2,'hari','naveen','suresh','suresh',7,8,'akash']
a.append('gokul')
print(a)
a.insert(0,1)
print(a)
print(len(a))
print(a)
a[1]=2
print(a)     
a.remove('hari')
print(a)
a.reverse()
print(a)                  
print(type(a))        
print(a.pop())
print(a.pop(1))
print(a.pop(2))
b=a.copy()
print(b)
c=b.count(2)
print(c)
g=int(input("enter the list"))
list1=[]
for i in range(g):
    h=int(input("Enter the values in the list"))
    list1.append(h)
    print(list1)
