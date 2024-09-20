from abc import ABC, abstractmethod

class Weapon(ABC):

    #Имя оружия
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    @property
    def name(self):
        return "меч"
    def attack(self):
        print("Игрок атакует мечом")

class Bow(Weapon):
    @property
    def name(self):
        return "лук"
    def attack(self):
        print("Игрок атакует луком")

class Gun(Weapon):
    @property
    def name(self):
        return "пистолет"
    def attack(self):
        print("Игрок атакует пистолетом")

class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def attack(self,monster):
        self.weapon.attack()
        print(f"Монстр {monster.name} побежден")

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} сменяет оружие на {weapon.name}")

class Monster:
    def __init__(self,name):
        self.name = name

#Инициализируем оружие
sword = Sword()
bow = Bow()
gun = Gun()

#Создаем монстров
monster1 = Monster("Годзилла")
monster2 = Monster("Гидра")
monster3 = Monster("Скелет")

#Создаем игрока
player = Fighter("Боец", sword)

#Игровой процесс
player.attack(monster1)
player.change_weapon(bow)
player.attack(monster2)
player.change_weapon(gun)
player.attack(monster3)
