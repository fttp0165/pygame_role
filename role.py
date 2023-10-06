import random

class BaseAttribute():
    def __init__(self,attack=10,defense=10,dodge=0.1,magic_attack=10,magic_defense=5,lucky=1) -> None:
        self.attack=attack
        self.defense= defense
        self.dodge=dodge
        self.magic_attack=magic_attack
        self.magic_defense=magic_defense
        self.lucky=lucky


class Role(BaseAttribute):
    def __init__(self,name,hp=100,hp_max=100,mp=100,mp_max=100,level=1,experience=0,experience_max=100) -> None:
        super().__init__() 
        self.name=name
        self.hp=hp
        self.hp_max=hp_max
        self.mp=mp
        self.mp_max=mp_max
        self.level=level
        self.experience=experience
        self.experience_max=experience_max

    def take_damage(self,damage):
        if self.dodge_chance():
            print("Miss")
        else:
            #傷害減防禦
            damage_after_defense = max(damage - self.defense,0)
            print(f'damage_after_defense:{damage_after_defense}')
            self.hp -= damage_after_defense
            print(f'{self.name} 受到{damage_after_defense}傷害')

    def dodge_chance(self):
        return random.random() <self.dodge        
    
    def __str__(self) -> str:
        return f' name:{self.name}\n LV:{self.level}\n HP:{self.hp}/{self.hp_max}\n MP:{self.mp}/{self.mp_max}\n Ex:{self.experience} / {self.experience_max}\n Attack:{self.attack}'


class Enemy(Role):
    def __init__(self, name, hp=100, hp_max=100, mp=100, mp_max=100, level=1, experience=0, experience_max=100) -> None:
        super().__init__(name, hp, hp_max, mp, mp_max, level, experience, experience_max)

benny=Role('Benny')
benny.attack=15
frogger=Role('Frogger')
print(benny)
print(frogger)
frogger.take_damage(benny.attack)
print(frogger)