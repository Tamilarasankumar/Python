class college:
    def name(self):
        print("College is good")
class clgname(college):
    def name1(self):
        print("KSR COLLEGE")
class clglocation(college):
    def name2(self) :
        print("Thiruchengode")
class placement(clgname,clglocation,college):
    def name3(self):
        print("Good")
p=placement()
p.name1()
p.name()
p.name3()
p.name2()                      

