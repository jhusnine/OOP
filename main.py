class heroes:
    def __init__(self, name, role ,damage_type):
        self.name = name
        self.role = role
        self.damage_type = damage_type
        
    def describe(self):
        print(f"{self.name} is a {self.role} hero with {self.damage_type} damage. ")
        
    def __str__(self):
        return f"{self.name} is a {self.role} hero with {self.damage_type} damage. "
        
mm = heroes("Granger","marksman/assassin", "jungler")
fighter = heroes("Alucard", "fighter", "physical")
mage = heroes("Lylia","mage", "magic")
tank = heroes("Edith", "tank/marksman", "physical")
support = heroes("Estes", "support", "magic")

mm.describe()
fighter.describe()
mage.describe()
tank.describe()  
support.describe()
