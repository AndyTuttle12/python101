import time;
from random import randint;

class Character(object):
	# def __init__(self):
		# self.name = name;
		# self.health = health;
		# self.hit_points = hit_points;
		# self.power = power;
		# self.luck = luck;
		# self.damage_roll = damage_roll;
		# self.armor = armor;
		# self.armor_durability = armor_durability;
	def is_alive(self):
		return self.health > 0;
	def has_armor(self):
		return self.armor_durability > 0;
	def lucky(self):
		return self.luck * randint(0,1);

class Monster(Character):
	def __init__(self):
		Character.__init__(self);
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
