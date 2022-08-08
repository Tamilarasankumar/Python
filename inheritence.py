class upstox:
    def lowcast(self):
        print("Monthly charge",self)
    lowcast("20")    
class Angel(upstox):
    def brokerage(self):
        print("yearly charge",self)
    brokerage("240")    
c=Angel()
c.brokerage()
c.lowcast()

