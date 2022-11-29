x = 0
y = 0
def perpindahan(perintah):
    global x
    global y
    for i in (perintah):
        if i == 'R':
            x = x+1
            print(x,y)
        elif i == 'L':
            x = x-1
            print(x,y)
        elif i == 'U':
            y = y+1
            print(x,y)
        elif i == 'D':
            y = y-1
            print(x,y)
        else:
            pass

condition = True
while condition:
    perintah = input("Perpindahan: ").upper()
    if perintah == 'START':
        x = 0
        y = 0
        print(x,y)
    elif perintah == 'END':
        print('Program Selesai')
        condition = False
    else:
        perpindahan(perintah)
        