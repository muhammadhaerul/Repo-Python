import re
x = input()
y = "^[A-Za-z02468]{40}[13579\s]{5}$"
result = re.search(y, x)
if result:
    print('True')
else:
    print('False')