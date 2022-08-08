#exception:user defined error.using except keyword to give the error what we want to appear on the screen.

try:
    a=10
    b=0
    c=a/b
    print(c)
except Exception as e:
    print(e)
try:
    a=10
    b=0
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print("Error",e)
#name Error:
try:
    name="sam"
    print("college")
except NameError as e:
    print("Name error",e)
#value Error 
try:
    num=int(input("Enter the number"))
    print(num)
except ValueError as e:
    print("value error:",e)
#Index error
try:
    li=[10,45,20,30,48]
    print(li[7])
except IndexError as e:
    print("Index Error",e)
#Key Error
try:
    dd={"Name":"sam","name1":"pk"}
    print(dd['age'])
except KeyError as e:
    print("Key error:",e) 
#Attribute Error:
try:
    class a:

        pass
    A=a()
    a.hello()
except AttributeError as e:
    print("Attribute Error:",e)                           


