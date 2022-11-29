class Human:
    def __init__(self, name, position):
        self.name = name
        self.__position = position
        self._speed = 1
    
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setMovement(self, arah):
        if arah == "L":
            self.__position = self.__position - self._speed
        elif arah == "R":
            self.__position = self.__position + self._speed
    def getMovement(self):
        return self.__position

class Hero(Human):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
    
    def setPower(self, power):
        self._power = power 
    def getPower(self):
        return self._power

    def setHealth(self, health):
        self._health = health 
    def getHealth(self):
        return self._health

    def setArmor(self, armor):
        self._armor = armor 
    def getArmor(self):
        return self._armor

    def setSpeed(self, speed):
        self._speed = speed
    def getSpeed(self):
        return self._speed

    def attack(self, target):
        target._health = target._health - self._power

class Warrior(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 26
        self._armor = 30
    
    def special(self, target):
        self._armor = 45
        self._power = 32
        target._health = target._health - self._power

class Assasin(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 35
        self._speed = 4
        
    def special(self, target):
        self._speed = 7
        self._power = 42
        target._health = target._health - self._power

class Support(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._health = 500
        self._armor = 8
        self._speed = 4
    
    def special(self, target):
        self._speed = 6
        target._health = target._health + 150

warrior = Warrior("bambang",pos_x = 10)
assassin = Assasin("joko", pos_x = 25)
support = Support("udin", pos_x = 30)

# sebelum
print("health (before) :", warrior.getHealth())
assassin.attack(warrior)
# sesudah
print("health (after)  :", warrior.getHealth())

print("-" * 25)

# sebelum
print("Warrior (health) :", warrior.getHealth())
print("Support (speed)  :", support.getSpeed())