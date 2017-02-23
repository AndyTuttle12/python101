from rpg_hero import Hero;
from rpg_art import Banner;
import time;
import os;
os.system("afplay zelda_medley.mp3 &");

print Banner;
time.sleep(2.8);

hero = Hero();
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
time.sleep(1.5);
print "You must be VERY CAREFUL, %s!" % hero.name;
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
