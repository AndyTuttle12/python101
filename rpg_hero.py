import time;
from random import randint;
from rpg_character import Character;

class Hero(Character):
	def __init__(self):
		Character.__init__(self);
		self.name = 'Link';
		self.health = 20;
		self.power = 8;
		self.luck = 7;
		self.damage_roll = 0;
		self.armor = 9;
		self.armor_durability = 5;
	def attack(self, enemy):
		if self.lucky() > 2:
			print "%s attacks %s" % (self.name, enemy.name);
			print ""
			self.damage_roll = self.power+self.lucky();
			enemy.take_damage(self.damage_roll);
			time.sleep(1.5);
			print "%s has done %d damage to %s" % (self.name, self.damage_roll, enemy.name);
			print ""
			print "%s's Health: %s | %s's Health: %s" % (self.name, self.health, enemy.name, enemy.health);
			print ""
			time.sleep(1.5);
		else:
			print "You take a wild swing and miss %s completely." % enemy.name;
			print ""
			print "%s's Health: %s | %s's Health: %s" % (self.name, self.health, enemy.name, enemy.health);
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
	def get_item(self, item):
		print "You purchased %s for %s rupees!" % (item.name, item.price)
		print ""
	def is_shopping(self):
		return self;

