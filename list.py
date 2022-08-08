'''prop=['Tamil',5.5,70,'k']#declare the list(list[5]=0,1,2,3,4)
print(prop)
prop.append('software developer')#append insert the value in last
print(prop)
print(len(prop))#length of the list
prop.insert(4,15.5)#insert some specific location
print(prop)
prop[4]=1#replace the value in that location
print(prop)'''

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


