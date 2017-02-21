full_name = "Andy Tuttle";
age = 26;

my_array = [];
my_array.append(full_name);
my_array.append(age);
print my_array;

def say_hello():
	print "Hello!"
say_hello();

split_name = full_name.split(' ');
print split_name;

def say_name():
	print "Hello, " + split_name[0];
say_name();

def my_age(year):
	print 2017 - year;
my_age(1990);

def sum_odd_numbers():
	sum = 0;
	for i in range(1, 5001):
		if i % 2 == 1:
			sum += i
	print sum;
sum_odd_numbers();