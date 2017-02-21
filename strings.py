# str = "i am in code schOOl.";
# print str.upper();

# print str.capitalize();

# print str[::-1];

# word = raw_input("submit a word to convert: ").upper();
# leet_chars = {'A':'4','E':'3','G':'6','I':'1','O':'0','S':'5','T':'7'};
# leet_word = '';
# for i in range(0,len(word)):
# 	if word[i] in leet_chars:
# 		leet_word+=leet_chars[''+word[i]+''];
# 	else:
# 		leet_word+=word[i];
# print leet_word;


# word = raw_input("say a long vowel word: ");
# vowels = ['a','A','e','E','i','I','o','O','u','U'];
# long_word = '';
# for i in range(0,len(word)):
# 	if word[i] in vowels:
# 		if word[i+1] in vowels:
# 			long_word += word[i] * 5;
# 		else:
# 			long_word += word[i];
# 	elif word[i] not in vowels:
# 		long_word += word[i];
# 	else: 
# 		print 'undefined';
# print long_word;

