from rpg_hero import Hero;
from rpg_monsters import Bokoblin;
from rpg_art import Banner;

hero = Hero();
enemies = [Bokoblin()];

print Banner;

for enemy in enemies:
	# print vars(enemy);
	# while hero.health > 0 and enemy.health > 0:
	while hero.is_alive() and enemy.is_alive():
		print "What will you do? ";
		print "1. Fight %s" % enemy.name;
		print "2. Run Away";
		print "> ",
		input = int(raw_input());
		if input == 1:
			# enemy.health -= hero.power;
			hero.attack(enemy);
		elif input == 2:
			break;
		else:
			print "Invalid choice %r" % input;
		if enemy.is_alive():
			# hero.health -= enemy.power;
			enemy.attack(hero);
	if hero.is_alive():
		print "You won! the %s is defeated!" % enemy.name;
	else:
		print "You were defeated by the vicious %s." % enemy.name;

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
# def main():
# 	hero_health = 10
# 	hero_power = 5
# 	goblin_health = 6
# 	goblin_power = 2

# 	while goblin_health > 0 and hero_health > 0:
# 		print "You have %d health and %d power." % (hero_health, hero_power)
# 		print "The goblin has %d health and %d power." % (goblin_health, goblin_power)
# 		print "What do you want to do?"
# 		print "1. fight goblin"
# 		print "2. do nothing"
# 		print "3. flee"
# 		print "> ",
# 		input = raw_input()
# 		if input == "1":
# 			# Hero attacks goblin
# 			goblin_health -= hero_power
# 			print "You do %d damage to the goblin." % hero_power
# 			if goblin_health <= 0:
# 				print "The goblin is dead."
# 		elif input == "2":
# 			pass
# 		elif input == "3":
# 			print "Goodbye."
# 			break
# 		else:
# 			print "Invalid input %r" % input

# 		if goblin_health > 0:
# 			# Goblin attacks hero
# 			hero_health -= goblin_power
# 			print "The goblin does %d damage to you." % goblin_power
# 			if hero_health <= 0:
# 				print "You are dead."

# main()
