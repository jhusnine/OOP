class hero:
    def __init__(self, name, role, dmg_type, health, auto_atk_dmg):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.health = health
        self.auto_atk_dmg = auto_atk_dmg

    def describe(self):
        return f"{self.name} is a {self.role} with a {self.dmg_type} power"


hero_mm1 = hero("granger", "marksman", "physical damage/jungler", 2260,116)
hero_fighter1 = hero("alucard", "fighter", "physical_damage", 2621, 123)
hero_mage1 = hero("lylia", "mage", "magic_damage", 2501, 113)
hero_fighter2 = hero("silvana", "fighter", "magic_damage", 2828, 126)
hero_mage2 = hero("kagura", "mage", "magic_damage", 2496, 118)

print(f'''
{hero_mm1.name}
{hero_mm1.role}
{hero_mm1.health} HP
{hero_mm1.auto_atk_dmg} basic attack damage
{hero_mm1.dmg_type}
{hero_mm1.describe()}
    
{hero_fighter1.name}
{hero_fighter1.role}
{hero_fighter1.health} HP
{hero_fighter1.auto_atk_dmg} basic attack damage
{hero_fighter1.dmg_type}
{hero_fighter1.describe()}

{hero_mage1.name}
{hero_mage1.role}
{hero_mage1.health} HP
{hero_mage1.auto_atk_dmg} basic attack damage
{hero_mage1.dmg_type}
{hero_mage1.describe()}

{hero_fighter2.name}
{hero_fighter2.role}
{hero_fighter2.health} HP
{hero_fighter2.auto_atk_dmg} basic attack damage
{hero_fighter2.dmg_type}
{hero_fighter2.describe()}

{hero_mage2.name}
{hero_mage2.role}
{hero_mage2.health} HP
{hero_mage2.auto_atk_dmg} basic attack damage
{hero_mage2.dmg_type}
{hero_mage2.describe()}

''')
