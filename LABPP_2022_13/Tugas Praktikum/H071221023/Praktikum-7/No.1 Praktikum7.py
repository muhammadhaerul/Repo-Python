import re

string = input()
x = re.compile("[A-Za-z02468]{40}[13579\s]{5}")
result = x.fullmatch(string)
if result :
    print("True")
else :
    print("False")    
    