import random
import name_generator
from util import race_bonuses, display_menu_options
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

        # TODO: Move race info to the races themselves
        #       Try to use a dict comprehension to create this dict automatically
        race_options = {
            '1': {
                'label': 'Dwarf (Hill)',
                'race': races.d_hill
            },
            '2': {
                'label': 'Dwarf (Mountain)',
                'race': races.d_mountain
            },
            '3': {
                'label': 'Elf (High)',
                'race': races.high_e
            },
            '4': {
                'label': 'Elf (Wood)',
                'race': races.wood_e
            },
            '5': {
                'label': 'Elf (Drow)',
                'race': races.drow_e
            },
            '6': {
                'label': 'Halfling (Lightfoot)',
                'race': races.half
            },
            '7': {
                'label': 'Halfling (Stout)',
                'race': races.stout_half
            },
            '8': {
                'label': 'Human',
                'race': races.human
            },
            '9': {  # TODO
                'label': 'Human (Variant)',
                'race': None
            },
            '10': {  # TODO
                'label': 'Dragonborn',
                'race': None
            },
            '11': {  # TODO
                'label': 'Gnome (Forest)',
                'race': None
            },
            '12': {  # TODO
                'label': 'Gnome (Rock)',
                'race': None
            },
            '13': {  # TODO
                'label': 'Half-Elf',
                'race': None
            },
            '14': {  # TODO
                'label': 'Half-Orc',
                'race': None
            },
            '15': {  # TODO
                'label': 'Tiefling',
                'race': None
            },
        }

        display_options = [
            f'{key}. {info["label"]}'
            for key, info in race_options.items()
        ]
        display_menu_options(display_options, per_line=3)

        race_choice = input('Enter the number of your character\'s race: ')
        if race_choice in race_options:
            character.set_attributes(race_options[race_choice]['race'])

        print(character.__dict__)

main()