import re
N = int(input())
IP = []
IPv4 = "^(([0-1]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]).){3}([0-1]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])$"
IPv6 = "^([0-9a-f]{1,4}:){7}([0-9a-f]{1,4})$"

for i in range(N):
    x = input()
    IP.append(x)
for i in IP:
    y = re.search(IPv4, i)
    z = re.search(IPv6, i)
    
    if y:
        print('IPv4')
    elif z:
        print('IPv6')
    else:
        print('Bukan IP Address')