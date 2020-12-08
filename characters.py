class Characters:
    def __init__(self, name, character, initiative, endurance, attack, agility, special):
        self.name = name
        self.character = character
        self.initiative = initiative
        self.endurance = endurance
        self.attack = attack
        self.agility = agility
        self.special = special

    def all_stats(self):
        allstats = {'Username': f'{self.name}', 'Class': f'{self.character}', 'Initiative': f'{self.initiative}', 'Endurance': f'{self.endurance}',
            'Attack': f'{self.attack}', 'Agility': f'{self.agility}', 'Special': f'{self.special}'}
        return allstats


class Knight(Characters):
    def __init__(self, name):
        super().__init__(name, 'Knight', 5, 9, 6, 4, "Shield Block")

class Wizard(Characters):
    def __init__(self, name):
        super().__init__(name, 'Wizard', 6, 4, 9, 5, "Blinding Light")

class Thief(Characters):
    def __init__(self, name):
        super().__init__(name, 'Thief', 7, 5, 5, 7, 'Critical Hit')

name = input("Username: ")
test_character = Knight(name)
print(test_character.all_stats())
