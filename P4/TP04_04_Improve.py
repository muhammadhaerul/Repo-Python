#Program04: Robot Movement Operation

x = 0
y = 0

def movement(move):
  global x
  global y
  for i in move:
    match i:
      case 'R':
        x += 1
        print(x, y)
      case 'L':
        x -= 1
        print(x, y)
      case 'U':
        y += 1
        print(x, y)
      case 'D':
        y -= 1
        print(x, y)
      case _:
        pass

condition = True

while(condition):
    s = str(input('')).upper()
    if s == 'START':
        x = 0
        y = 0
        print(x, y)    
    elif s == 'END':
      condition = False
    else:
      movement(s)
        