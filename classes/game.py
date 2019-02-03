import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD  = '\033[1m'
    UNDERLINE = '\033[4m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

class Person:
    def __init__(self, hp, mp, atk, df, mag):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.magic = mag
        self.actions =["Attack", "Magic"]
        
    def generate_dmg(self):
        return random.randrange(self.atkl, self.atkh)
    
    def generate_spell_dmg(self, i):
        ngl = self.magic[i]["dmg"] - 5
        ngh = self.magic[i]["dmg"] + 5
        return random.randrange(ngl, ngh)
        
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
        
    def get_hp(self):
        return self.hp
    
    def get__max_hp(self):
        return self.maxhp
        
    def get_mp(self):
        return self.mp
        
    def get__max_mp(self):
        return self.maxmp
        
    def reduce_mp(self, cost):
        self.mp -= cost
        
    def get_spell_name(self, i):
        return self.magic[i]["name"]
        
    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]
        
    def choose_action(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1
            
    def choose_magic(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(i) + ":", spell["name"], "(cost:", str(spell["mp"]) + ")")
            i += 1
            
            
    