from zombie import Zombie
import hero

zombie_object = Zombie(6,8,10,'bat',15);
# print vars(zombie_object);

heroObject = hero.Hero();
print vars(heroObject);

hero.cheer_hero(heroObject);