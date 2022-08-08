from abc import ABC
class bus(ABC):
    def volvo(self):
        print("HEllo")
        pass
class SRT(bus):
    def volvo(self):
        print("It a luxary bus")
class KPN(bus):
    def volvo(self):
        print("AC BUS")
class SAT(bus):
    def volvo(self):
        print("Luxary vechicle")       
s=SRT()
s.volvo()
s1=SAT()
s1.volvo()
b=bus()
b.volvo()         