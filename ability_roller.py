import random


def ability_scores():
    pre_scores = []
    scores = []
    scores.clear()
    pre_scores.clear()
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

    print()
    print('1. Dwarf (Hill) 2. Dwarf (Mountain) 3. Elf (High)\n'
          '4. Elf (Wood) 5. Elf (Drow) 6. Halfling (Lightfoot)\n' 
          '7. Halfling (Stout) 8. Human 9. Human (Variant)\n' 
          '10. Dragonborn 11. Gnome (Forest) 12. Gnome (Rock)\n'
          '13. Half-Elf 14. Half-Orc 15. Tiefling')
    print()
    race_selection = input('Enter the number of your character\'s race: ')
    print()

    while len(scores) < 6:
        pre_scores.append(random.randint(1, 6))
        if len(pre_scores) == 4:
            # print(pre_scores) DEBUG
            pre_scores.sort()
            pre_scores.reverse()
            pre_scores.pop()
            # print(pre_scores) DEBUG
            pre_sum = sum(pre_scores)
            scores.append(pre_sum)
            pre_scores.clear()

    print('Your ability scores are', *scores, sep=' ')
    print('and your race bonuses are:')
    print()
    if race_selection == '1':
        print('STR +', dwarf_hill[0], 'DEX +', dwarf_hill[1], 'CON +', dwarf_hill[2], 'INT +', dwarf_hill[3], 'WIS +',
              dwarf_hill[4], 'CHA +', dwarf_hill[5])
        print()
    elif race_selection == '2':
        print('STR +', dwarf_mountain[0], 'DEX +', dwarf_mountain[1], 'CON +', dwarf_mountain[2], 'INT +',
              dwarf_mountain[3], 'WIS +', dwarf_mountain[4], 'CHA +', dwarf_mountain[5])
        print()
    elif race_selection == '3':
        print('STR +', elf_high[0], 'DEX +', elf_high[1], 'CON +', elf_high[2], 'INT +', elf_high[3], 'WIS +',
              elf_high[4], 'CHA +', elf_high[5])
        print()
    elif race_selection == '4':
        print('STR +', elf_wood[0], 'DEX +', elf_wood[1], 'CON +', elf_wood[2], 'INT +', elf_wood[3], 'WIS +',
              elf_wood[4], 'CHA +', elf_wood[5])
        print()
    elif race_selection == '5':
        print('STR +', elf_drow[0], 'DEX +', elf_drow[1], 'CON +', elf_drow[2], 'INT +', elf_drow[3], 'WIS +',
              elf_drow[4], 'CHA +', elf_drow[5])
        print()
    elif race_selection == '6':
        print('STR +', halfling_lightfoot[0], 'DEX +', halfling_lightfoot[1], 'CON +', halfling_lightfoot[2], 'INT +',
              halfling_lightfoot[3], 'WIS +', halfling_lightfoot[4], 'CHA +', halfling_lightfoot[5])
        print()
    elif race_selection == '7':
        print('STR +', halfling_stout[0], 'DEX +', halfling_stout[1], 'CON +', halfling_stout[2], 'INT +',
              halfling_stout[3], 'WIS +', halfling_stout[4], 'CHA +', halfling_stout[5])
        print()
    elif race_selection == '8':
        print('STR +', human[0], 'DEX +', human[1], 'CON +', human[2], 'INT +', human[3], 'WIS +', human[4], 'CHA +',
              human[5])
        print()
    elif race_selection == '9':
        print('STR +', human[0], 'DEX +', human[1], 'CON +', human[2], 'INT +', human[3], 'WIS +', human[4], 'CHA +',
              human[5])
        print('Add +1 to any two ability scores.')
        print()
    elif race_selection == '10':
        print('STR +', dragonborn[0], 'DEX +', dragonborn[1], 'CON +', dragonborn[2], 'INT +', dragonborn[3],
              'WIS +', dragonborn[4], 'CHA +', dragonborn[5])
        print()
    elif race_selection == '11':
        print('STR +', gnome_forest[0], 'DEX +', gnome_forest[1], 'CON +', gnome_forest[2], 'INT +', gnome_forest[3],
              'WIS +',gnome_forest[4], 'CHA +', gnome_forest[5])
        print()
    elif race_selection == '12':
        print('STR +', gnome_rock[0], 'DEX +', gnome_rock[1], 'CON +', gnome_rock[2], 'INT +', gnome_rock[3],
              'WIS +', gnome_rock[4], 'CHA +', gnome_rock[5])
        print()
    elif race_selection == '13':
        print('STR +', half_elf[0], 'DEX +', half_elf[1], 'CON +', half_elf[2], 'INT +', half_elf[3], 'WIS +',
              half_elf[4], 'CHA +', half_elf[5])
        print('Add +1 to any two ability scores.')
        print()
    elif race_selection == '14':
        print('STR +', half_orc[0], 'DEX +', half_orc[1], 'CON +', half_orc[2], 'INT +', half_orc[3], 'WIS +',
              half_orc[4], 'CHA +', half_orc[5])
        print()
    elif race_selection == '15':
        print('STR +', tiefling[0], 'DEX +', tiefling[1], 'CON +', tiefling[2], 'INT +', tiefling[3], 'WIS +',
              tiefling[4], 'CHA +', tiefling[5])
        print()
    else:
        incorrect_race = race_selection
        print('INVALID RACE SELECTION')
        print()
