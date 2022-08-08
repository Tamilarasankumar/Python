'''a={'naveen','pk','anu','sathish','pk'}#set can't allowed duplicates
print(a)
#update
ss={'sam','pk','anu','sathish'}
ss.update('raja')#letters are print separate
print(ss)



#convert to list to update
b={'sam','raja','ganesh','gopi'}
li=['vimal']
b.update(li)
print(b)


#remove and discard 
a={1,2,3,'sam','pk'}
print(a)
a.remove('sam')
print(a)
a.discard(2)
print(a)

#pop method
s={'sam','pk','hari','naveen'}
s1=s.pop()
print(s1)
print(s)'''



#add method
a={'sam','hari','anu'}
print(a)
a.add('viji')#add the value in set
print(a)

#accessing
a={'sam','hari','anu'}
for  i in a:#print uncontinuously
    print(i)

#check the set in present or  not[]
a={'sam','pk','anu'}
print("pk"in a)#if the value is here  it's true otherwise false