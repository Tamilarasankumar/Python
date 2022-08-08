'''#for i in range(100,200,+2): print(i,end=" ")

a=[1,2,3,4]
a.pop(0)
print(a)
a.remove(2)
print(a)  
a.append(5) 
print(a)
'''



try:
    a=10
    b=0
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print(e)    
    