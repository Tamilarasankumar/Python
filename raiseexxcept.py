'''#raise except is used to give the user defind error using raise keyword.
try:
    pas=input("St the password")
    con=input("Confirm password")
    if pas !=con:
        raise AnnamalaiError

    else:
        print("Password was set successfully")
except AnnamalaiError as an:
    print(an) 
finally:
    print("successfully login")              '''