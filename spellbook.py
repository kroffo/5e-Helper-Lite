cantrip_spellbook = {  #line 526 is where 1st level spells start.
    'Acid Splash': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Conjuration',
        'castTime': '1 action',
        'range': '60 feet',
        'components': ['V', 'S'],  # I don't know how multiple components should be formatted...
        'duration': 'Instantaneous',
        'classes': ['Artificer', 'Fighter (Eldritch Knight)', 'Rouge (Arcane Trickster)', 'Sorcerer', 'Wizard'],
        'subclasses': [''],
        'description': ['You hurl a bubble of acid. Choose one creature you can see within range, or choose two '
                        'creatures you can see within range that are within 5 feet of each other. A target must '
                        'succeed on a Dexterity saving throw or take 1d6 acid damage.',

                        'This spell\'s damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and '
                        '17th level (4d6)'],
        'id': 0.1
    },
    'Blade Ward': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Abjuration',
        'castTime': '1 action',
        'range': 'Self',
        'components': ['V', 'S'],
        'duration': '1 round',
        'classes': ['Bard', 'Fighter (Eldritch Knight)', 'Rouge (Arcane Trickster)', 'Sorcerer', 'Wizard'],
        'subclasses': [''],
        'description': ['You extend you hand and trace a sigil of warding in the air. Until the end of your next turn, '
                        'you have resistance against bludgeoning, piercing, and slashing damage dealt by weapon '
                        'attacks.'],
        'id': 0.2
    },
    'Chill Touch': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Necromancy',
        'castTime': '1 action',
        'range': '120 feet',
        'components': ['V', 'S'],
        'duration':'1 round',
        'classes': ['Fighter (Eldritch Knight)', 'Rouge (Arcane Trickster)', 'Sorcerer', 'Wizard'],
        'subclasses': ['Druid (Spores)'],
        'description': ['You create a ghostly, skeletal hand in the space of a creature within range. Make a ranged '
                        'spell attack against the creature to assail it with the chill of the grave. On a hit, the '
                        'target takes 1d8 necrotic damage, and it can\'t regain hit points until the start of your '
                        'next turn. Until then, the hand clings to the target.',

                        'If you hit an undead target, it also has disadvantage on attack rolls on attack rolls against '
                        'you until the end of your next turn.',

                        'This spell\'s damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and '
                        '17th level (4d8)'],
        'id': 0.3
    },
    'Dancing Lights': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Evocation',
        'castTime': '1 action',
        'range': '120 feet',                              # Wychwood is spelled correctly
        'components': ['V', 'S', 'M (A bit of phosphorus or wychwood, or a glowworm)'],
        'duration': 'Concentration, up to 1 min',
        'classes': ['Artificer', 'Bard', 'Fighter (Eldritch Knight)', 'Rouge (Arcane Trickster)', 'Sorcerer', 'Wizard'],
        'subclasses': [''],
        'description': ['You create up to four torch-sized lights within range, making them appear as torches, '
                        'lanterns, or glowing orbs that hover in the air for the duration. You can also combine the '
                        'four lights into one glowing vaguely humanoid form of Medium size. Whichever form you choose, '
                        'each light sheds dim light in a 10-foot radius.',

                        'As a bonus action on your turn, you can move the lights up to 60 feet to a new spot within '
                        'range. A light must be within 20 feet of another light created by this spell, and a light '
                        'winks out if it exceeds the spell\'s range. '],
        'id': 0.4
    },
    'Druidcraft': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Transmutation',
        'castTime': '1 action',
        'range': '30 feet',
        'components': ['V', 'S'],
        'duration': 'Instantaneous',
        'classes': ['Druid'],
        'subclasses': [''],
        'description': ['Whispering to the spirits of nature, you create one of the following effects within range: '
                        '       - You create a tiny, harmless sensory effect that predicts what the weather will be at '
                        'your location for the next 24 hours. The effect might manifest as a golden orb for clear '
                        'skies, a cloud for rain, falling snowflakes for snow, and so on. This effect persists for 1 '
                        'round.',
                        '       - You instantly make a flower blossom, a seed pod open, or a leaf bud bloom.',
                        '       - You create an instantaneous, harmless sensory effect, such as falling leaves, a puff '
                        'of wind, the sound of a small animal, or the faint odor of skunk. The effect must fit in a '
                        '5-foot cube.',
                        'You instantly light or snuff out a candle, a torch, or a small campfire.'],
        'id': 0.5
    },
    'Eldritch Blast': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Evocation',
        'castTime': '1 action',
        'range': '120 feet',
        'components': ['V', 'S'],
        'duration': 'Instantaneous',
        'classes': ['Warlock'],
        'subclasses': [''],
        'description': ['A beam of crackling energy streaks toward a creature within range. Make a ranged spell attack '
                        'against the target. On a hit, the target takes 1d10 force damage.',

                        'The spell creates more than one beam when you reach higher levels: two beams at 5th level, '
                        'three beams at 11th level, and four beams at 17th level. You can direct the beams at the same '
                        'target or at different ones. Make a separate attack roll for each beam.'],
        'id': 0.6
    },
    'Fire Bolt': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Evocation',
        'castTime': '1 action',
        'range': '120 feet',
        'components': ['V', 'S'],
        'duration': 'Instantaneous',
        'classes': ['Artificer', 'Fighter (Eldritch Knight)', 'Rouge (Arcane Trickster)', 'Sorcerer', 'Wizard'],
        'subclasses': [''],
        'description': ['You hurl a mote of fire at a creature or object within range. Make a ranged spell attack '
                        'against the target. On a hit, the target takes 1d10 fire damage. A flammable object hit by '
                        'this spell ignites if it isn\'t being worn or carried.',

                        'This spell\'s damage increases by 1d10 when you reach 5th level (2d10), 11th level (3d10), '
                        'and 17th level (4d10)'],
        'id': 0.7
    },
    'Friends': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Enchantment',
        'castTime': '1 action',
        'range': 'Self',
        'components': ['S', 'M (a small amount of makeup applied to the face as the spell is cast'],
        'duration': 'Concentration, up to 1 minute',
        'classes': ['Bard', 'Fighter (Eldritch Knight)', 'Rouge (Arcane Trickster)', 'Sorcerer', 'Warlock', 'Wizard'],
        'subclasses': [''],
        'description': ['For the duration, you have advantage on all Charisma checks directed at one creature of your '
                        'choice that isn\'t hostile toward you. When the spell ends, the creature realizes that you '
                        'used magic to influence its mood and becomes hostile toward you. A creature prone to '
                        'violence might attack you. Another creature might seek retribution in other ways (at the '
                        'DM\'s discretion), depending on the nature of your interaction with it.'],
        'id': 0.8
    },
    'Guidance': {
        'source': 'Player\'s Handbook',
        'level': '0',
        'school': 'Divination',
        'castTime': '1 action',
        'range': 'Touch',
        'components': ['V', 'S'],
        'duration': 'Concentration, up to 1 minute',
        'classes': ['Artificer', 'Cleric', 'Druid'],
        'subclasses': ['Bard (Spirits)', 'Druid (Stars)', 'Sorcerer (Divine Soul)'],
        'description': ['You touch one willing creature. Once before the spell ends, the target can roll a d4 and add '
                        'the number rolled to one ability check of its choice. It can roll the die before or after '
                        'making the ability check. The spell then ends.'],
        'id': 0.9
},
    'Light': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Evocation',
        'castTime': '1 action',
        'range': 'Touch',
        'components': ['V', 'M (a firefly or phosphorescent moss)'],
        'duration': '1 hour',
        'classes': ['Artificer', 'Bard', 'Cleric', 'Fighter (Eldritch Knight)', 'Rouge (Arcane Trickster)', 'Sorcerer',
                    'Wizard'],
        'subclasses': ['Sorcerer (Divine Soul)', 'Warlock (Celestial)'],
        'description': ['You touch one object that is no larger than 10 feet in any dimension. Until the spell ends, '
                        'the object sheds bright light in a 20-foot radius and dim light for an additional 20 feet. '
                        'The light can be colored as you like. Completely covering the object with something opaque '
                        'blocks the light. The spell ends if you cast it again or dismiss it as an action.',

                        'If you target an object held or worn by a hostile creature, that creature must succeed on a '
                        'Dexterity saving throw to avoid the spell.'],
        'id': 0.10
    },
    'Mage Hand': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Conjuration',
        'castTime': '1 action',
        'range': '30 feet',
        'components': ['V', 'S'],
        'duration': '1 minute',
        'classes': ['Artificer', 'Bard', 'Fighter (Eldritch Knight)', 'Rouge (Arcane Trickster)', 'Sorcerer',
                    'Warlock', 'Wizard'],
        'subclasses': ['Ranger (Swarmkeeper)'],
        'description': ['A spectral, floating hand appears at a point you choose within range. The hand lasts for the '
                        'duration or until you dismiss it as an action. The hand vanishes if it is ever more than 30 '
                        'feet away from you or if you cast this spell again.',

                        'You can use your action to control the hand. You can use the hand to manipulate an object, '
                        'open an unlocked door or container, stow or retrieve an item from an open container, or pour '
                        'the contents out of a vial. You can move the hand up to 30 feet each time you use it.',

                        'The hand can\'t attack, activate magical items, or carry more than 10 pounds.'],
        'id': 0.11
    },
    'Mending': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Transmutation',
        'castTime': '1 action',
        'range': 'Touch',
        'components': ['V', 'S', 'M (two lodestones)'],
        'duration': 'Instantaneous',
        'classes': ['Artificer', 'Bard', 'Cleric', 'Druid', 'Fighter (Eldritch Knight)', 'Rouge (Arcane Trickster)',
                    'Sorcerer', 'Wizard'],
        'subclasses': ['Sorcerer (Divine Soul)'],
        'description': ['The spell repairs a single bread or tear in an object you touch, such as broken chain link, '
                        'two halves of a broken key, a torn cloak, or a leaking wineskin. As long as the break or '
                        'tear is no larger than 1 foot in any dimension, you mend it, leaving no trace of the former '
                        'damage.',

                        'This spell can physically repair a magic item or construct, but the spell can\'t restore '
                        'magic to such an object.'],
        'id': 0.12
    },
    'Message': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Transmutation',
        'castTime': '1 action',
        'range': '120 feet',
        'components': ['V', 'S', 'M (a short piece of copper wire)'],
        'duration': '1 round',
        'classes': ['Artificer', 'Bard', 'Fighter (Eldritch Knight)', 'Rouge (Arcane Trickster)', 'Sorcerer', 'Wizard'],
        'subclasses': [''],
        'description': ['You point your finger toward a creature within range and whisper a message. The target (and '
                        'only the target) hears the message and can reply in a whisper that only you can hear.',

                        'You can cast this spell through solid objects if you are familiar with the target and know '
                        'it is beyond the barrier. Magical silence, 1 foot of stone, 1 inch of common metal, a thin '
                        'sheet of lead, or 3 feet of wood blocks the spell. The spell doesn\'t have to follow a '
                        'straight line and can travel freely around corners or through openings'],
        'id': 0.13
    },
    'Minor Illusion': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Illusion',
        'castTime': '1 action',
        'range': '30 feet',
        'components': ['S', 'M (a bit of fleece)'],
        'duration': '1 minute',
        'classes': ['Bard', 'Fighter (Eldritch Knight)', 'Rouge (Arcane Trickster)', 'Sorcerer', 'Warlock', 'Wizard'],
        'subclasses': ['Monk (Shadow)'],
        'description': ['You create a sound or an image of an object within range that lasts for the duration. The '
                        'illusion also ends if you dismiss it as an action or cast this spell again.',

                        'If you create a sound, its volume can range from a whisper to a scream. It can be your '
                        'voice, someone else\'s voice, a lion\'s roar, a beating of drums, or any other sound you '
                        'choose. The sound continues unabated throughout the duration, or you can make discrete '
                        'sounds at different times before the spell ends.',

                        'If you create an image of an object — such as a chair, muddy footprints, or a small chest — '
                        'it must be no larger than a 5-foot cube. The image can\'t create sound, light, smell, or any '
                        'other sensory effect. Physical interaction with the image reveals it to be an illusion, '
                        'because things can pass through it.',

                        'If a creature uses its action to examine the sound or image, the creature can determine that '
                        'it is an illusion with a successful Intelligence (Investigation) check against your spell '
                        'save DC. If a creature discerns the illusion for what it is, the illusion becomes faint to '
                        'the creature.'],
        'id': 0.14
    },
    'Poison Spray': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Conjuration',
        'castTime': '1 action',
        'range': '10 feet',
        'components': ['V', 'S'],
        'duration': 'Instantaneous',
        'classes': ['Artificer', 'Druid', 'Fighter (Eldritch Knight)', 'Rouge (Arcane Trickster)', 'Sorcerer',
                    'Warlock', 'Wizard'],
        'subclasses': [''],
        'description': ['You extend your hand toward a creature you can see within range and project a puff of noxious '
                        'gas from your palm. The creature must succeed on a Constitution saving throw or take 1d12 '
                        'poison damage.',

                        'This spell\'s damage increases by 1d12 when you reach 5th level (2d12), 11th level (3d12), '
                        'and 17th level (4d12).'],
        'id': 0.15
    },
    'Prestidigitation': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Transmutation',
        'castTime': '1 action',
        'range': '10 feet',
        'components': ['V', 'S'],
        'duration': '1 hour',
        'classes': ['Artificer', 'Bard', 'Fighter (Eldritch Knight)', 'Rouge (Arcane Trickster)', 'Sorcerer',
                    'Warlock', 'Wizard'],
        'subclasses': [''],
        'description': ['This spell is a minor magical trick that novice spellcasters use for practice. You create one '
                        'of the following magical effects within range: ',
                        '   - You create an instantaneous, harmless sensory effect, such as a shower of sparks, a puff '
                        'of wind, faint musical notes, or an odd odor.',
                        '   - You instantaneously light or snuff out a candle, a torch, or a small campfire. ',
                        '   - You instantaneously clean or soil an object no larger than 1 cubic foot.',
                        '   - You chill, warm, or flavor up to 1 cubic foot of nonliving material for 1 hour.',
                        '   - You make a color, a small mark, or a symbol appear on an object or a surface for 1 hour.',
                        '   - You create a non-magical trinket or an illusory image that can fit in your hand and that '
                        'lasts until the end of your next turn.',
                        '   - If you cast this spell multiple times, you can have up to three of its non-instantaneous '
                        'effects active at a time, and you can dismiss such an effect as an action.'],
        'id': 0.16
    },
    'Produce Flame': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Conjuration',
        'castTime': '1 action',
        'range': 'Self',
        'components': ['V', 'S'],
        'duration': '10 minutes',
        'classes': ['Druid'],
        'subclasses': [''],
        'description': ['A flickering flame appears in your hand. The flame remains there for the duration and harms '
                        'neither you nor your equipment. The flame sheds bright light in a 10-foot radius and dim '
                        'light for an additional 10 feet. The spell ends if you dismiss it as an action or if you cast '
                        'it again.',

                        'You can also attack with the flame, although doing so ends the spell. When you cast this '
                        'spell, or as an action on a later turn, you can hurl the flame at a creature within 30 feet '
                        'of you. Make a ranged spell attack. On a hit, the target takes 1d8 fire damage.',

                        'This spell\'s damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and '
                        '17th level (4d8).'],
        'id': 0.17
},
    'Ray of Frost': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Evocation',
        'castTime': '1 action',
        'range': '60 feet',
        'components': ['V', 'S'],
        'duration': 'Instantaneous',
        'classes': ['Artificer', 'Fighter (Eldritch Knight', 'Rouge (Arcane Trickster)', 'Sorcerer', 'Wizard'],
        'subclasses': [''],
        'description': ['A frigid beam of blue-white light streaks toward a creature within range. Make a ranged spell '
                        'attack against the target. On a hit, it takes 1d8 cold damage, and its speed is reduced by '
                        '10 feet until the start of your next turn.',

                        'The spell\'s damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and '
                        '17th level (4d8).'],
        'id': 0.18
    },
    'Resistant': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Abjuration',
        'castTime': '1 action',
        'range': 'Touch',
        'components': ['V', 'S', 'M'],
        'duration': 'Concentration, up to 1 minute',
        'classes': ['Artificer', 'Cleric', 'Druid'],
        'subclasses': [''],
        'description': ['You touch one willing creature. Once before the spell ends, the target can roll a d4 and add '
                        'the number rolled to one saving throw of its choice. It can roll the die before or after '
                        'making the saving throw. The spell then ends.'],
        'id': 0.19
    },
    'Sacred Flame': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Evocation',
        'castTime': '1 action',
        'range': '60 feet',
        'components': ['V', 'S'],
        'duration': 'Instantaneous',
        'classes': ['Cleric'],
        'subclasses': ['Sorcerer (Divine Soul)', 'Sorcerer (Lunar Sorcery)', 'Warlock (Celestial)'],
        'description': ['Flame-like radiance descends on a creature that you can see within range. The target must '
                        'succeed on a Dexterity saving throw or take 1d8 radiant damage. The target gains no benefit '
                        'from cover for this saving throw.',

                        'The spell\'s damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and '
                        '17th level (4d8).'],
        'id': 0.20
    },
    'Shillelagh': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Transmutation',
        'castTime': '1 bonus action',
        'range': 'Touch',
        'components': ['V', 'S', 'M (Mistletoe, a shamrock leaf, and a club or quarterstaff)'],
        'duration': '1 minute',
        'classes': ['Druid'],
        'subclasses': [''],
        'description': ['The wood of a club or quarterstaff you are holding is imbued with nature\'s power. For the '
                        'duration, you can use your spell casting ability instead of Strength for the attack and '
                        'damage rolls of melee attacks using that weapon, and the weapon\'s damage die becomes a d8. '
                        'The weapon also becomes magical, if it isn\'t already. The spell ends if you cast it again '
                        'or if you let go of the weapon.'],
        'id': 0.21
    },
    'Spare the Dying': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Necromancy',
        'castTime': '1 action',
        'range': 'Touch',
        'components': ['V', 'S'],
        'duration': 'Instantaneous',
        'classes': ['Artificer', 'Cleric'],
        'subclasses': [''],
        'description': ['You touch a living creature that has 0 hit points. The creature becomes stable. This spell '
                        'has no effect on undead or constructs'],
        'id': 0.22
    },
    'Shocking Grasp': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Evocation',
        'castTime': '1 action',
        'range': 'Touch',
        'components': ['V', 'S'],
        'duration': 'Instantaneous',
        'classes': ['Artificer', 'Fighter (Eldritch Knight)', 'Rouge (Arcane Trickster)', 'Sorcerer', 'Wizard'],
        'subclasses': [''],
        'description': ['Lightning springs from your hand to deliver a shock to a creature you try to touch. Make a '
                        'melee spell attack against the target. You have advantage on the attack roll if the target '
                        'is wearing armor made of metal. On a hit, the target takes 1d8 lightning damage, and it '
                        'can\'t take reactions until the start of its next turn.',

                        'The spell\'s damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and '
                        '17th level (4d8).'],
        'id': 0.23
    },
    'Thaumaturgy':{
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Transmutation',
        'castTime': '1 action',
        'range': '30 feet',
        'components': ['V'],
        'duration': 'Up to 1 minute',
        'classes': ['Ranger (Drakewarden)', 'Sorcerer (Divine Soul)'],
        'subclasses': [''],
        'description': ['You manifest a minor wonder, a sign of supernatural power, within range. You create one of '
                        ' the following magical effects within range: ',

                        '		- Your voice booms up to three times as loud as normal for 1 minute.',
                        '		- You cause flames to flicker, brighten, dim, or change color for 1 minute.',
                        '		- You cause harmless tremors in the ground for 1 minute.',
                        '		- You create an instantaneous sound that originates from a point of your choice within '
                        'range, such as a rumble of thunder, the cry of a raven, or ominous whispers.',

                        '		- You instantaneously cause an unlocked door or window to fly open or slam shut.',
                        '		- You alter the appearance of your eyes for 1 minute.',

                        'If you cast this spell multiple times, you can have up to three of its 1-minute effects '
                        'active at a time, and you can dismiss such an effect as an action.'],
        'id': 0.24
    },
    'Thorn Whip': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Transmutation',
        'castTime': '1 action',
        'range': '30 feet',
        'components': ['V', 'S', 'M (the stem of a plant with horns)'],
        'duration': 'Instantaneous',
        'classes': ['Artificer', 'Druid'],
        'subclasses': [''],
        'description': ['You create a long, vine-like whip covered in thorns that lashes out at your command toward a '
                        'creature in range. Make a melee spell attack against the target. If the attack hits, the '
                        'creature takes 1d6 piercing damage, and if the creature is Large or smaller, you pull the '
                        'creature up to 10 feet closer to you.',

                        'This spell\'s damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and '
                        '17th level (4d6).'],
        'id': 0.25
    },
    'True Strike': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Divination',
        'castTime': '1 action',
        'range': '30 feet',
        'components': ['S'],
        'duration': 'Concentration, up to 1 round',
        'classes': ['Bard', 'Fighter (Eldritch Knight)', 'Rouge (Arcane Trickster)', 'Sorcerer', 'Warlock', 'Wizard'],
        'subclasses': [''],
        'description': ['You extend your hand and point a finger at a target in range. Your magic grants you a brief '
                        'insight into the target\'s defenses. On your next turn, you gain advantage on your first '
                        'attack roll against the target, provided that this spell hasn\'t ended.'],
        'id': 0.26
    },
    'Vicious Mockery': {
        'source': 'Player\'s Handbook',
        'level': 0,
        'school': 'Enchantment',
        'castTime': '1 action',
        'range': '60 feet',
        'components': ['V'],
        'duration': 'Instantaneous',
        'classes': ['Bard'],
        'subclasses': [''],
        'description': ['You unleash a string of insults laced with subtle enchantments at a creature you can see '
                        'within range. If the target can hear you (though it need not understand you), it must '
                        'succeed on a Wisdom saving throw or take 1d4 psychic damage and have disadvantage on the '
                        'next attack roll it makes before the end of its next turn.',

                        'This spell\'s damage increases by 1d4 when you reach 5th level (2d4), 11th level (3d4), and '
                        '17th level (4d4).'],
        'id': 0.27
    },
}

first_level_spellbook = {
    'Absorb Elements': {
        'source': 'Xanathar\'s Guide to Everything',
        'level': 1,
        'school': 'Abjuration',
        'castTime': '1 reaction, which you can take when you take acid, cold, fire, lightning, or thunder damage',
        'range': 'Self',
        'components': ['S'],
        'duration': '1 round',
        'classes': ['Artificer', 'Druid', 'Fighter (Eldritch Knight)', 'Ranger', 'Rouge (Arcane Trickster)', 'Sorcerer', 'Wizard'],
        'subclasses': [''],
        'description': ['The spell captures some of the incoming energy, lessening its effect on you and storing it '
                        'for your next melee attack. You have resistance to the triggering damage type until the start '
                        'of your next turn. Also, the first time you hit with a melee attack on your next turn, the '
                        'target takes an extra 1d6 damage of the triggering type, and the spell ends.',

                        'At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, the '
                        'extra damage increases by 1d6 for each slot level above 1st.'],
        'id': 1.01  # .0 could be used for other books, like Xanathar's maybe??
    },
    'Alarm': {
        'source': 'Player\'s Handbook',
        'level': 1,
        'school': 'Abjuration',
        'ritual': True,
        'castTime': '1 minute',
        'range': '120 feet',
        'components': ['V', 'S', 'M (a tiny bell and a piece of fine silver wire)'],
        'duration': '8 hours',
        'classes': ['Artificer', 'Fighter (Eldritch Knight)', 'Ranger', 'Rouge (Arcane Trickster)', 'Wizard'],
        'subclasses': [''],
        'description': ['You set an alarm against unwanted intrusion. Choose a door, a window, or an area within range '
                        'that is no larger than a 20-foot cube. Until the spell ends, an alarm alerts you whenever a '
                        'Tiny or larger creature touches or enters the warded area. When you cast the spell, you can '
                        'designate creatures that won\'t set off the alarm. You also choose whether the alarm is '
                        'mental or audible.',

                        'A mental alarm alerts you with a ping in your mind if you are within 1 mile of the warded '
                        'area. This ping awakens you if you are sleeping.',

                        'An audible alarm produces the sound of a hand bell for 10 seconds within 60 feet.'],
        'id': 1.1  # notice the .1 as this is the first first-level spell from Player's Handbook. Is that a good system?
    },
    'Animal Friendship': {
        'source': 'Player\'s Handbook',
        'level': 1,
        'school': 'Enchantment',
        'castTime': '1 action',
        'range': '30 feet',
        'components': ['V', 'S', 'M (a morsel of food)'],
        'duration': '24 hours',
        'classes': ['Bard', 'Druid', 'Ranger'],
        'subclasses': ['Cleric (Nature)'],
        'description': ['This spell lets you convince a beast that you mean it no harm. Choose a beast that you can '
                        'see within range. It must see and hear you. If the beast\'s Intelligence is 4 or higher, the '
                        'spell fails. Otherwise, the beast must succeed on a Wisdom saving throw or be charmed by you '
                        'for the spell\'s duration. If you or one of your companions harms the target, the spell ends.',

                        'At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, you can '
                        'affect one additional beast for each slot level above 1st.'],
        'id': 1.2
    },
    # Agathys is spells correctly.
    'Armor or Agathys': {  
        'source': 'Player\'s Handbook',
        'level': 1,
        'school': 'Abjuration',
        'castTime': '1 action',
        'range': 'Self',
        'components': ['V', 'S', 'M (a cup of water)'],
        'duration': '1 hour',
        'classes': ['Warlock'],
        'subclasses': ['Paladin (Conquest)'],
        'description': ['A protective magical force surrounds you, manifesting as a spectral frost that covers you and '
                        'your gear. You gain 5 temporary hit points for the duration. If a creature hits you with a '
                        'melee attack while you have these hit points, the creature takes 5 cold damage.',

                        'At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, both the '
                        'temporary hit points and the cold damage increase by 5 for each slot level above 1st.'],
        'id': 1.3
    },
    'Arms of Hadar': {
        'source': 'Player\'s Handbook',
        'level': 1,
        'school': 'Conjuration',
        'castTime': '1 action',
        'range': 'Self (10-foot radius)',
        'components': ['V', 'S'],
        'duration': 'Instantaneous',
        'classes': ['Warlock'],
        'subclasses': ['Sorcerer (Aberrant Mind)'],
        'description': ['You invoke the power of Hadar, the Dark Hunger. Tendrils of dark energy erupt from you and '
                        'batter all creatures within 10 feet of you. Each creature in that area must make a Strength '
                        'saving throw. On a failed save, a target takes 2d6 necrotic damage and can\'t take reactions '
                        'until its next turn. On a successful save, the creature takes half damage, but suffers no '
                        'other effect.',
    
                        'At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, the '
                        'damage increases by 1d6 for each slot level above 1st.'],
        'id': 1.4
    },
    'Bane': {
        'source': 'Player\'s Handbook',
        'level': 1,
        'school': 'Enchantment',
        'castTime': '1 action',
        'range': '30 feet',
        'components': ['V', 'S', 'M (a drop of blood)'],
        'duration': 'Concentration, up to 1 minute',
        'classes': ['Bard', 'Cleric'],
        'subclasses': ['Cleric (Grave)', 'Paladin (Vengeance)', 'Sorcerer (Divine Soul)', 'Warlock (Undead)'],
        'description': ['Up to three creatures of your choice that you can see within range must make Charisma saving '
                        'throws. Whenever a target that fails this saving throw makes an attack roll or a saving throw '
                        'before the spell ends, the target must roll a d4 and subtract the number rolled from the '
                        'attack roll or saving throw.',
    
                        'At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, you can '
                        'target one additional creature for each slot level above 1st.'],
        'id': 1.5
    },
    'Bless': {
        'source': 'Player\'s Handbook',
        'level': 1,
        'school': 'Enchantment',
        'castTime': '1 action',
        'range': '30 feet',
        'components': ['V', 'S', 'M (a sprinkling of holy water)'],
        'duration': 'Concentration, up to 1 minute',
        'classes': ['Cleric', 'Paladin'],
        'subclasses': ['Cleric (Life)', 'Sorcerer (Divine Soul)'],
        'description': ['You bless up to three creatures of your choice within range. Whenever a target makes an '
                        'attack roll or a saving throw before the spell ends, the target can roll a d4 and add the '
                        'number rolled to the attack roll or saving throw.',
    
                        'At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, you can '
                        'target one additional creature for each slot level above 1st.'],
        'id': 1.6
    },
    'Burning Hands': {
        'source': 'Player\'s Handbook',
        'level': 1,
        'school': 'Evocation',
        'castTime': '1 action',
        'range': 'Self (15-foot cone)',
        'components': ['V', 'S'],
        'duration': 'Instantaneous',
        'classes': ['Fighter (Eldritch Knight)', 'Rouge (Arcane Trickster)', 'Sorcerer', 'Wizard'],
        'subclasses': ['Cleric (Light)', 'Druid (Wildfire)', 'Monk (Four Elements)', 'Monk (Sun Soul)',
                       'Warlock (Fiend)', 'Warlock (Genie - Efreeti)'],  #Efreeti is spelled correctly
        'description': ['As you hold your hands with thumbs touching and fingers spread, a thin sheet of flames shoots '
                        'forth from your outstretched fingertips. Each creature in a 15-foot cone must make a '
                        'Dexterity saving throw. A creature takes 3d6 fire damage on a failed save, or half as much '
                        'damage on a successful one.',
    
                        'The fire ignites any flammable objects in the area that aren\'t being worn or carried.',

                        'At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, the '
                        'damage increases by 1d6 for each slot level above 1st.'],
        'id': 1.7
    },
    'Charm Person': {
        'source': 'Player\'s Handbook',
        'level': 1,
        'school': 'Enchantment',
        'castTime': '1 action',
        'range': '30 feet',
        'components': ['V', 'S'],
        'duration': '1 hour',
        'classes': ['Bard', 'Druid', 'Fighter (Eldritch Knight)', 'Rogue (Arcane Trickster)', 'Sorcerer', 'Warlock',
                    'Wizard'],
        'subclasses': ['Cleric (Trickery)', 'Ranger (Fey Wanderer)'],
        'description': ['You attempt to charm a humanoid you can see within range. It must make a Wisdom saving throw, '
                        'and does so with advantage if you or your companions are fighting it. If it fails the saving '
                        'throw, it is charmed by you until the spell ends or until you or your companions do anything '
                        'harmful to it. The charmed creature regards you as a friendly acquaintance. When the spell '
                        'ends, the creature knows it was charmed by you.',

                        'At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, you '
                        'can target one additional creature for each slot level above 1st. The creatures must be '
                        'within 30 feet of each other when you target them.'],
        'id': 1.8
    },
    'Chromatic Orb': {
        'source': 'Player\'s Handbook',
        'level': 1,
        'school': 'Evocation',
        'castTime': '1 action',
        'range': '90 feet',
        'components': ['V', 'S', 'M (a diamond worth at least 50gp)'],
        'duration': 'Instantaneous',
        'classes': ['Fighter (Eldritch Knight)', 'Rogue (Arcane Trickster)', 'Sorcerer', 'Wizard'],
        'subclasses': [''],
        'description': ['You hurl a 4-inch-diameter sphere of energy at a creature that you can see within range. You'
                        ' choose acid, cold, fire, lightning, poison, or thunder for the type of orb you create, and '
                        'then make a ranged spell attack against the target. If the attack hits, the creature takes '
                        '3d8 damage of the type you chose.',

                        'At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, the '
                        'damage increases by 1d8 for each slot level above 1st.'],
        'id': 1.9
    },
    'Color Spray': {
        'source': 'Player\'s Handbook',
        'level': 1,
        'school': 'Illusion',
        'castTime': '1 action',
        'range': 'Self (15-foot cone)',
        'components': ['V', 'S', 'M (a pinch of powder or sand that is colored red, yellow, and blue)'],
        'duration': '1 round',
        'classes': ['Fighter (Eldritch Knight)', 'Rogue (Arcane Trickster)', 'Sorcerer', 'Wizard'],
        'subclasses': ['Sorcerer (Lunar Sorcery)'],
        'description': ['A dazzling array of flashing, colored light springs from your hand. Roll 6d10; the total is '
                        'how many hit points of creatures this spell can effect. Creatures in a 15-foot cone '
                        'originating from you are affected in ascending order of their current hit points (ignoring '
                        'unconscious creatures and creatures that can\'t see).',

                        'Starting with the creature that has the lowest current hit points, each creature affected by '
                        'this spell is blinded until the end of your next turn. Subtract each creature\'s hit points '
                        'from the total before moving on to the creature with the next lowest hit points. A creature\'s '
                        'hit points must be equal to or less than the remaining total for that creature to be affected.',

                        'At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, roll an '
                        'additional 2d10 for each slot level above 1st.'],
        'id': 1.10
    },
    'Command': {
        'source': 'Player\'s Handbook',
        'level': 1,
        'school': 'Enchantment',
        'castTime': '1 action',
        'range': '60 feet',
        'components': ['V'],
        'duration': '1 round',
        'classes': ['Cleric', 'Paladin'],
        'subclasses': ['Bard (Glamour)', 'Cleric (Knowledge)', 'Cleric (Order)', 'Paladin (Conquest)', 'Paladin (Crown)',
                       'Sorcerer (Divine Soul)', 'Warlock (Fiend)'],
        'description': ['You speak a one-word command to a creature you can see within range. The target must succeed '
                        'on a Wisdom saving throw or follow the command on its next turn. The spell has no effect if '
                        'the target is undead, if it doesn\'t understand your language, or if your command is directly '
                        'harmful to it.',

                        'Some typical commands and their effects follow. You might issue a command other than one '
                        'described here. If you do so, the DM determines how the target behaves. If the target can\'t '
                        'follow your command, the spell ends.',

                        '   - Approach: The target moves toward you by the shortest and most direct route, ending its '
                        'turn if it moves within 5 feet of you.',
                        '   - Drop: The target drops whatever it is holding and then ends its turn.',
                        '   - Flee: The target spends its turn moving away from you by the fastest available means.',
                        '   - Grovel: The target falls prone and then ends its turn.',
                        '   - Halt: The target doesn\'t move and takes no actions. A flying creature stays aloft, '
                        'provided that it is able to do so. If it must move to stay aloft, it flies the minimum '
                        'distance needed to remain in the air.',

                        'At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, you can '
                        'affect one additional creature for each slot level above 1st. The creatures must be within 30 '
                        'feet of each other when you target them.'],
        'id': 1.11
    },
    'Compelled Duel': {
            'source': 'Player\'s Handbook',
            'level': 1,
            'school': 'Enchantment',
            'castTime': '1 bonus action',
            'range': '30 feet',
            'components': ['V'],
            'duration': 'Concentration, up to 1 minute',
            'classes': ['Paladin'],
            'subclasses': ['Paladin (Crown)'],
            'description': ['You attempt to compel a creature into a duel. One creature that you can see within range '
                            'must make a Wisdom saving throw. On a failed save, the creature is drawn to you, compelled '
                            'by your divine demand. For the duration, it has disadvantage on attack rolls against '
                            'creatures other than you, and must make a Wisdom saving throw each time it attempts to '
                            'move to a space that is more than 30 feet away from you; if it succeeds on this saving '
                            'throw, this spell doesn\'t restrict the target\'s movement for that turn.',

                            'The spell ends if you attack any other creature, if you cast a spell that targets a '
                            'hostile creature other than the target, if a creature friendly to you damages the target '
                            'or casts a harmful spell on it, or if you end your turn more than 30 feet away from the '
                            'target.'],
            'id': 1.12
        },
    'Comprehend Languages': {
        'source': 'Player\'s Handbook',
        'level': 1,
        'school': 'Divination',
        'ritual': True,
        'castTime': '1 action',
        'range': 'Self',
        'components': ['V', 'S', 'M (a pinch of soot and salt)'],
        'duration': '1 hour',
        'classes': ['Bard', 'Fighter (Eldritch Knight)', 'Rogue (Arcane Trickster)', 'Sorcerer', 'Warlock', 'Wizard'],
        'subclasses': [''],
        'description': ['For the duration, you understand the literal meaning of any spoken language that you hear. '
                        'You also understand any written language that you see, but you must be touching the surface '
                        'on which the words are written. It takes about 1 minute to read one page of text.',

                        'This spell doesn\'t decode secret messages in a text or a glyph, such as an arcane sigil, '
                        'that isn\'t part of a written language.'],
        'id': 1.13
    },
    'Create or Destroy Water': {
        'source': 'Player\'s Handbook',
        'level': 1,
        'school': 'Transmutation',
        'castTime': '1 action',
        'range': '30 feet',
        'components': ['V', 'S', 'M (a drop of water if creating water or a few grains of sand if destroying it)'],
        'duration': 'Instantaneous',
        'classes': ['Cleric', 'Druid'],
        'subclasses': ['Sorcerer (Divine Soul)', 'Warlock (Fathomless)'],
        'description': ['You either create or destroy water.',

                        '   - Create Water: You create up to 10 gallons of clean water within range in an open'
                        ' container. Alternatively, the water falls as rain in a 30-foot cube within range, '
                        'extinguishing exposed flames in the area.',

                        '   - Destroy Water: You destroy up to 10 gallons of water in an open container within '
                        'range. Alternatively, you destroy fog in a 30-foot cube within range.',

                        'At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, you '
                        'create or destroy 10 additional gallons of water, or the size of the cube increases by 5 '
                        'feet, for each slot level above 1st.'],
        'id': 1.14
    },
    'Cure Wounds': {
        'source': 'Player\'s Handbook',
        'level': 1,
        'school': 'Evocation',
        'castTime': '1 action',
        'range': 'Touch',
        'components': ['V', 'S'],
        'duration': 'Instantaneous',
        'classes': ['Artificer', 'Bard', 'Cleric', 'Druid', 'Paladin', 'Ranger'],
        'subclasses': ['Cleric (Life)', 'Druid (Wildfire)', 'Sorcerer (Divine Soul)', 'Warlock (Celestial)'],
        'description': ['A creature you touch regains a number of hit points equal to 1d8 + your spellcasting '
                        'ability modifier. This spell has no effect on undead or constructs.',

                        'At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, the '
                        'healing increases by 1d8 for each slot level above 1st.'],
        'id': 1.15
    },
    'Detect Evil and Good': {
        'source': 'Player\'s Handbook',
        'level': 1,
        'school': 'Divination',
        'castTime': '1 action',
        'range': 'Self',
        'components': ['V', 'S'],
        'duration': 'Concentration, up to 10 minutes',
        'classes': ['Cleric', 'Paladin'],
        'subclasses': ['Sorcerer (Divine Soul)', 'Warlock (Genie- Djinni)', 'Warlock (Genie- Efreeti)',
                       'Warlock (Genie- Marid)'],
        'description': ['For the duration, you know if there is an aberration, celestial, elemental, fey, fiend, '
                        'or undead within 30 feet of you, as well as where the creature is located. Similarly, you '
                        'know if there is a place or object within 30 feet of you that has been magically '
                        'consecrated or desecrated.',

                        'The spell can penetrate most barriers, but it is blocked by 1 foot of stone, 1 inch of '
                        'common metal, a thin sheet of lead, or 3 feet of wood or dirt.'],
        'id': 1.16
    },
    'Detect Magic': {
        'source': 'Player\'s Handbook',
        'level': 1,
        'school': 'Divination',
        'ritual': True,
        'castTime': '1 action',
        'range': 'Self',
        'components': ['V', 'S'],
        'duration': 'Concentration, up to 10 minutes',
        'classes': ['Artificer', 'Bard', 'Cleric', 'Druid', 'Fighter (Eldritch Knight)', 'Paladin', 'Ranger',
                    'Rogue (Arcane Trickster)', 'Sorcerer', 'Wizard'],
        'subclasses': ['Cleric (Arcana)', 'Paladin (Watchers)', 'Sorcerer (Divine Soul)'],
        'description': ['For the duration, you sense the presence of magic within 30 feet of you. If you sense '
                        'magic in this way, you can use your action to see a faint aura around any visible '
                        'creature or object in the area that bears magic, and you learn its school of magic, if '
                        'any.',

                        'The spell can penetrate most barriers, but it is blocked by 1 foot of stone, 1 inch of '
                        'common metal, a thin sheet of lead, or 3 feet of wood or dirt.'],
        'id': 1.17
    }
}