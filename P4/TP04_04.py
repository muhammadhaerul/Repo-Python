#Program04: Robot movement operation

move = str(input('')).upper()

x = 0
y = 0

def movement(move):
  global x
  global y
  print(x, y)
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
        print(x, y)
        
movement(move)