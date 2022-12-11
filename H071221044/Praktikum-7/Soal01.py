#1. Buatlah sebuah program untuk mengecek sebuah string S sesuai dengan kondisi
import re
string_s = str(input())
s = "^[A-Za-z02468]{40}[13579\s]{5}$"
result = re.search(s, string_s)

if result:
    print("True")
else:
    print("False")