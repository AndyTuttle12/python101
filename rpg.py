from rpg_hero import Hero;
from rpg_opening import hero;
from rpg_monsters import Bokoblin, Moblin, Lizalfos;
from rpg_art import Banner;
from rpg_item import Item;
import time;
import rpg_opening;
# import pyglet;

# music = pyglet.resource.media('zelda_medley.mp3');
# music.play();

# pyglet.app.run();

rpg_opening;
enemies = [Bokoblin(),Moblin(),Lizalfos()];
hero = Hero();
for enemy in enemies:
	# print vars(enemy);
	# while hero.health > 0 and enemy.health > 0:
	print ""
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
		print "-- GAME OVER --";
		time.sleep(2.8);
		exit();

print ""
time.sleep(1);
print ""
time.sleep(1);
print ""
time.sleep(1);
print "Hey there Mr. fairy! Welcome to the item shop!";
print ""
time.sleep(1);

while hero.is_shopping():
	print "Take a look around and buy something, why don't ya?";
	print ""
	time.sleep(.8);
	print "< Press a number to purchase an item. Press [0] to leave. >";
	print ""
	time.sleep(.8);
	print "1. Deku Seeds -- 10 R";
	print ""
	time.sleep(.2);
	print "2. Health Potion -- 20 R";
	print ""
	time.sleep(.2);
	print "3. Deku Stick -- 30 R";
	print ""
	time.sleep(.2);
	print "4. Sling Shot -- 100 R";
	print ""
	time.sleep(.2);
	print "5. Deku Shield -- 200 R";
	print ""
	time.sleep(.2);
	print ">";
	input = int(raw_input());
	if input == 1:
		hero.get_item(Item('Deku Seeds', '10'));
	if input == 2:
		hero.get_item(Item('Health Potion', '20'));
	if input == 3:
		hero.get_item(Item('Deku Stick', '30'));
	if input == 4:
		hero.get_item(Item('Sling Shot', '100'));
	if input == 5:
		hero.get_item(Item('Deku Shield', '200'));
	if input == 0:
		print "See ya later then!";
		print ""
		print ""
		print ""
		time.sleep(1);
		break;