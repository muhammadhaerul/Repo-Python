from hero import Warrior, Assassin, Support
warrior = Warrior("Bambang", 10)
assassin = Assassin("Joko", 25)
support = Support("Udin", 30)

# sebelum
print("health (before)", warrior.getHealth())
assassin.attack(warrior)

# sesudah
print("health (after)", warrior.getHealth())
print("-"*20)

# sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())
support.special(warrior)

# sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed): ",support.getSpeed())