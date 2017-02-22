from rpg_hero import Hero;
from rpg_monsters import Bokoblin, Moblin, Lizalfos;
from rpg_art import Banner;
import time;

hero = Hero();
enemies = [Bokoblin(),Moblin(),Lizalfos()];

print Banner;
time.sleep(2.8);

hero.name = raw_input("Greetings traveler! What is your name? ");
region = raw_input("And from where do you hail? ");

print 'Welcome brave %s, to a to a land of galantry and fearsome foes! ' % hero.name;
print ""
time.sleep(1.5);
print "You must travel to Hyrule castle in order to stop a great evil that has taken over all of Hyrule.";
print ""
time.sleep(1.5);
print "The evil has spread across the land and is even in this very forest.";
print ""
time.sleep(1.5);
print "In order to defeat this evil, you must find the powers left by the Goddesses and cleanse this land!";
print ""
time.sleep(1.5);
print "But before you leave to find the legends of the past to vanquish the darkness of the hour, you must be vigilant!";
print ""
if hero.name is "Andy":
	time.sleep(1.5);
	print "You must be VERY CAREFUL, Andy!";
	print ""
time.sleep(1.5);
print "It's dangerous to go alone. Here, take this!";
print ""
time.sleep(3.5);
print "< You recieve the [HERO'S SWORD] and [DEKU SHIELD]! >";
print ""
time.sleep(3.5);
print "Farewell and good luck in your adventures!";
print ""
time.sleep(1.5);
print ""
time.sleep(1.5);
print ""
time.sleep(1.5);

print "< FARON WOODS >";
print ""
time.sleep(1.5);
print ""
time.sleep(1.5);
print "You are traveling down the path when you hear something up ahead...";
print ""
time.sleep(1.5);


for enemy in enemies:
	# print vars(enemy);
	# while hero.health > 0 and enemy.health > 0:
	\
	print "A %s has appeared and starts to attack you!" % enemy.name;
	print ""
	time.sleep(1.5);
	while hero.is_alive() and enemy.is_alive():
		time.sleep(.8);
		print "What will you do? ";
		print ""
		time.sleep(.2);
		print "1. Fight %s" % enemy.name;
		time.sleep(.2);
		print "2. Run Away";
		print ""
		time.sleep(.2);
		print "> ",
		input = int(raw_input());
		if input == 1:
			# print hero.lucky();
			# enemy.health -= hero.power;
			hero.attack(enemy);
		elif input == 2:
			if hero.is_alive() and enemy.is_alive():
				break;
		else:
			print "Invalid choice %r" % input;
			print ""
		if enemy.is_alive():
			# hero.health -= enemy.power;
			enemy.attack(hero);
	if hero.is_alive() and enemy.is_alive():
		print "You have run away... You cowardly go home to your village.";
		print ""
		time.sleep(.8);
	elif hero.is_alive():
		print "You won! the %s is defeated!" % enemy.name;
		print ""
		time.sleep(.8);
	else:
		print "You were defeated by the vicious %s." % enemy.name;
		print ""
		time.sleep(.8);

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
