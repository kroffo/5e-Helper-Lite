import random

# Remove this ya fool
gen_name = []

FIRST_NAMES = [
    'Argo', 'Senic', 'Elbane', 'Irina',
    'Nilex', 'Cornelius', 'Kenton', 'Loxie', 'Jairo',
    'Josette', 'Klaudius', 'Laharo',
    'Jeren', 'Mayda', 'Irden', 'Ashtyn', 'Brennen',
    'Tsao', 'Jinn', 'Valiant'
]

LAST_NAMES = [
    'Aljack', 'Alamondar', 'Balaskor', 'Belturret', 'Blaurbuckle',
    'Blent', 'Caunor', 'Coldspar', 'Curhelm', 'Darvent', 'Dornwood',
    'Dunflask', 'Elfgard', 'Elstorn', 'Falkyn', 'Farhaven',
    'Fornadar', 'Gaunt', 'Ghelkyn', 'Gostskar',
    'Gyrhall', 'Harbranch'
]

def generate_name():
    first = random.choice(FIRST_NAMES)
    last = random.choice(LAST_NAMES)
    return f'{first} {last}'

def give_name():
    print()
    character_name = []
    gen_name = []
    gen_name.clear()
    gen_name.append(first_names().pop())
    gen_name.append(last_names().pop())
    print('Your character\'s name is : ', *gen_name, sep=' ')
    print()


def first_names():
    names = ['Argo', 'Senic', 'Elbane', 'Irina',
                   'Nilex', 'Cornelius', 'Kenton', 'Loxie', 'Jairo',
                   'Josette', 'Klaudius', 'Laharo',
                   'Jeren', 'Mayda', 'Irden', 'Ashtyn', 'Brennen',
                   'Tsao', 'Jinn', 'Valiant']

    random.shuffle(names)
    # print(names) DEBUG
    return names


def last_names():
    names = ['Aljack', 'Alamondar', 'Balaskor', 'Belturret', 'Blaurbuckle',
                  'Blent', 'Caunor', 'Coldspar', 'Curhelm', 'Darvent', 'Dornwood',
                  'Dunflask', 'Elfgard', 'Elstorn', 'Falkyn', 'Farhaven',
                  'Fornadar', 'Gaunt', 'Ghelkyn', 'Gostskar',
                  'Gyrhall', 'Harbranch']

    random.shuffle(names)
    # print(names) DEBUG
    return names
