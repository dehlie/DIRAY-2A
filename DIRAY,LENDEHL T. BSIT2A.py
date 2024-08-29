class hero(): 
    def __init__(self, name, role, dmg_type, health, auto_atk_dmg):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.health = health
        self.auto_atk_dmg = auto_atk_dmg
   
    def describe(self):
        return f"{self.name} is a {self.role} with a damage type of {self.dmg_type} power"
    
hero_mm1 = hero("layla", "marksman", "attack damage","100","30")
hero_fighter2 = hero ("argus", "fighter", "attack damage","150","20")
hero_mage3 = hero ("cyclops", "mage", "attack damage", "80","10")
hero_jungler4 = hero ("karina", "assasin", "jungler","90","30")
hero_support5 = hero ("estes", "healer", "healing","95","10")

print(f''' 
{hero_mm1.name}
{hero_mm1.role}
{hero_mm1.health} HP
{hero_mm1.auto_atk_dmg} basic attack damage 
{hero_mm1.dmg_type}
{hero_mm1.describe()}

{hero_fighter2.name}
{hero_fighter2.role}
{hero_fighter2.health} HP
{hero_fighter2.auto_atk_dmg} basic attack damage 
{hero_fighter2.dmg_type}
{hero_fighter2.describe()}

{hero_mage3.name}
{hero_mage3.role}
{hero_mage3.health} HP
{hero_mage3.auto_atk_dmg} basic attack damage 
{hero_mage3.dmg_type}
{hero_mage3.describe()}

{hero_jungler4.name}
{hero_jungler4.role}
{hero_jungler4.health} HP
{hero_jungler4.auto_atk_dmg} basic attack damage 
{hero_jungler4.dmg_type}
{hero_jungler4.describe()}

{hero_support5.name}
{hero_support5.role}
{hero_support5.health} HP
{hero_support5.auto_atk_dmg} basic attack damage 
{hero_support5.dmg_type}
{hero_support5.describe()}''')

