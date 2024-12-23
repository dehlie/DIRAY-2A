class character:
    def __init__(self, name, role):
        self.name = name
        self.role = role


hero = character("Ling", "Assasin")
hero2 = character("Akai", "Tank")

print(hero.name, hero.role, hero2.name, hero2.role)