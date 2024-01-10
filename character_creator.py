import random
import name_generator
from util import race_bonuses
import races
from kenny import run_kennys_cheat_code_mode
from character import Character

# DICTIONARIES
character = Character()

# GLOBAL LISTS
custom_name = []

# GLOBAL VARIABLES
gen_name = name_generator.gen_name


def main():
    cc_intro()
    character_name()
    character_race()


def cc_intro():
    print()
    print('===========================================')
    print()
    print('Welcome to the 5e Helper Character Creator!')
    print('This feature will walk you through the steps of creating')
    print('a character and then output your character data on the screen.')
    print()
    print('===========================================')


def character_name():
    prompt = (
        '\nCharacter Name?\n'
        '1. Custom Name\n'
        '2. Name Generator\n\n'

        'CHOICE: '
    )

    name_choice = input(prompt)
    while name_choice not in ['1', '2', 'potato']:
        print('INVALID MENU CHOICE')
        name_choice = input(prompt)

    if name_choice == '1':
        name = input('What is your character\'s name?')
    elif name_choice == '2':
        name = name_generator.generate_name()
    elif name_choice == 'potato':
        run_kennys_cheat_code_mode()
        name = 'potato'

    character.set_name(name)


def character_race():
    print()
    print("You must now chose your character's race. You may view the Racial Bonuses chart before selecting\n"
          "your character's race or proceed right to race selection.\n")

    prompt = (
        '1. View Racial Bonuses\n'
        '2. Select Character Race'
        ''
        '\n\nCHOICE: '
    )
    menu_choice = input(prompt)
    while menu_choice not in [str(n) for n in range(1, 16)]:
        print('INCORRECT SELECTION. PLEASE TRY AGAIN.')
        menu_choice = input(prompt)

    if menu_choice == '1':
        race_bonuses()
    elif menu_choice == '1' or '2':
        # If user input is 1, it will display the racial bonuses menu but not proceed to the
        # race selection. The desired function is to proceed right to race selection after the racial bonuses
        # menu is displayed.
        print()
        print('1. Dwarf (Hill)     | 2. Dwarf (Mountain) | 3. Elf (High)\n'
              '4. Elf (Wood)       | 5. Elf (Drow)       | 6. Halfling (Lightfoot)\n'
              '7. Halfling (Stout) | 8. Human            | 9. Human (Variant)\n'
              '10. Dragonborn      | 11. Gnome (Forest)  | 12. Gnome (Rock)\n'
              '13. Half-Elf        | 14. Half-Orc        | 15. Tiefling')
        print()
        race_choice = input('Enter the number of your character\'s race: ')
        if race_choice == '1':
            character.set_attributes(races.d_hill)
        elif race_choice == '2':
            character.set_attributes(races.d_mountain)
            print(character.__dict__)
        elif race_choice == '3':
            character.set_race(races.high_e.name)
            character.set_str(races.high_e.scores[0])
            character.set_dex(races.high_e.scores[1])
            character.set_con(races.high_e.scores[2])
            character.set_inte(races.high_e.scores[3])
            character.set_wis(races.high_e.scores[4])
            character.set_cha(races.high_e.scores[5])
            character.set_vision(races.high_e.vision)
            character.set_size(races.high_e.size)
            character.set_languages(races.high_e.languages)
            character.set_speed(races.high_e.speed)
            character.set_r_traits(races.high_e.r_traits)
            character.set_subr_traits(races.high_e.subr_traits)
            character.set_combat_prof(races.high_e.combat_prof)
            character.set_tool_prof(races.high_e.tool_prof)
        elif race_choice == '4':
            character.set_race(races.wood_e.name)
            character.set_str(races.wood_e.scores[0])
            character.set_dex(races.wood_e.scores[1])
            character.set_con(races.wood_e.scores[2])
            character.set_inte(races.wood_e.scores[3])
            character.set_wis(races.wood_e.scores[4])
            character.set_cha(races.wood_e.scores[5])
            character.set_vision(races.wood_e.vision)
            character.set_size(races.wood_e.size)
            character.set_languages(races.wood_e.languages)
            character.set_speed(races.wood_e.speed)
            character.set_r_traits(races.wood_e.r_traits)
            character.set_subr_traits(races.wood_e.subr_traits)
            character.set_combat_prof(races.wood_e.combat_prof)
            character.set_tool_prof(races.wood_e.tool_prof)
        elif race_choice == '5':
            character.set_race(races.drow_e.name)
            character.set_str(races.drow_e.scores[0])
            character.set_dex(races.drow_e.scores[1])
            character.set_con(races.drow_e.scores[2])
            character.set_inte(races.drow_e.scores[3])
            character.set_wis(races.drow_e.scores[4])
            character.set_cha(races.drow_e.scores[5])
            character.set_vision(races.drow_e.vision)
            character.set_size(races.drow_e.size)
            character.set_languages(races.drow_e.languages)
            character.set_speed(races.drow_e.speed)
            character.set_r_traits(races.drow_e.r_traits)
            character.set_subr_traits(races.drow_e.subr_traits)
            character.set_combat_prof(races.drow_e.combat_prof)
            character.set_tool_prof(races.drow_e.tool_prof)
        elif race_choice == '6':
            character.set_race(races.lightfoot_half.name)
            character.set_str(races.lightfoot_half.scores[0])
            character.set_dex(races.lightfoot_half.scores[1])
            character.set_con(races.lightfoot_half.scores[2])
            character.set_inte(races.lightfoot_half.scores[3])
            character.set_wis(races.lightfoot_half.scores[4])
            character.set_cha(races.lightfoot_half.scores[5])
            character.set_vision(races.lightfoot_half.vision)
            character.set_size(races.lightfoot_half.size)
            character.set_languages(races.lightfoot_half.languages)
            character.set_speed(races.lightfoot_half.speed)
            character.set_r_traits(races.lightfoot_half.r_traits)
            character.set_subr_traits(races.lightfoot_half.subr_traits)
            character.set_combat_prof(races.lightfoot_half.combat_prof)
            character.set_tool_prof(races.lightfoot_half.tool_prof)
        elif race_choice == '7':
            character.set_race(races.stout_half.name)
            character.set_str(races.stout_half.scores[0])
            character.set_dex(races.stout_half.scores[1])
            character.set_con(races.stout_half.scores[2])
            character.set_inte(races.stout_half.scores[3])
            character.set_wis(races.stout_half.scores[4])
            character.set_cha(races.stout_half.scores[5])
            character.set_vision(races.stout_half.vision)
            character.set_size(races.stout_half.size)
            character.set_languages(races.stout_half.languages)
            character.set_speed(races.stout_half.speed)
            character.set_r_traits(races.stout_half.r_traits)
            character.set_subr_traits(races.stout_half.subr_traits)
            character.set_combat_prof(races.stout_half.combat_prof)
            character.set_tool_prof(races.stout_half.tool_prof)
        elif race_choice == '8':
            character.set_race(races.human.name)
            character.set_str(races.human.scores[0])
            character.set_dex(races.human.scores[1])
            character.set_con(races.human.scores[2])
            character.set_inte(races.human.scores[3])
            character.set_wis(races.human.scores[4])
            character.set_cha(races.human.scores[5])
            character.set_vision(races.human.vision)
            character.set_size(races.human.size)
            character.set_languages(races.human.languages)
            character.set_speed(races.human.speed)
            character.set_r_traits(races.human.r_traits)
            character.set_subr_traits(races.human.subr_traits)
            character.set_combat_prof(races.human.combat_prof)
            character.set_tool_prof(races.human.tool_prof)
        elif race_choice == '9':
            character.update({'Race': standard_races['human_variant']})
        elif race_choice == '10':
            character.update({'Race': standard_races['dragonborn']})
        elif race_choice == '11':
            character.update({'Race': standard_races['gnome_forest']})
        elif race_choice == '12':
            character.update({'Race': standard_races['gnome_rock']})
        elif race_choice == '13':
            character.update({'Race': standard_races['half_elf']})
        elif race_choice == '14':
            character.update({'Race': standard_races['half_orc']})
        elif race_choice == '15':
            character.update({'Race': standard_races['tiefling']})


main()