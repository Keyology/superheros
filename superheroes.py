import random


class Hero:
    def __init__(self, name, current_health, starting_health =100, ):
        self.name = name 
        self.abilities = list()
        self.starting_health = starting_health 
        self.current_health = starting_health 
    
    def add_ability(self, ability):
        self.abilities.append(self.ability)
    
    def attack(self):
        #will get back to this function 
        for hero_attack in self.abilities:
            return attack()
    
    def take_damage(self, damage):
        self.current_health -= damage
    
    def is_alieve(self):
        if self.current_health >= 0:
            return True
            print('hero is alieve')
        else:
            return False
            print('hero is dead')
    
    def fight(self, opponent):
       while self.is_alieve() and opponent.is_alieve():
           damage = self.attack()
           opponent.take_damage(damage)




class Ability:
    
    def __init__(self, name, attack_strength):
        self.name = name 
        self.attack_strength = attack_strength
    
    def attack(self):
        return random.randint(0, self.attack_strength)

class Weapon(Ability):
    def attack(self):
        
        return self.attack() / self.attack_strength


class Team:
    def __init__(self, team_name):
        self.name = name
        self.heroes = list()
    
    def add_hero(self, Hero):
        self.heroes.append(Hero)
    
    def remove_hero(self, name):
        self.heroes.remove(name)
    
    def view_all_heroes(self):

        for i in self.heroes:
            print(i)
    
    




if __name__ == '__main__':
    hero = Hero()
    print(hero.attack())
    ability = Ability()
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability()
    hero.add_ability(new_ability)
    print(hero.attack())


        