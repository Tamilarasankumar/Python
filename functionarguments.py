'''def ask(purpose):#calling with one argument
    if purpose=='economy': print("Dont wprry")
    elif purpose=='Health' : print("Gov't business")
    elif purpose=='relief':print("life the light")
    else:print("Bharat matha ji jay")
ask('Health')
ask('relief') 
ask('business')


def prompt(qual,ref):#calling with two argument
    if qual=='ug' and ref=='HR':print('you are in UK team')
    elif qual=='diploma' and ref=='testlead':print("Test Associate")
    elif qual=='diploma' and ref=='testlead':print('test association')
    else:print("you are hired")
prompt('ug','HR') 
prompt(ref='testlead',qual='diploma')   '''

def register(name,location,prefix='mr/miss/mrs'):
    if location=='salem':
        print(prefix,name,'has approved in',location)
    elif location=='chennai':
        print(prefix,name,'has gone under waiting states since its',location)
    else:print("Business not approved")
register("zealous Tech Corp",'salem') 
register("annamalai automobiles','chennai","Mr.")
register("has been completed",'sss')           