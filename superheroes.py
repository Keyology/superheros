import random


class Hero:
    def __init__(self, name, starting_health =100):
         
        self.name = name 
        self.abilities = list()
        self.kills = 0
        self.starting_health = starting_health 
        self.current_health = starting_health 
            
    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def attack(self):
        # if there are no abilities, return 0
        total_damage = 0

        if len(self.abilities) <= 0:
            return 0

        for ability in self.abilities:
            total_damage += ability.attack()

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
        print('{} will be fighting {}'.format(self.name, opponent))
        while self.is_alieve() == True and opponent.is_alieve() == True:
           self.take_damage(opponent.attack()) 
           opponent.take_damage(self.attack())
           if opponent.is_alive() == False:
               self.deaths += 1
        print('the fight continues')
       




class Ability:
    
    def __init__(self, name, max_damage):
        self.name = name 
        self.max_damage = max_damage
    
    def attack(self):
        max_attack = self.max_damage
        min_attack = max_attack = 0
        return random.randint(min_attack, self.max_damage)

class Weapon(Ability):

    def attack(self):
        """
        This method should should return a random value
        between one half to the full attack power of the weapon.
        
        1. max_attack = get the full attack power of the weapon
            Hint: The attack power is inherited.
        2. min_attack = divide the full power by 2
        3. get random num between min & max
        4. return that value
        """
        max_attack = self.max_damage
        min_attack = max_attack // 2
        ran_num = random.randint(min_attack, max_attack)
        print('******** Random Num: {}'.format(ran_num))
        return ran_num
        



class Team:
    def __init__(self, team_name):
        '''Instantiate resources.'''
        self.name = team_name
        self.heroes = list()
    
    def add_hero(self, Hero):
        '''Add Hero object to heroes list.'''
        self.heroes.append(Hero)
    
    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.pop(hero)
            else:
                return 0
                
    
        
    
    def view_all_heroes(self):
        '''Print out all heroes to the console.'''
        print('INSIDE the FUNCTION ************')
        if (self.heroes <= 0):
            print('HERE')
        else:
            print('ELSE BLOCK')
            for hero in self.heroes:
                print('********* FOR LOOP')
                print(hero.name)

    




if __name__ == '__main__':
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 20)
    hero.add_ability("flying")
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 30)
    hero.add_ability(new_ability)
    print(hero.attack())
    hero2 = Hero("Jodie Foster")
    ability2 = Ability("Science", 800)
    hero2.add_ability(ability2)
    hero.fight(hero2)
    

        