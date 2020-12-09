class Characters:
    def __init__(self, name, character, initiative, endurance, attack, agility, special, money):
        self.name = name
        self.character = character
        self.initiative = initiative
        self.endurance = endurance
        self.attack = attack
        self.agility = agility
        self.special = special
        self.money = money

    def all_stats(self):  # Maybe create a function that allows others to print out all the parent attributes as a dict instead of making a dict like you did here??
        allstats = {'Username': f'{self.name}', 'Class': f'{self.character}', 'Initiative': f'{self.initiative}', 'Endurance': f'{self.endurance}',
            'Attack': f'{self.attack}', 'Agility': f'{self.agility}', 'Special': f'{self.special}', 'Wallet': f'{self.money}'}
        return allstats

class handle_functions(Characters):  # Class that allows you to handle functions/methods that exist in parentclass
    def __init__(self):
        pass

class Knight(Characters):
    def __init__(self, name):
        super().__init__(name, 'Knight', 5, 9, 6, 4, "Shield Block", {'Wallet': 0})

class Wizard(Characters):
    def __init__(self, name):
        super().__init__(name, 'Wizard', 6, 4, 9, 5, "Blinding Light", {'Wallet': 0})

class Thief(Characters):
    def __init__(self, name):
        super().__init__(name, 'Thief', 7, 5, 5, 7, 'Critical Hit', {'Wallet': 0})


#x = Knight("adi").all_stats()
#y = Wizard("Bajs").all_stats()
#lista = [x, y]
#print(lista)
name = input("Username: ")
test_character = Knight(name)
attr_value = test_character.__dict__
print(attr_value)
print(attr_value['money']['Wallet'] + 2)
#test_character.money['Wallet'] = 0 + 2

#vars(test_character.all_stats())
#print(test_character.all_stats())