class Characters:
    def __init__(self, character, initiative, endurance, attack, agility, special):
        self.character = character
        self.initiative = initiative
        self.endurance = endurance
        self.attack = attack
        self.agility = agility
        self.special = special
        self.allstats = {'Class': f'{character}', 'Initiative': f'{initiative}', 'Endurance': f'{endurance}',
            'Attack': f'{attack}', 'Agility': f'{agility}', 'Special': f'{special}'}

class Knight(Characters):
    def __init__(self):
        super().__init__('Knight', 5, 9, 6, 4, "Shield Block")

class Wizard(Characters):
    def __init__(self):
        super().__init__('Wizard', 6, 4, 9, 5, "Blinding Light")

class Thief(Characters):
    def __init__(self):
        super().__init__('Thief', 7, 5, 5, 7, 'Critical Hit')


test_character = Knight()
print(test_character.allstats)
