# input(di dalam looping)

x = 0
y = 0

def pergerakan_robot():
    global x
    global y
    for i in operasi:
        if i == "R":
            x = x+1
            print(x,y)
        elif i == "L":
            x = x-1
            print(x,y)
        elif i == "U":
            y = y+1
            print(x,y)
        elif i == "D":
            y = y-1
            print(x,y)

while True:
    operasi = input()
    if operasi == "end":
        break
    pergerakan_robot()
        