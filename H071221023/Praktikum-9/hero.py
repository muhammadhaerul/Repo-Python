class Human:
    def __init__(self, name, position):
        self.name = name
        self.__pos_x = position
        self._speed = 2
    
    def setMovement(self, move):
        if move == 'L':
            self.__pos_x -= self._speed
        if move == 'R':
            self.__pos_x += self._speed
            
    def getMovement(self):
        return self.__pos_x       

class Hero(Human):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack(self, target):
        target._health -= self._power

    def getHealth(self):
        return self._health

    def getSpeed(self):
        return self._speed

class Warrior(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 26
        self._armor = 30
        
    def special(self, target):
        self._armor = 45
        self._power = 32
        target._health -= self._power
    
class Assassin(Hero):
    def __init__(self, nama, pos_x):
        super().__init__(nama, pos_x)
        self._power = 35
        self._speed = 4

    def special(self, target):
        self._speed = 7
        self._power = 42
        target._health -= self._power

class Support(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special(self, target):
        self._speed = 6
        target._health += 150

