class students:
    def name1(name):
       if name=='hari':
            print("name is hari")
       elif name=='mohan':
          print("name is mohan")
       else:
        print("no name")
    name1('hari')  
class age(students):
    def number(no):
        if no==5:
            print('five')
        else:
            print('nothing')
    number(5)
a=age()
a.number()
a.name1()            
