print('Program pergerakan robot')
print('------------------------')

def robot():
    x = 0
    y = 0
    while True:
        str = input().lower()
        if str == 'start': 
            print(x,y)
            continue
        elif str == 'end':
            break
        elif x == 0 and y == 0:
            pass
            
        for i in str:
            if i == 'r':
                x += 1
            elif i == 'l':
                x -= 1
            elif i == 'u':
                y += 1   
            elif i == 'd':
                y -= 1
            else:
                continue
            print(x,y)
robot()