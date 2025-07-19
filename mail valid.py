import re 
input=input("enter a valid mail id:")
if re.match("^[a-z]+[\._]?+[a-z]+[@]\w+[.]\w{2,3}$",input):
    print("valid mail id",input)
else:
    print("invalid mail id",input)