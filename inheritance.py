class Animal(object):
	def __init__(self, name, species):
		self.name = name;
		self.species = species;
	def speak(self):
		print self.name + " is making a noise.";
	def run(self):
		print self.name + " is running.";

animal1 = Animal("Mitzie","Alien");
animal1.speak();
animal1.run();


class Dog(Animal):
	def __init__(self, dogName):
		Animal.__init__(self, dogName, "Dog");
		print self.name;
	def bark(self):
		print self.name + " is barking.";

dog = Dog('Fido');
dog.bark();
print dog.species;

