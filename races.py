class Race(object):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof):
        self.name = name
        self.scores = scores
        self.vision = vision
        self.size = size
        self.languages = languages
        self.speed = speed
        self.r_traits = r_traits
        self.combat_prof = combat_prof
        self.tool_prof = tool_prof


class Dwarf(Race):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)


d = Dwarf('Dwarf Race', [0, 0, 2, 0, 0, 0], 60, 'Small', ['Common', 'Gnomish'], 25,
          ['Ability Score Increase - Your Constitution score increase by 2',
           'Dwarven Resilience - you have advantage on saving throws against poison, and you have resistance against'
           ' poison damage',
           'Stonecunning - Whenever you make an Intelligence (History) check related to the origin of stonework, '
           'you are'
           'considered proficient in the History skill and add double your proficiency bonus to the check, instead of '
           'your normal proficiency bonus.'],
          ['Battleaxe', 'Handaxe', 'Light Hammer', 'Warhammer'],
          ['Smith\'s Tools', 'Brewer\'s Supplies', 'Mason\'s Tools'])


class MountainDwarf(Dwarf):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


d_mountain = MountainDwarf('Mountain Dwarf Race', [2, 0, 2, 0, 0, 0], d.vision, d.size, d.languages, d.speed,
                           d.r_traits,
                           subr_traits=['Ability Score Increase - Your Strength score increases by 2.',
                                        'Dwarven Armor Training - You have proficiency with light and medium armor.'],
                           combat_prof=['Battleaxe', 'Handaxe', 'Light Hammer', 'Warhammer', 'Light Armor',
                                        'Medium Armor'],
                           tool_prof=d.tool_prof)


class HillDwarf(Dwarf):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


d_hill = HillDwarf('Hill Dwarf Race', [0, 0, 2, 0, 1, 0], d.vision, d.size, d.languages, d.speed, d.r_traits,
                   subr_traits=['Dwarven Toughness - Your hit point maximum increases by 1, and it increases by 1'
                                ' every time you gain a level.',
                                'Ability Score Increase - Your Wisdom score increases by 1.'],
                   combat_prof=d.combat_prof,
                   tool_prof=d.tool_prof)


class Elf(Race):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits,  combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)


e = Elf('Elf Race', [0, 2, 0, 0, 0, 0], 60, 'Medium', ['Common, Elvish'], 30,
        ['Ability Score Increase - Your Dexterity score increases by 2.',
         'Keen Senses - You have proficiency in the Perception Skill.',
         'Fey Ancestry - You have advantage on saving throws against being charmed, and magic can\'t put you to'
         ' sleep.',
         ' Trance - Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious,'
            ' for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you'
            ' can dream after a fashion; such dreams are actually mental exercises that have become '
            'reflexive through years of practice. After resting in this way, you gain the same benefit that'
            ' a human does from 8 hours of sleep.'],
        combat_prof=[None],
        tool_prof=[None])


class HighElf(Elf):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


high_e = HighElf('High Elf', [0, 2, 0, 1, 0, 0], e.vision, e.size,
                 languages=['Common', 'Elvish', 'Extra Language'],
                 speed=e.speed, r_traits=e.r_traits,
                 subr_traits=['Ability Score Increase - Your Intelligence score increases by 1.',
                              'Cantrip - You know one cantrip of your choice from the wizard spell list. Intelligence '
                              'is your spellcasting ability for it.',
                              'Extra Language - You can speak, read, and write one extra language of your choice.',
                              'Elf Weapon Training - You have proficiency with the longsword, shortsword, shortbow, '
                              'and the longbow.'],
                 combat_prof=['Longsword', 'Shortsword', 'Shortbow', ' Longbow'],
                 tool_prof=e.tool_prof)


class WoodElf(Elf):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


wood_e = WoodElf('Wood Elf', [0, 2, 0, 0, 1, 0], e.vision, e.size, e.languages, speed=35, r_traits=e.r_traits,
                 subr_traits=['Ability Score Increase - Your wisdom score increases by 1.',
                              'Fleet of Foot - Your base waling speed increases to 35 feet.',
                              'Mask of the Wild - You can attempt to hide even when you are only lightly obscured by '
                              'foliage, heavy rain, falling snow, mist, and other natural phenomena.',
                              'Elf Weapon Training - You have proficiency with the longsword, shortsword, shortbow, '
                              'and the longbow.'],
                 combat_prof=['Longsword', 'Shortsword', 'Shortbow', ' Longbow'],
                 tool_prof=e.tool_prof)


class DrowElf(Elf):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


drow_e = DrowElf('Drow Elf', [0, 2, 0, 0, 0, 1], vision=120, size=e.size, languages=e.languages, speed=e.speed,
                 r_traits=e.r_traits,
                 subr_traits=['Ability Score Increase - Your Charisma score increases by 1',
                              'Superior Darkvision - Your darkvision has a radius of 120 feet.',
                              'Sunlight Sensitivity - You have disadvantage on attack rolls and on Wisdom (Perception) '
                              'checks that rely on sight when you, the target of your attack, or whatever you are '
                              'trying to perceive is in direct sunlight.',
                              'Drow Magic - You know the \'dancing lights\' cantrip. When you reach 3rd level, you can '
                              'cast the \'faerie fire\' spell once with this trait and regain the ability to do so '
                              'when you finish a long rest. When you reach 5th level, you can cast the \'darkness\' '
                              'spell once with this trait and regain the ability to do so when you finish a long rest.'
                              'Charisma is your spellcasting ability for these spells.',
                              'Drow Weapon Training - You have proficiency with rapiers, shortswords, and hand '
                              'crossbows.'],
                 combat_prof=['Rapier', 'Shortsword', 'Hand Crossbow'],
                 tool_prof=e.tool_prof)


class Halfling(Race):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits,  combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)


half = Halfling('Halfling Race', [0, 2, 0, 0, 0, 0], 0, 'Small', ['Common', 'Halfling'], 25,
                ['Ability Score Increase - Your Dexterity score increase by 2.',
                 'Lucky - When you roll a 1 on the d20 for an attack roll, ability check, or saving throw, you can '
                 'reroll the die and must use the new roll.',
                 'Brave - You have advantage on saving throws against being frightened.',
                 'Halfling Nimbleness - You can move through the space of any creature that is of a size larger than '
                 'yours.'],
                combat_prof=[None],
                tool_prof=[None])


class LightfootHalfling(Halfling):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


lightfoot_half = LightfootHalfling('Lightfoot Halfling', [0, 2, 0, 0, 0, 1], half.vision, half.size, half.languages,
                                   half.speed, half.r_traits,
                                   subr_traits=['Ability Score Increase - Your Charisma score increases by 1.',
                                                'Naturally Stealthy - You can attempt to hide even when you are '
                                                'obscured by only a creature that is at least one size larger than '
                                                'you.'],
                                   combat_prof=half.combat_prof,
                                   tool_prof=half.tool_prof)


class StoutHalfling(Halfling):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


stout_half = StoutHalfling('Stout Halfling', [0, 2, 1, 0, 0, 0], half.vision, half.size, half.languages, half.speed,
                           half.r_traits,
                           subr_traits=['Ability Score Increase - Your Constitution score increases by 1.',
                                        'Stout Resilience - You have advantage on saving throws against poison, and '
                                        'you have resistance against poison damage.'],
                           combat_prof=half.combat_prof,
                           tool_prof=half.tool_prof)


class Human(Race):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits,  combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)


human = Human('Human Race', [1, 1, 1, 1, 1, 1], 0, 'Medium', ['Common', 'Extra Language'], 30,
              r_traits={None},
              combat_prof=[None],
              tool_prof=[None])


# # #  START DRAGONBORNs
class Dragonborn(Race):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits,  combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)


dragonborn = Dragonborn('Dragonborn Race', [2, 0, 0, 0, 0, 1], 0, 'Medium', ['Common', 'Draconic'], 30,
                        r_traits={'Ability Score Increase': {'Strength': 2,
                                                             'Charisma': 1},
                                  'Draconic Ancestry': 'You have draconic ancestry. Choose one type of dragon from the '
                                                       'Draconic Ancestry table (or subrace). Your breath weapon and '
                                                       'damage resistance are determined by the dragon type, as shown '
                                                       'in the table (PHB page 34).',

                                  'Breath Weapon': 'You can use your action to exhale destructive energy. Your '
                                                   'draconic ancestry determines the size, shape, and damage type of '
                                                   'the exhalation. When you use your breath weapon, each creature in '
                                                   'the area of the exhalation must make a saving throw, the type of '
                                                   'which is determined by your draconic ancestry. The DC for this '
                                                   'saving throw equals 8 + your Constitution modifier + your '
                                                   'proficiency bonus. A creature takes 2d6 damage on a failed save, '
                                                   'and half as much damage on a successful one. The damage increases '
                                                   'to 3d6 at 6th level, 4d6 at 11th level, and 5d6 at 16th level. '
                                                   'After you use your breath weapon, you can’t use it again until you '
                                                   'complete a short or long rest.',
                                  'Damage Resistance': 'You have resistance to the damage type associated with your '
                                                       'draconic ancestry.'},
                        combat_prof=[None],
                        tool_prof=[None])


class BlackDragonborn(Dragonborn):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


black_dragonborn = BlackDragonborn('Black Dragonborn', dragonborn.scores, dragonborn.vision, dragonborn.size,
                                   dragonborn.languages, dragonborn.speed, dragonborn.r_traits,
                                   subr_traits={'Dragon Color': 'Black',
                                                'Damage Type': 'Acid',
                                                'Breath Weapon': '5 by 30 ft. line (Dex. save)'},
                                   combat_prof=dragonborn.combat_prof,
                                   tool_prof=dragonborn.tool_prof)


class BlueDragonborn(Dragonborn):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


blue_dragonborn = BlueDragonborn('Blue Dragonborn', dragonborn.scores, dragonborn.vision, dragonborn.size,
                                 dragonborn.languages, dragonborn.speed, dragonborn.r_traits,
                                 subr_traits={'Dragon Color': 'Blue',
                                              'Damage Type': 'Lightning',
                                              'Breath Weapon': '5 by 30 ft. line (Dex. save)'},
                                 combat_prof=dragonborn.combat_prof,
                                 tool_prof=dragonborn.tool_prof)


class BrassDragonborn(Dragonborn):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


brass_dragonborn = BrassDragonborn('Brass Dragonborn', dragonborn.scores, dragonborn.vision, dragonborn.size,
                                   dragonborn.languages, dragonborn.speed, dragonborn.r_traits,
                                   subr_traits={'Dragon Color': 'Brass',
                                                'Damage Type': 'Fire',
                                                'Breath Weapon': '5 by 30 ft. line (Dex. save)'},
                                   combat_prof=dragonborn.combat_prof,
                                   tool_prof=dragonborn.tool_prof)


class BronzeDragonborn(Dragonborn):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


bronze_dragonborn = BronzeDragonborn('Bronze Dragonborn', dragonborn.scores, dragonborn.vision, dragonborn.size,
                                     dragonborn.languages, dragonborn.speed, dragonborn.r_traits,
                                     subr_traits={'Dragon Color': 'Bronze',
                                                  'Damage Type': 'Lightning',
                                                  'Breath Weapon': '5 by 30 ft. line (Dex. save)'},
                                     combat_prof=dragonborn.combat_prof,
                                     tool_prof=dragonborn.tool_prof)


class CopperDragonborn(Dragonborn):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


copper_dragonborn = CopperDragonborn('Copper Dragonborn', dragonborn.scores, dragonborn.vision, dragonborn.size,
                                     dragonborn.languages, dragonborn.speed, dragonborn.r_traits,
                                     subr_traits={'Dragon Color': 'Copper',
                                                  'Damage Type': 'Acid',
                                                  'Breath Weapon': '5 by 30 ft. line (Dex. save)'},
                                     combat_prof=dragonborn.combat_prof,
                                     tool_prof=dragonborn.tool_prof)


class GoldDragonborn(Dragonborn):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


gold_dragonborn = GoldDragonborn('Gold Dragonborn', dragonborn.scores, dragonborn.vision, dragonborn.size,
                                 dragonborn.languages, dragonborn.speed, dragonborn.r_traits,
                                 subr_traits={'Dragon Color': 'Gold',
                                              'Damage Type': 'Fire',
                                              'Breath Weapon': '15 ft. cone (Dex save)'},
                                 combat_prof=dragonborn.combat_prof,
                                 tool_prof=dragonborn.tool_prof)


class GreenDragonborn(Dragonborn):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


green_dragonborn = GreenDragonborn('Green Dragonborn', dragonborn.scores, dragonborn.vision, dragonborn.size,
                                   dragonborn.languages, dragonborn.speed, dragonborn.r_traits,
                                   subr_traits={'Dragon Color': 'Green',
                                                'Damage Type': 'Poison',
                                                'Breath Weapon': '15 ft. cone (Con save)'},
                                   combat_prof=dragonborn.combat_prof,
                                   tool_prof=dragonborn.tool_prof)


class RedDragonborn(Dragonborn):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


red_dragonborn = RedDragonborn('Red Dragonborn', dragonborn.scores, dragonborn.vision, dragonborn.size,
                               dragonborn.languages, dragonborn.speed, dragonborn.r_traits,
                               subr_traits={'Dragon Color': 'Red',
                                            'Damage Type': 'Fire',
                                            'Breath Weapon': '15 ft. cone (Dex save)'},
                               combat_prof=dragonborn.combat_prof,
                               tool_prof=dragonborn.tool_prof)


class SilverDragonborn(Dragonborn):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


silver_dragonborn = SilverDragonborn('Silver Dragonborn', dragonborn.scores, dragonborn.vision, dragonborn.size,
                                     dragonborn.languages, dragonborn.speed, dragonborn.r_traits,
                                     subr_traits={'Dragon Color': 'Silver',
                                                  'Damage Type': 'Cold',
                                                  'Breath Weapon': '15 ft. cone (Con save)'},
                                     combat_prof=dragonborn.combat_prof,
                                     tool_prof=dragonborn.tool_prof)


class WhiteDragonborn(Dragonborn):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


white_dragonborn = WhiteDragonborn('White Dragonborn', dragonborn.scores, dragonborn.vision, dragonborn.size,
                                   dragonborn.languages, dragonborn.speed, dragonborn.r_traits,
                                   subr_traits={'Dragon Color': 'White',
                                                'Damage Type': 'Cold',
                                                'Breath Weapon': '15 ft. cone (Con save)'},
                                   combat_prof=dragonborn.combat_prof,
                                   tool_prof=dragonborn.tool_prof)


# # #  END DRAGONBORNs


class Gnome(Race):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits,  combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)


g = Gnome('Gnome Race', [0, 0, 0, 2, 0, 0], 60, 'Small', ['Common', 'Gnomish'], 25,
          r_traits={'Ability Score Increase': {'Intelligence': 2},
                    'Gnome Cunning':'You have advantage on all Intelligence, Wisdom, and Charisma saving throws '
                    'against magic.'},
          combat_prof=[None],
          tool_prof=[None])


class ForestGnome(Gnome):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


forest_g = ForestGnome('Forest Gnome', [0, 1, 0, 2, 0, 0], g.vision, g.size, g.languages, g.speed,
                       r_traits=g.r_traits,
                       subr_traits={'Ability Score Increase': {'Dexterity', 1},
                                    'Natural Illusionist': 'You know the minor illusion cantrip. Intelligence is your '
                                                           'spellcasting ability for it.',
                                    'Speak with Small Beasts': 'Through sounds and gestures, you can communicate '
                                                               'simple ideas with Small or smaller beasts. Forest '
                                                               'gnomes love animals and often keep squirrels, badgers, '
                                                               'rabbits, moles, woodpeckers, and other creatures as '
                                                               'beloved pets.'},
                       combat_prof=g.combat_prof,
                       tool_prof=g.tool_prof)


class RockGnome(Gnome):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


rock_g = RockGnome('Rock Gnome', [0, 0, 1, 2, 0, 0], g.vision, g.size, g.languages, g.speed,
                   r_traits=g.r_traits,
                   subr_traits={'Ability Score Increase': {'Constitution', 1},
                                'Artificer\'s Lore': 'Whenever you make an Intelligence (History) check related to '
                                                     'magic items, alchemical objects, or technological devices, you '
                                                     'can add twice your proficiency bonus, instead of any proficiency '
                                                     'bonus you normally apply.'},
                   combat_prof=g.combat_prof,
                   tool_prof=['Tinker - You have proficiency in with artisan\'s tools (tinker\'s tools). Using those '
                              'tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork '
                              'device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 '
                              'hour repairing it to keep the device functioning), or when you use your action to '
                              'dismantle it; at that time, you can reclaim the materials used to create it. You can '
                              'have up to three such devices active at a time. When you create a device, choose one '
                              'of the following options:',
                              ['Clockwork Toy - This toy is a clockwork animal, monster, or person, such as a frog, '
                               'mouse, bird, dragon, or soldier. When placed on the ground, the toy moves 5 feet '
                               'across the ground on each of your turns in a random direction. It makes noises as '
                               'appropriate to the creature it represents.',

                               'Fire Starter - This device produces a miniature flame, which you can use to light a '
                               'candle, torch, or campfire. Using the device requires your action.',

                               'Music Box - When opened, this music box plays a single song at a moderate volume. The '
                               'box stops playing when it reaches the song\'s end or when it is closed.']], )


class HalfElf(Race):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits,  combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)


half_e = HalfElf('Half-Elf Race', [0, 0, 0, 0, 0, 2], 60, 'Medium', ['Common', 'Elvish', 'Extra Language'], 30,
                 r_traits={'Ability Score Increase': {'Charisma': 2,
                                                      'First Half-Elf Increase': 1,
                                                      'Second Half-Elf Increase': 1},
                           'Fey Ancestry': 'You have advantage on saving throws against being charmed, and magic '
                                           'cannot put you to sleep',
                           'Skill Versatility': 'You gain proficiency in two skills of your choice.'},
                 combat_prof=[None],
                 tool_prof=[None])


class HalfOrc(Race):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits,  combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)


half_o = HalfOrc('Half Orc Race', [2, 0, 1, 0, 0, 0], 60, 'Medium', ['Common', 'Orc'], 30,
                 r_traits={'Ability Score Increase': {'Strength': 2,
                                                      'Constitution': 1},
                           'Menacing': 'You gain proficiency in the Intimidation skill.',
                           'Relentless Endurance': 'When you are reduced to 0 hit points but not killed outright, you '
                                                   'can drop to 1 hit point instead. You can\'t use this feature again '
                                                   'until you finish a long rest.',
                           'Savage Attacks': 'When you score a critical hit with a melee weapon attack, you can roll '
                                             'one of the weapon\'s damage dice one additional time and add it to the '
                                             'extra damage of the critical hit.'},
                 combat_prof=[None],
                 tool_prof=[None])


class Tiefling(Race):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)


t = Tiefling('Tiefling', [0, 0, 0, 1, 0, 2], 60, 'Medium', ['Common', 'Infernal'], 30,
             r_traits={'Hellish Resistance': 'You have resistance to fire damage'},
             combat_prof=[None],
             tool_prof=[None])


class AsmodeusTiefling(Tiefling):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


asmodeus_t = AsmodeusTiefling('Asmodeus Tiefling', t.scores, t.size, t.vision, t.languages, t.speed, t.r_traits,
                              subr_traits={'Ability Score Increase': {'Charisma': 2,
                                                                      'Intelligence': 1},
                                           'Infernal Legacy': 'You know the Thaumaturgy cantrip. Once you reach 3rd '
                                                              'level, you can cast the Hellish Rebuke spell as a 2nd-'
                                                              'level spell; you must finish a long rest in order to '
                                                              'cast the spell again using this trait. Once you reach '
                                                              '5th level, you can also cast the Darkness spell; you '
                                                              'must finish a long rest in order to cast the spell '
                                                              'again using this trait. Charisma is your spellcasting '
                                                              'ability for these spells.'},
                              combat_prof=t.combat_prof,
                              tool_prof=t.tool_prof)


class BaalzeBulTiefling(Tiefling):
    def __init__(self, name, scores, vision, size, languages, speed, r_traits, subr_traits, combat_prof, tool_prof):
        super().__init__(name, scores, vision, size, languages, speed, r_traits, combat_prof, tool_prof)
        self.subr_traits = subr_traits


baalzebul_t = AsmodeusTiefling('BaalzeBul Tiefling', t.scores, t.size, t.vision, t.languages, t.speed, t.r_traits,
                               subr_traits={'Ability Score Increase': {'Charisma': 2,
                                                                       'Intelligence': 1},
                                            'Infernal of Maladomini': 'You know the Thaumaturgy cantrip. Once you '
                                                                      'reach 3rd level, you can cast the Ray of '
                                                                      'Sickness spell as a 2nd-level spell once with '
                                                                      'this trait and regain the ability to do so once '
                                                                      'you finish a long rest. Once you reach 5th '
                                                                      'level, you can cast the Crown of Madness spell '
                                                                      'once with this trait and regain the ability to '
                                                                      'do so once you finish a long rest. Charisma is '
                                                                      'your spellcasting ability for these spells.'},
                               combat_prof=t.combat_prof,
                               tool_prof=t.tool_prof)


'''
Race Traits

Human Traits
  Variant Human  # I DID NOT ADD THE VARIANT HUMAN AS A SUBRACE. SEE GOOGLE DOCS FOR WHY.
    Ability Score Increase - Two different ability scores of your choice increase by 1.
    Skills - You gain proficiency in one skill of your choice.
    Feat - You gain one feat of your choice.


# OLD RACE STUFF

# KEYS
# 0 = Race Name
# 1 = Ability Score Bonuses
#           in Ability Score List [0 = STR, 1 = DEX, 2 = CON, 3 = INT, 4 = WIS, 5 = CHA]
# 2 = Dark vision   | 3 = Size
# 4 = Languages     | 5 = Speed
# 6 = Race Traits   | 7 = Subclass Traits
# 8 = Proficiencies


standard_races = {
    'dwarf_hill': {0: 'Hill Dwarf', 1: [0, 0, 2, 0, 1, 0], 2: 60, 3: 'Small', 4: ['Common', 'Gnomish'], 5: 25, 6:
        ['Dwarven Resilience -'], 7: ['Dwarven Toughness - Your hit point maximum increases by 1, and it increases by 1'
                                      ' every time you gain a level.']},
    'dwarf_mountain': {0: 'Mountain Dwarf', 1: [2, 0, 2, 0, 0, 0], 2: 60, 3: 'Small', 4: ['Common', 'Gnomish'], 5: 25,
                       },
    'elf_high': {0: [0, 2, 0, 1, 0, 0]},
    'elf_wood': {0: [0, 2, 0, 0, 1, 0]},
    'elf_drow': {0: [0, 2, 0, 0, 0, 1]},
    'halfling_lightfoot': {0: [0, 2, 0, 0, 0, 1]},
    'halfling_stout': {0: [0, 2, 1, 0, 0, 0]},
    'human': {0: [1, 1, 1, 1, 1, 1]},
    'human_variant': {0: [1, 1, 1, 1, 1, 1]},
    'dragonborn': {0: [2, 0, 0, 0, 0, 1]},
    'gnome_forest': {0: [0, 1, 0, 2, 0, 0]},
    'gnome_rock': {0: [0, 0, 1, 2, 0, 0]},
    'half_elf': {0: [0, 0, 0, 0, 0, 2]},
    'half_orc': {0: [2, 0, 1, 0, 0, 0]},
    'tiefling': {0: [0, 0, 0, 1, 0, 2]},
}

# for ab in standard_races['dwarf_hill'][0]:
#     print(ab, end=' | ')

# print([standard_races['gnome_rock'][0][3]])
#     Figured it out! To print the individual ability scores in from the dictionary,
#     follow the pattern above. the first index after the race is the ability score
#     list which should be 0, then use the second [] to pick the individual ability
#     score from that list.

# print('STR: ', standard_races['dwarf_hill'][0][0], 'DEX: ', standard_races['dwarf_hill'][0][1], 'CON: ',
#       standard_races['dwarf_hill'][0][2], 'INT: ', standard_races['dwarf_hill'][0][3], 'WIS: ', standard_races['dwarf_hill'][0][4], 'CHA: ',
#       standard_races['dwarf_hill'][0][0])
#   Just a template for printing out a race ability scores.

character.set_race(races.race.name)
character.set_str(races.race.scores[0])
character.set_vision(races.race.vision)
character.set_size(races.race.size)
character.set_languages(races.race.languages)
character.set_speed(races.race.speed)
character.set_r_traits(races.race.r_traits)
character.set_subr_traits(races.race.subr_traits)
character.set_combat_prof(races.race.combat_prof)
character.set_tool_prof(races.race.tool_prof)

print(character.
'''
