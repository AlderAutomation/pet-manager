import random

class Pet(): 
    def __init__(self, name: str) -> None:
        self.name = name
        self.age = 0
        self.sex = self.get_sex()
        self.art = "./assets/images/Sprite-0001.png"
        self.isAlive = True
        self.isSick = False
        self.food_likes = []
        self.toy_likes = []
        self.hunger = Level("Hunger")
        self.clean = Level("Clean")
        self.social = Level("Social")
        self.entertainment = Level("Entertainment")
        self.bathroom = Level("Bathroom")
        self.happy = self.get_happiness()


    def get_happiness(self) -> float:
        """Take all other levels and gets the average number. Use this to set self.happiness"""
        total = 0
        level_list = [self.hunger.amount, self.clean.amount, self.social.amount, self.entertainment.amount, self.bathroom.amount]
        for i in level_list: 
            total = total + i

        return total / len(level_list)


    def get_sex(self) -> str:
        if random.randrange(1,3) == 1:
            return "male"
        else: 
            return "female"


class Level:
    def __init__(self, name:str) -> None:
        self.name = name
        self.amount = 50

    def raise_level(self, amount:int):
        self.amount = self.amount + amount

    def lower_level(self, amount:int):
        self.amount = self.amount - amount



