import random


def intro():
    print()
    print('==================================')
    print()
    print('Welcome to the D&D 5e Helper Lite!')
    print()
    print('==================================')
    print()


def race_bonuses():
    print()
    print('RACE                 | STR | DEX | CON | INT | WIS | CHA |')
    print('----------------------------------------------------------')
    print('Dwarf (Hill)         |     |     |  +2 |     |  +1 |     |')
    print('Dwarf (Mountain      |  +2 |     |  +2 |     |     |     |')
    print('Elf (High)           |     |  +2 |     |  +1 |     |     |')
    print('Elf (Wood)           |     |  +2 |     |     |  +1 |     |')
    print('Elf (Drow)           |     |  +2 |     |     |     |  +1 |')
    print('Halfling (Lightfoot) |     |  +2 |     |     |     |  +1 |')
    print('Halfling (Stout)     |     |  +2 |  +1 |     |     |     |')
    print('Human                |  +1 |  +1 |  +1 |  +1 |  +1 |  +1 | (Human Variant +1 to any two)')
    print('Dragonborn           |  +2 |     |     |     |     |  +1 |')
    print('Gnome (Forest)       |     |  +1 |     |  +2 |     |     |')
    print('Gnome (Rock)         |     |     |  +1 |  +2 |     |     |')
    print('Half-Elf (+1 Any 2)  |     |     |     |     |     |  +2 |')
    print('Half-Orc             |  +2 |     |  +1 |     |     |     |')
    print('Tiefling             |     |     |     |  +1 |     |  +2 |')
    return


def ability_races():
    dwarf_hill = [0, 0, 2, 0, 1, 0]
    dwarf_mountain = [2, 0, 2, 0, 0, 0]
    elf_high = [0, 2, 0, 1, 0, 0]
    elf_wood = [0, 2, 0, 0, 1, 0]
    elf_drow = [0, 2, 0, 0, 0, 1]
    halfling_lightfoot = [0, 2, 0, 0, 0, 1]
    halfling_stout = [0, 2, 1, 0, 0, 0]
    human = [1, 1, 1, 1, 1, 1]
    dragonborn = [2, 0, 0, 0, 0, 1]
    gnome_forest = [0, 1, 0, 2, 0, 0]
    gnome_rock = [0, 0, 1, 2, 0, 0]
    half_elf = [0, 0, 0, 0, 0, 2]
    half_orc = [2, 0, 1, 0, 0, 0]
    tiefling = [0, 0, 0, 1, 0, 2]

    return


def end():
    print()
    print('===========================================')
    print()
    print('Thank you for using the D&D 5e Helper Lite!')
    print('Happy adventuring!')
    print()
    print('===========================================')
    print()
    exit()
    
