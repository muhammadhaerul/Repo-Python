from hero import Warrior, Assasin, Support,Human,Hero
human = Human("nama1", 10)

# print(human.getMovement())
# human.setMovement("L")
# print(human.getMovement())\

# hero1 = Hero("hero1", 5)
# hero2 = Hero("hero2", 8)
# print(hero1.__dict__)
# print(hero2.__dict__)
# hero2.attack(hero1)
# print(hero1.__dict__)
# print(hero2.__dict__)

warrior = Warrior("warrior", 15)
assassin = Assasin("assassin", 9)
support = Support("support", 5)
print(assassin.__dict__)
print(support.__dict__)
support.special(assassin)
print(assassin.__dict__)
print(support.__dict__)
