import time;

class Hero(object):
	def __init__(self):
		self.name = 'Link';
		self.health = 10;
		self.power = 5;
	def is_alive(self):
		return self.health > 0;
	def attack(self, enemy):
		print "%s attacks %s" % (self.name, enemy.name);
		enemy.take_damage(self.power);
		time.sleep(1.5);
		print "%s has done %d damage to %s" % (self.name, self.power, enemy.name);
	def take_damage(self, points_of_damage):
		self.health -= points_of_damage;

