import util
import dice_roller as dice
import character_creator as cc
import name_generator
import ability_roller


def main():
    util.intro()
    display_menu()


def display_menu():
    print('MENU')
    print('------------------------')
    print('1. Dice Roller')
    print('2. View Racial Bonuses')
    print('3. Name Generator')
    print('4. Ability Score Roller')
    print('5. Character Creator')
    print('6. Quit Program')
    print()
    menu_choice = ''
    menu_choice = input('Enter the number of the program you would like to use: ')
    if menu_choice == '6':
        print()
        print('===========================================')
        print()
        print('Thank you for using the D&D 5e Helper Lite!')
        print('Happy adventuring!')
        print()
        print('===========================================')
        print()
        exit()
    while menu_choice != '6':
        if menu_choice == '1':
            dice.dice_roller()
            roll_again = ''
            while roll_again != 'n':
                roll_again = input('Would you like to roll again? (y/n)')
                if str.lower(roll_again) == 'y':
                    dice.dice_roller()
                elif str.lower(roll_again) == 'n':
                    print()
                    display_menu()
                    break
        elif menu_choice == '2':
            util.race_bonuses()
            menu = ''
            while menu != 'M':
                print()
                menu = input('Type "M" to return to the menu. ')
                if str.lower(menu) == 'm':
                    print()
                    display_menu()
                    break
                else:
                    print('INVALID INPUT')
        elif menu_choice == '3':
            name_generator.give_name()
            another_name = ''
            while another_name != 'n':
                another_name = input('Would you like to roll again? (y/n)')
                if str.lower(another_name) == 'y':
                    name_generator.give_name()
                elif str.lower(another_name) == 'n':
                    print()
                    display_menu()
                    break
                else:
                    print('INVALID INPUT')
                    print()
        elif menu_choice == '4':
            ability_roller.ability_scores()
            repeat = ''
            while repeat != 'n':
                repeat = input('Would you like to use the ability score helper again? (y/n) ')
                if str.lower(repeat) == 'y':
                    ability_roller.ability_scores()
                elif str.lower(repeat) == 'n':
                    print()
                    display_menu()
                    break
        else:
            print('INVALID INPUT')
            print()
            display_menu()
            break


main()
