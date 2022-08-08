'''s=('tamil','kevin',1,2,3)
print(s)
print(type(s))
'''
a=('tamil','sam',1,5,8,9,4)
print(a[0:4])
print(a[:2])
print(a[2:])
''''
#tuple have 2 methods methods
#count
b=(1,2,3,4,5,6,1,8,3,4,1,510,1)          #duplicate numbers
c=b.count(1)
print(c)
#index
n=(1,2,3,4,5,6,7)                #find the position for given number
d=n.index(1)
print(d)

#convert tuple to list
a=('sam','hari','monish','suresh')
b=list(a)
b[2]='naveen'
a=tuple(b)
print(a)
'''
''''
#append method
a=('sam','sathish','anu','priya')
b=list(a)
b.append("ganesh")
a=tuple(b)
print(a)
#adding tuple in tuple
a=('sam','sathish','anu','priya')
b=('ganesh',)
a+=b
print(a)

#remove
a=('sam','sathish','anu','pk','raja','naveen')
b=list(a)
b.remove('raja')
a=tuple(b)
print(a)
#add the values
a=('sam','naveen','hari')
a=a*3
print(a)
b=(1,2,3)
c=a+b
print(c)
n=(1,2,3,4,5,6,7)                #find the position for given number
d=n.index(1)
print(d)'''