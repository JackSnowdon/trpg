from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


# Create Black Magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 26, 680, "black")
blizzard = Spell("Blizzard", 20, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 20, 500, "white")
cura = Spell("Cura", 32, 1500, "white")

# Create Some Items
# Potions 
potion = Item("Potion", "potion", "Heals 250 HP", 250)
hipotion = Item("Hi-Potion", "potion", "Heals 1000 HP", 1000)
superpotion = Item("Super Potion", "potion", "Heals 5000 HP", 5000)

# Elixers
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
megaelixer = Item("Mega Elixer", "elixer", "Fully restores HP/MP of the Party", 9999)

# Attack Items 
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

# Spell/Item Lists
player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 2}, {"item": elixer, "quantity": 10},
                {"item": megaelixer, "quantity": 5}, {"item": grenade, "quantity": 10}]

# Instantiate People
player1 = Person("Valos:", 3460, 265, 180, 34, player_spells, player_items)
player2 = Person("Range:", 2460, 220, 140, 34, player_spells, player_items)
player3 = Person("Latho:", 8460, 290, 160, 34, player_spells, player_items)

enemy1 = Person("Imp  :", 1500, 130, 700, 325, [], [])
enemy2 = Person("Magus:", 18000, 120, 560, 25, [], [])
enemy3 = Person("Imp  :", 1500, 130, 700, 325, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

# Init Game
running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attacks!" + bcolors.ENDC)

while running:
# Choose Action
    print("==============================")
    
    print("\n\n")
    print("NAME                    HP:                                    MP:")
    for player in players:
        player.get_stats()
        
    print("\n")
    
    for enemy in enemies:
        enemy.get_enemy_stats()
        
    for player in players:
        
        player.choose_action()
        choice = input("    Choose action: ")
        index = int(choice) - 1
        
# Attack
        if index == 0:
            dmg = player.generate_dmg()
            enemy = player.choose_target(enemies)
            
            enemies[enemy].take_damage(dmg)
            print("You attacked " + enemies[enemy].name.replace(" ", "") + " for"  , dmg, 
            "points of damage.")
            
            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " has died.")
                del enemies[enemy]
# Magic
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic: ")) - 1
            
            if magic_choice == -1:
                continue
            
            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_spell_dmg()
            
            current_mp = player.get_mp()
            
            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue
            
            player.reduce_mp(spell.cost)
            
            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKGREEN + "\n" + spell.name + " heals for",
                str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
            
                enemies[enemy].take_damage(magic_dmg)
                
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg),
                "points of damage to " + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)
                
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]
# Items    
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1
            
            if item_choice == -1:
                continue
            
            item = player.items[item_choice]["item"]
            
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue
            
            player.items[item_choice]["quantity"] -= 1
            
            
            
            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for",
                str(item.prop), "HP", bcolors.ENDC)
            elif item.type == "elixer":
                
                if item.name =="MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                        
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP"
                + bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop),
                "points of damage to " + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)
                
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]
                
# Enemy Attack         
    enemy_choice = 1
    target = random.randrange(0, 3)
    enemy_dmg = enemies[0].generate_dmg()
    
    players[target].take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, 
    "points of damage.")

# Round Results    
    
    defeated_enemies = 0
    defeated_players = 0
    
    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1
    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1
    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif defeated_players == 2:
        print(bcolors.FAIL + "You have been defeated. Game Over." + bcolors.ENDC)
        running = False