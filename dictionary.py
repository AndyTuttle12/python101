# zombie = {
# 	'speed':10,
# 	'power':6,
# 	'hunger':12,
# 	'name':'Zombo'
# }

# print zombie['speed'];

# zombie['weapon'] = 'Fist';
# zombie['startX'] = 200;
# zombie['startY'] = 100;
# print zombie;

# if zombie['speed'] <= 5:
# 	zombie['position'] = zombie['startX'] + 2;
# elif zombie['speed'] >= 10:
# 	zombie['position'] = zombie['startX'] + 4;
# else:
# 	zombie['position'] = zombie['startX'] + 6;

# zombie['pointless'] = 'duh';
# del zombie['pointless'];
# print zombie;

# tech_skills = {
# 	'html':110,
# 	'css':110,
# 	'js':110,
# 	'react':110,
# 	'sass':120,
# 	'node':110,
# 	'express':110,
# 	'socketio':100,
# 	'redux':110,
# 	'mysql':110,
# 	'git':110,
# 	'sketch':110,
# 	'python':100,
# 	'photoshop':100,
# 	'pug':100,
# 	'apache':100,
# 	'linux':100,
# 	'aws':100,
# 	'bootstrap':110,
# 	'jquery':110,
# 	'babel':110,
# 	'mongodb':110,
# 	'angular':90,
# 	'angular2':20,
# 	'postcss':80,
# 	'typescript':20,
# 	'vue':10,
# 	'java':0,
# 	'c#':0,
# 	'c':0,
# 	'c++':0
# }

# print 'I need to work on these: '
# for skill,value in tech_skills.items():
# 	if value < 100:
# 		print skill;
		


# for key in zombie:
# 	print zombie[key];

# zombies = [];
# zombies.append({
# 	'speed':5,
# 	'power':10,
# 	'hunger':8,
# 	'name':'Bill'
# })

# zombies.append({
# 	'speed':4,
# 	'power':16,
# 	'hunger': 20,
# 	'name':'Sven'
# })

# print zombies;
# print zombies[0];
# print zombies[0]['name'];
# for zombie in zombies:
# 	print zombie['name'];

# zombies[0]['victims'] = [{},'Rishi','Anna'];
# print zombies[0];

# zombies[0]['victims'][0]['name'] = 'Sean';
# print zombies[0];

# zombie[0]['super_mode'] = {
# 	# at night...
# 	'power': 23,
# 	'hunger': 20;
# 	'weapon': 'baseball_bat'
# }

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }

# # print phonebook_dict['Alice'];
# phonebook_dict['Kareem'] = '938-489-1234';
# del phonebook_dict['Alice'];
# phonebook_dict['Bob'] = '968-345-2345';
# print phonebook_dict;

# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }

# print ramit['email'];
# print ramit['interests'][0];
# print ramit['friends'][0]['email'];
# print ramit['friends'][1]['interests'][1];

# def letter_histogram(word):
# 	letters = {};
# 	for letter in word:
# 		letter_count = word.count(letter);
# 		letters[letter] = letter_count;
# 	print letters;

# letter_histogram('banana');

# def word_histogram(phrase):
# 	words = {};
# 	phrase = phrase.lower().split(' ');
# 	for word in phrase:
# 		word_count = phrase.count(word);
# 		words[word] = word_count;
# 	print words;

# word_histogram('To be or not to be');