import random

def verifyInt(K):
    if not K.isnumeric():
        return verifyInt(input("Invalid Input, Please enter an integer: "))
    return int(K)

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = int(starting_health)
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total = 0
        for x in range(len(self.abilities)):
            total += self.abilities[x].attack()
        return total

    def defend(self):
        total = 0
        if self.current_health == 0:
            self.deaths += 1
            return total
        for x in self.armors:
            total += x.block()
        return total

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_armor(self, armor):
        self.armors.append(armor)

   
    
    def take_damage(self, damage):
        self.current_health -= damage - self.defend()

    
    def is_alive(self):
        if int(self.current_health) > 0:
            return True
        elif int(self.current_health) <= 0:
            self.current_health = 0
            return False
     
    def add_kill(self, num_kills):
        self.kills += num_kills

    def fight(self, opponent):
        print('{} will be fighting {}'.format(self.name, opponent))
        while(self.is_alive() == True  and opponent.is_alive() == True):
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
        if not self.is_alive():
            opponent.add_kill(1)
            print(self.name + " died")
            self.deaths += 1
            return self
        elif not opponent.is_alive():
            self.add_kill(1)
            print(opponent.name + " died")
            opponent.deaths += 1
            return opponent
        print("the fight continues")



class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        max_attack = self.max_damage
        min_attack = max_attack = 0
        return random.randint(min_attack, max_attack)



class Weapon(Ability):
    def attack(self):

        max_wepon_damage  = int(self.max_damage)
        min_weapon_damage = int(self.max_damage) //2
        ran_num = random.randint( min_weapon_damage, max_wepon_damage )
        print('******** Random Num: {}'.format(ran_num))
        return ran_num
        
        return random.randint(int(self.max_damage)/2, int(self.max_damage))



class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def healthCheck(self):
        health_total = 0
        for i in self.heroes:
            health_total += i.current_health
        return health_total

    def add_hero(self, Hero):
        self.heroes.append(Hero)
        print("*** this is hero list:", self.heroes)

    def remove_hero(self, name):
        removed = False
        for a_hero in range(len(self.heroes)-1):
            print("*** this is hero list:", a_hero)
            if self.heroes[a_hero].name == name:
                print("This is self.heros:", self.heroes)
                self.heroes.pop(a_hero)
                removed == True
        if not removed:
        
            return 0

    def attack(self, other_team):
         while self.healthCheck() and other_team.healthCheck():
            self.remove_hero(self.heroes[random.randint(0, len(self.heroes)-1)].fight(other_team.heroes[random.randint(0, len(other_team.heroes)-1)]).name)
    def revive_heroes(self):
        for i in self.heroes:
            i.current_health = i.starting_health

    def stats(self):
        total_deaths = 0
        total_kills = 0
        for i in self.heroes:
            total_deaths += i.deaths
            total_kills += i.kills
        if(self.healthCheck() <= 0):
            print ("{}: {}".format(self.name, (total_kills/total_deaths)))
        else:
            print ("{}: {}".format(self.name, float(total_kills)))

    def view_all_heroes(self):
        print(self.heroes)



class Armor:
    def __init__(self, name, max_block):
        '''Instantiate name and defense strength.'''
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, int(self.max_block))


class Arena:
    def __init__(self):
        '''
        Declare variables
        '''
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("Create a name for this hero's ability: ")
        damage = verifyInt(input("What is the maximum damage for this ability: "))
        ability = Ability(name, damage)
        return ability

    def create_weapon(self):
        name = input("Create a name for this hero's weapon: ")
        damage = verifyInt(input("What is the maximum damage for this weapon: "))
        weapon = Weapon(name, damage)
        return weapon

    def create_armor(self):
        name = input("Create a name for this armor piece: ")
        block = verifyInt(input("What is this armor's power: "))
        armor = Armor(name, block)
        return armor

    def create_hero(self):
        name = input("What is this hero's name: ")
        health = verifyInt(input("How much health does this hero have: "))
        hero = Hero(name, health)
        abilities = verifyInt(input("How many abilities does this hero have: "))
        weapon = verifyInt(input("How many weapons does this hero have: "))
        armor = verifyInt(input("How many armors does this hero have: "))

        for x in range(abilities):
            hero.add_ability(self.create_ability())

        for y in range(weapon):
            hero.add_weapon(self.create_weapon())

        for z in range(armor):
            hero.add_armor(self.create_armor())

        return hero

    def build_team_one(self):
    
        name = input("Choose a name for this team: ")
    
        self.team_one = Team(name)
        heroes = verifyInt(input("How many heroes on this team: "))

        for x in range(heroes):
            self.team_one.add_hero(self.create_hero())

    def build_team_two(self):
        name = input("Choose a name for this team: ")
        self.team_two = Team(name)
        heroes = verifyInt(input("How many heroes on this team: "))

        for x in range(heroes):
            self.team_two.add_hero(self.create_hero())

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        if self.team_one.healthCheck() < 1:
            print(self.team_two.name + " Wins")
            print("Surviving Heroes:")
            for x in self.team_two.heroes:
                if x.current_health > 0:
                    print(x.name)
        elif self.team_two.healthCheck() < 1:
            print(self.team_one.name + " Wins")
            print("Surviving Heroes:")
            for x in self.team_one.heroes:
                if x.current_health > 0:
                    print(x.name)
        print("Team Kill/Death Ratios:")
        self.team_one.stats()
        self.team_two.stats()

if __name__ == "__main__":
    game_is_running = True
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input(" Would you like to Play Again? Y or N: ")

        if play_again.lower() == "n":
            game_is_running = False
        elif play_again.lower() == "y":
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
        else:
            print("Invalid Input, terminating")
            game_is_running = False