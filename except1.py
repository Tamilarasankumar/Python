try:
    a=int(input("enter the value"))
except ValueError as e:
    print("Value Error:",e)
    raise KeyError("that is value")
else:
    print("value is",a)
finally:
    print("Hello the words")
            
    