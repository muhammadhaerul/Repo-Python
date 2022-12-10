#2. Buatlah program untuk mengecek apakah sebuah inputan merupakan IPv4,IPv6 atau bukan keduanya
import re

X = int(input())
IP = []
IPv4 = "^(([0-1]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]).){3}([0-1]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])$"
IPv6 = "^([0-9a-f]{1,4}:){7}([0-9a-f]{1,4})$"

for i in range(X):
    a = input()
    IP.append(a)
for i in IP:
    b = re.search(IPv4, i)
    c = re.search(IPv6, i)
    if b:
        print('IPv4')
    elif c:
        print('IPv6')
    else:
        print("Bukan IP Address")