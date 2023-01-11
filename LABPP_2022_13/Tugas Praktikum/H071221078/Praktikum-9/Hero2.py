from Hero import Warrior,Assasin,Support

warrior = Warrior("Bambang", position=10)
assassin = Assasin("Joko", position=25)
support = Support("Udin", position=30)

print("health (before) ", warrior.getHealth())
assassin.attack(warrior)
print("health (after) ", warrior.getHealth())
print("-"*10)

print("Warrior (health) ", warrior.getHealth())
print("Support (speed) : ", support.getSpeed())

support.special(warrior)

print("Warrior (health) ", warrior.getHealth())
print("Support (speed) : ", support.getSpeed())