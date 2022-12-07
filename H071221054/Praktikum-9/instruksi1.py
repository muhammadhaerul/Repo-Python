from hero import Warrior, Assasin, Support

warrior = Warrior("Bambang",pos_x = 10)
assassin = Assasin("Joko", pos_x = 25)
support = Support("Udin", pos_x = 30)

print(f"health (before) : {warrior.getHealth()}")
assassin.attack(warrior)

print(f"health (after)  : {warrior.getHealth()}")

print("-" * 15)


print(f"Warrior (health) : {warrior.getHealth()}")
print(f"Support (speed)  : {support.getSpeed()}")

support.special(warrior)

print(f"Warrior (health) : {warrior.getHealth()}")
print(f"Support (speed)  : {support.getSpeed()}")