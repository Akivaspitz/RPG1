from game import Player, bcolors
import random

magic = [{"Name": "Fireball","Cost": 25, "Damage": 30},
         {"Name": "Lightning Bolt ", "Cost": 25, "Damage": 28},
         {"Name": "Ray Of Frost", "Cost": 5, "Damage": 4}]
player = Player(460, 100, 30, 30, magic)

print(player.atk_damage())
print("********")
player.choose_action()
player.choose_magic()
print("********")

print(player.magic_damage(1))
print(player.magic_damage(2))
print(player.magic_damage(0))
print("********")
print(player.magic_damage(1))
