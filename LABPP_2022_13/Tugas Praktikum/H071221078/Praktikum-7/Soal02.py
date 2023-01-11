import re

kodeipv4 = r'(25[0-5]|2[0-4][\d]|[0-1]?[\d]?[\d])'
kodeipv6 = r'[0-9a-fA-F]{1,4}'
v4 = fr'{kodeipv4}' + fr'.{kodeipv4}'*3
v6 = fr'{kodeipv6}' + fr':{kodeipv6}'*7

baris = int(input())
x = []

for i in range (baris):
    teks = input()
    x.append(teks)

for ip in x:
    ipv4 = re.fullmatch(v4, ip)
    ipv6 = re.fullmatch(v6, ip)

    if ipv4:
        print('IPv4')
    elif ipv6:
        print('IPv6')
    else:
        print('Bukan IP Address')