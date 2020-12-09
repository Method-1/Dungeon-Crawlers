class Characters:
    def __init__(self, name, character, initiative, endurance, attack, agility, special, wallet):
        self.name = name
        self.character = character
        self.initiative = initiative
        self.endurance = endurance
        self.attack = attack
        self.agility = agility
        self.special = special
        self.wallet = wallet

    def __repr__(self):
        return "{:<10}{:<14}{:<12}{:<10}{:<10}{:<8}{:<14}{:6}".format(self.name, self.character, self.initiative, self.endurance, self.attack, self.agility, self.special, self.wallet)


class Knight(Characters):
    def __init__(self, name, character, initiative, endurance, attack, agility, special, wallet):
        super().__init__(name, character, initiative, endurance, attack, agility, special, wallet)
        self.name = name


class Wizard(Characters):
    def __init__(self, name, character, initiative, endurance, attack, agility, special, wallet):
        super().__init__(name, character, initiative, endurance, attack, agility, special, wallet)
        self.name = name


class Thief(Characters):
    def __init__(self, name, character, initiative, endurance, attack, agility, special, wallet):
        super().__init__(name, character, initiative, endurance, attack, agility, special, wallet)
        self.name = name