'''a={'name':'tamil','age':'25'}#dictionary have keys and values
print(a)
print(a['age'])

#duplicate not alowed
a1={'name':'raja','age':'25','age':'27'}
print(a1)
print(len(a1))
print(type(a1))

a={'name':'pp','age':25,'hobbies':'chatting',"friends":['hari','raj','ragul']}
'print(a)
b=a['hobbies']#shows it value
print(b)
b=a.get("name")#shows its value
print(b)
b=a.keys()#shows the keys
print(b)
a['bike']='fz'#add this in dictionary in last
print(a)
b=a.values()#showes all values
print(b)
a['car']='swift'#add this in dictionary in last
print(b)
b=a.keys()#shows all keys
print(b)






#updating
a={'name':'pp','age':25,'hobbies':'chatting',"friends":['hari','raj','ragul']}
print(a)
a['age']=24
print(a)
#update the dictionary using update 
a.update({'name':'tamil'})
print(a)

#pop method
a={'name':'pp','age':25,'hobbies':'chatting',"friends":['hari','raj','ragul']}
print(a)
a.pop('name')
print(a)

#del
del a['age']
print(a)

#clear

a.clear()
print(a)

#using loop
a={'name':'pp','age':25,'hobbies':'chatting',"friends":['hari','raj','ragul']}
print(a)
for i in a:
    print(i)
#values
for i in a:
    print(a[i])
#using values   
for i in a.values():
    print(i)  
#using keys
for i in a.keys():
    print(i)
#using items 
for i,j in a.item():
    print(i,j)     



a={'name':'pp','age':25,'hobbies':'chatting',"friends":['hari','raj','ragul']}
b={'name':'pp','age':25,'hobbies':'chatting',"friends":['hari','raj','ragul']}
a.add(b)
print(a)
a={'name':'pp',25:'age','hobbies':'chatting',"friends":['hari','raj','ragul']}
print(a)
b=int(input("Enter the number"))
print(b.values())'''
#using loop={}
user = input('enter a letter  ')
d = {'a': ' ', '2_1': 'a', '31':'d'}
for i in user:
    print(d[i])