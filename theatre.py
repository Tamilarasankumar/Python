'''seat=30
while seat>0:
    amt=int(input("Enter the amount:"))
    if amt>=120:
        print("You bought",seat,"ticket")
        seat-=1
    else:
        print("Insufficent amount to buy ticket")
        '''

#Theatre ticket booking
seat=30
while seat>0:
 qty=int(input("Tell us how many tickets you want:"))
 payable=qty*20
 amt=int(input("Enter the amount"))
 if amt>=payable:
      print("You bought",qty,"ticket")
      seat-=qty
 else:    
    print("Insufficent amount to buy ticket payable amount is",payable)    
