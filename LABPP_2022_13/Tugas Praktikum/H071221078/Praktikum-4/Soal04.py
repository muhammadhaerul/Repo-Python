def pergerakan_robot():
    x = 0
    y = 0

    while True:
        operasi= input()
        if operasi == "START":
            x -= x
            y -= y
            print (x, y)
            continue
        elif operasi == "END":
            break
        for i in operasi:
            if i == "R":
                x += 1
                print(x, y)
            elif i == "L":
                x -= 1
                print(x, y)
            elif i == "U":
                y += 1
                print(x, y)
            elif i == "D":
                y -= 1
                print(x, y)
            else:
                pass
        
pergerakan_robot()