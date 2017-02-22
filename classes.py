class Person(object):
    def __init__(self, name, email, phone, friends, greeting_count):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
    	self.greeting_count += 1;
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
    def print_contact_info(self):
    	print "%s's email: %s, %s's phone number: %s" % (self.name, self.email, self.name, self.phone);
    def add_friend(self, other_person):
    	self.friends.append(other_person);
    def num_friends(self):
    	print len(self.friends);
    def __repr__(self):
    	return '%r %r %r %r %r' % (self.name, self.email, self.phone, self.friends, self.greeting_count)

sonny = Person('Sonny','sonny@hotmail.com','483-485-4948', [], 0);

jordan = Person('Jordan','jordan@aol.com','495-586-3456', [], 0);

sonny.print_contact_info();

# jordan.friends.append(sonny);
# sonny.friends.append(jordan);
jordan.add_friend(sonny);
jordan.num_friends();

sonny.greet(jordan);
jordan.greet(sonny);

print sonny.greeting_count;
print jordan;
# print vars(sonny);
# print vars(jordan);

# class Vehicle(object):
# 	def __init__(self, make, model, year):
# 		self.make = make;
# 		self.model = model;
# 		self.year = year;
# 	def print_info(self):
# 		print self.year, self.make, self.model;

# car = Vehicle('Nissan', 'Leaf', 2015);
# car.print_info();