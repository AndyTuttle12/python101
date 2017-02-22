import time;
from random import randint;

class Bokoblin(object):
	def __init__(self):
		self.name = "bokoblin";
		self.health = 6;
		self.hit_points = 0;
		self.power = 2;
		self.luck = 3;
		self.damage_roll = 0;
		self.armor = 2;
		self.armor_durability = 3;
	def is_alive(self):
		return self.health > 0;
	def has_armor(self):
		return self.armor_durability > 0;
	def attack(self, hero):
		if self.lucky() > 2:
			print "%s attacks %s" % (self.name, hero.name);
			print ""
			self.damage_roll = self.power+self.lucky();
			hero.take_damage(self.damage_roll);
			time.sleep(1.5);
			print "%s has done %d damage to %s" % (self.name, self.damage_roll, hero.name);
			print ""
			print "%s's Health: %s | %s's Health: %s" % (hero.name, hero.health, self.name, self.hit_points);
			print ""
			time.sleep(.3);
		else:
			print "%s takes a wild swing and misses you completely." % self.name;
			print ""
			print "%s's Health: %s | %s's Health: %s" % (hero.name, hero.health, self.name, self.hit_points);
			print ""
			time.sleep(1.5);
	def take_damage(self, points_of_damage):
		if self.has_armor():
			self.armor_durability -= points_of_damage;
			self.hit_points = self.health + self.armor;
			self.hit_points -= points_of_damage;
			self.health = self.hit_points;
		else:
			self.health -= points_of_damage;
	def lucky(self):
		return self.luck * randint(0,1);

class Moblin(object):
	def __init__(self):
		self.name = "moblin";
		self.health = 7;
		self.hit_points = 0;
		self.power = 4;
		self.luck = 2;
		self.damage_roll = 0;
		self.armor = 3;
		self.armor_durability = 4;
	def is_alive(self):
		return self.health > 0;
	def has_armor(self):
		return self.armor_durability > 0;
	def attack(self, hero):
		if self.lucky() > 2:
			print "%s attacks %s" % (self.name, hero.name);
			print ""
			self.damage_roll = self.power+self.lucky();
			hero.take_damage(self.damage_roll);
			time.sleep(1.5);
			print "%s has done %d damage to %s" % (self.name, self.damage_roll, hero.name);
			print ""
			print "%s's Health: %s | %s's Health: %s" % (hero.name, hero.health, self.name, self.hit_points);
			print ""
			time.sleep(.3);
		else:
			print "%s takes a wild swing and misses you completely." % self.name;
			print ""
			print "%s's Health: %s | %s's Health: %s" % (hero.name, hero.health, self.name, self.hit_points);
			print ""
			time.sleep(1.5);
	def take_damage(self, points_of_damage):
		if self.has_armor():
			self.armor_durability -= points_of_damage;
			self.hit_points = self.health + self.armor;
			self.hit_points -= points_of_damage;
			self.health = self.hit_points;
		else:
			self.health -= points_of_damage;
	def lucky(self):
		return self.luck * randint(0,1);

class Lizalfos(object):
	def __init__(self):
		self.name = "lizalfos";
		self.health = 8;
		self.hit_points = 0;
		self.power = 5;
		self.luck = 6;
		self.damage_roll = 0;
		self.armor = 1;
		self.armor_durability = 6;
	def is_alive(self):
		return self.health > 0;
	def has_armor(self):
		return self.armor_durability > 0;
	def attack(self, hero):
		if self.lucky() > 2:
			print "%s attacks %s" % (self.name, hero.name);
			print ""
			self.damage_roll = self.power+self.lucky();
			hero.take_damage(self.damage_roll);
			time.sleep(1.5);
			print "%s has done %d damage to %s" % (self.name, self.damage_roll, hero.name);
			print ""
			print "%s's Health: %s | %s's Health: %s" % (hero.name, hero.health, self.name, self.hit_points);
			print ""
			time.sleep(.3);
		else:
			print "%s takes a wild swing and misses you completely." % self.name;
			print ""
			print "%s's Health: %s | %s's Health: %s" % (hero.name, hero.health, self.name, self.hit_points);
			print ""
			time.sleep(1.5);
	def take_damage(self, points_of_damage):
		if self.has_armor():
			self.armor_durability -= points_of_damage;
			self.hit_points = self.health + self.armor;
			self.hit_points -= points_of_damage;
			self.health = self.hit_points;
		else:
			self.health -= points_of_damage;
	def lucky(self):
		return self.luck * randint(0,1);