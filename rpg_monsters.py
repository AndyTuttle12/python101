from rpg_character import Monster;

class Bokoblin(Monster):
	def __init__(self):
		Monster.__init__(self);
		self.name = "bokoblin";
		self.health = 6;
		self.hit_points = 0;
		self.power = 2;
		self.luck = 6;
		self.damage_roll = 0;
		self.armor = 2;
		self.armor_durability = 3;

class Moblin(Monster):
	def __init__(self):
		Monster.__init__(self);
		self.name = "moblin";
		self.health = 7;
		self.hit_points = 0;
		self.power = 4;
		self.luck = 4;
		self.damage_roll = 0;
		self.armor = 3;
		self.armor_durability = 4;

class Lizalfos(Monster):
	def __init__(self):
		Monster.__init__(self);
		self.name = "lizalfos";
		self.health = 8;
		self.hit_points = 0;
		self.power = 5;
		self.luck = 8;
		self.damage_roll = 0;
		self.armor = 1;
		self.armor_durability = 6;