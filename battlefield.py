from dinosaur import Dinosaur 
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot("Sam")
        self.dinosaur = Dinosaur("Mark", 30)

    def run_game(self):
        pass
    
    def display_welcome(self):
        print('Welcome to super hero battle must be 18 to enter')


    
    def battle_phase(self):
        # self.dinosaur.attack(self.robot)
        self.robot.attack(self.dinosaur)
        
        
    
        

    def display_winner(self):
        pass    