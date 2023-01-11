X = int(input(' '))
Y = int(input(' '))

for i in range(1,Y+1):
    print(i, end='\n' if i % X == 0 else ' ')