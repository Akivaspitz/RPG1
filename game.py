import random

class bcolors:
    HEADER='\033[95m'
    OKBLUE='\033[94m'
    OKGREEN='\033[92m'
    WARNING='\033[93m'
    FAIL='\033[91m'
    ENDC='\033[0m'
    BOLD='\033[1m'
    UNDERLINE='\033[4m'

class Player:

    def __init__(self, hp, mp, atk, defence, magic):
        self.max_hp = hp
        self.current_hp = hp
        self.max_mp = mp
        self.current_mp = mp
        self.atk_high = atk + 10
        self.atk_low = atk - 10
        self.defence = defence
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def atk_damage(self):
        return random.randrange(self.atk_low, self.atk_high)

    def magic_damage(self, i):
        max_dmg = self.magic[i]["Damage"] + 10
        min_dmg = self.magic[i]["Damage"] - 10
        return random.randrange(min_dmg, max_dmg)

    def self_dmg(self, dmg):
        hp = self.current_hp - dmg
        if hp < 0:
            hp = 0
        return hp

    def get_hp(self):
        return self.current_hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.current_mp

    def get_max_mp(self):
        return self.max_mp

    def get_def(self):
        return self.defence

    def reduce_mp(self, cost):
        self.current_mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]["Name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["Cost"]

    def choose_action(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("Magic Spells")
        for spell in self.magic:
            print(str(i) + ":", spell["Name"], "(cost:", str(spell["Cost"]) + ")")
            i += 1

