

class Character:
    def __init__(self):
        # print('Constructor of Character class executing')
        self.name = None
        self.race = None
        self.class_name = None
        self.hp = None
        self.ac = None
        self.initiative = None
        self.speed = None
        self.vision = None
        self.size = None
        self.languages = None
        self.r_traits = None
        self.subr_traits = None
        self.combat_prof = None
        self.tool_prof = None
        self.hdie = None
        self.str = None
        self.dex = None
        self.con = None
        self.inte = None
        self.wis = None
        self.cha = None
        print(self.__dict__)

    def set_name(self, name):
        self.name = name
        
    def set_race(self, race):
        self.race = race
        
    def set_class(self, class_name):
        self.class_name = class_name
        
    def set_hp(self, hp):
        self.hp = hp
        
    def set_ac(self, ac):
        self.ac = ac
    
    def set_initiative(self, initiative):
        self.initiative = initiative
        
    def set_speed(self, speed):
        self.speed = speed

    def set_vision(self, vision):
        self.vision = vision

    def set_size(self, size):
        self.size = size

    def set_languages(self, languages):
        self.languages = languages

    def set_r_traits(self, r_traits):
        self.r_traits = r_traits

    def set_subr_traits(self, subr_traits):
        self.subr_traits = subr_traits

    def set_combat_prof(self, combat_prof):
        self.combat_prof = combat_prof

    def set_tool_prof(self, tool_prof):
        self.tool_prof = tool_prof

    def set_hdie(self, hdie):
        self.hdie = hdie

    def set_str(self, str):
        self.str = str

    def set_dex(self, dex):
        self.dex = dex

    def set_con(self, con):
        self.con = con

    def set_inte(self, inte):
        self.inte = inte

    def set_wis(self, wis):
        self.wis = wis

    def set_cha(self, cha):
        self.cha = cha