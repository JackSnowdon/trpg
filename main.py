from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item


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
enemy = Person("Magus:", 11200, 120, 560, 25, [], [])

players = [player1, player2, player3]

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
    
    enemy.get_enemy_stats()
        
    for player in players:
        
        player.choose_action()
        choice = input("    Choose action: ")
        index = int(choice) - 1
        
# Attack
        if index == 0:
            dmg = player.generate_dmg()
            enemy.take_damage(dmg)
            print("You attacked for", dmg, 
            "points of damage.")
            
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
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg),
                "points of damage" + bcolors.ENDC)
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
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP"
                + bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop),
                "points of damage" + bcolors.ENDC)
                
# Enemy Attack         
    enemy_choice = 1
    
    enemy_dmg = enemy.generate_dmg()
    player1.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, 
    "points of damage.")

# Round Results    
    print("-----------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/"
    + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You have been defeated. Game Over." + bcolors.ENDC)
        running = False