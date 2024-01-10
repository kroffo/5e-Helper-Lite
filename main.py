import util
import dice_roller as dice
import character_creator as cc
import name_generator
import ability_roller


def main():
    #util.intro()
    display_menu()


def display_menu():
    """
    Display the menu options and execute the requested action
    repeatedly until the user enters the exit command.
    """
    menu = (
           'MENU\n'
           '------------------------\n'
           '1. Dice Roller\n'
           '2. View Racial Bonuses\n'
           '3. Name Generator\n'
           '4. Ability Score Roller\n'
           '5. Character Creator\n'
           '6. Quit Program\n'
           '\n'
    )
    print(menu)

    prompt = 'Enter the number of the program you would like to use: '
    menu_choice = input(prompt)
    while menu_choice != '6':
        if menu_choice == '1':
            run_dice_roller()
        elif menu_choice == '2':
            view_racial_bonuses()
        elif menu_choice == '3':
            run_name_generator()
        elif menu_choice == '4':
            run_ability_score_roller()
        elif menu_choice == '5':
            warn_not_implemented('Character Creator')
        else:
            print('INVALID INPUT\n')

        print('\n===========================================\n')
        menu_choice = input(prompt)

    exit_program()


def warn_not_implemented(feature_name):
    """
    Print a generic feature-not-implemented message
    for a given feature
    """
    print(
        f'\nThank you for your interest in the {feature_name}.\n'
        'Unfortunately this feature has not yet been implemented\n'
        '\n'
        'Please try again soon :(\n'
    )


def prompt_loop_with_function(func, prompt):
    """
    Enter a loop executing a function repeatedly
    while prompting the user to continue or exit
    after each run.

    prompt should be the string message to print
    excluding the " (y/n): " suffix
    """
    rerun = 'y'
    while rerun != 'n':
        if rerun == 'y':
            func()
        else:
            print('INVALID INPUT')

        rerun = input(f'{prompt} (y/n): ')



def run_dice_roller():
    """
    Run the dice roller repeatedly until the user
    enters a response other than 'y' when prompted
    to roll again
    """
    prompt_loop_with_function(
        func=dice.dice_roller,
        prompt='Would you like to roll again?'
    )


def view_racial_bonuses():
    """
    Display racial bonuses to the user
    """
    util.race_bonuses()


def run_name_generator():
    prompt_loop_with_function(
        func=name_generator.give_name,
        prompt='Would you like to generate another name?'
    )


def run_ability_score_roller():
    prompt_loop_with_function(
        func=ability_roller.ability_scores,
        prompt='Would you like to use the ability score helper again?'
    )


def exit_program():
    print('\n'
          '===========================================\n'
          '\n'
          'Thank you for using the D&D 5e Helper Lite!\n'
          'Happy adventuring!\n'
          '\n'
          '===========================================\n'
          '\n'
      )
    exit()

main()
