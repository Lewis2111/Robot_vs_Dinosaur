from weapon import Weapon

class Dinosaur:
    
    def __init__(self, name, attack_power):
        self.name = "Mark"
        self.health = 70
        self.attack_power = 30
        
    def attack(self, robot):
    
        robot.health -= self.attack_power
        