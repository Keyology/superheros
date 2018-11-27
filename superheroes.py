import random


class Hero:
    def __init__(self, name, starting_health =100):
        self.name = name 
        self.abilities = list()
        self.kills = 0
        self.starting_health = starting_health 
        self.current_health = starting_health 
    
    def add_ability(self, ability):
        self.abilities.append(self.ability)
    
    def attack(self):
        total_damage = 0
        for i in self.abilities:
            total_damage = i.attack()
            return total_damage
            
    
    def take_damage(self):
        self.current_health -= self.total_damage
    
    def is_alieve(self):
        if self.current_health >= 0:
            return True
            print('hero is alieve')
        else:
            return False
            print('hero is dead')
    
    def add_kill(self, num_kills):
        self.kills += num_kills

    
    def fight(self, opponent):
        print('{} will be fighting {}'.format(self.name, self.opponent))
        while self.is_alieve() == True and opponent.is_alieve() == True:
           self.take_damage(opponent.attack()) 
           opponent.take_damage(self.attack())
           if opponent.is_alive() == False:
               self.kill += 1
        print('the fight continues')
       




class Ability:
    
    def __init__(self, name, max_damage):
        self.name = name 
        self.max_damage = max_damage
    
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


        