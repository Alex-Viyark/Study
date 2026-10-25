class Character:
    _min_hp=0
    _max_xp=100
    def __init__(self,username,level:int=0, rang:str='civilian',armor=False,helmet=False):
        self.username=username
        self.level=level
        self.rang=rang
        self.armor=armor
        self.helmet=helmet
    #информация о персонаже
    def info(self):
        print(f"Никнейм: {self.username}")
        print(f"Уровень: {self.level}")
        print(f"Пол: {self.rang}")
        print(f"Курс: {self.armor}")
        print(f"Группа: {self.helmet}")

class Knigt(Character):
    def __init__(self,rang:str='Kniht'):
        pass
class Dragon(Character):
    pass
class World:
    pass
class Forest(World):
    pass
class Village(World):
    pass
class Workshop:
    pass
class Shop:
    pass
