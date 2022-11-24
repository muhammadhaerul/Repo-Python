import re

string_S = str(input())
b = "^[A-Za-z02468]{40}[13579\s]{5}$"
result = re.search(b, string_S)

if result:
    print('True')
else:
    print('False')