import random


def dice_roller():
    print()
    die_sides = int(input('How many sides are on the die: '))
    dice_amt = int(input('How many dice would you like to roll: '))
    roll_totals = []

    while len(roll_totals) < dice_amt:
        roll_totals.append(random.randint(1, die_sides))

        if len(roll_totals) == dice_amt:
            print()
            print('Your rolls are', *roll_totals, sep=', ')
            print('and the total is', sum(roll_totals))
            print()
            break



