class sam:
    def name(self):
        print("sampk")
class raja(sam):
    def name(self):
        super().name()
        print("raja") 
class arun(raja):
    def name(Self):
        super().name()
        print("ARUN")
s=arun()
s.name()                       