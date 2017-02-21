# # TUPLES!! IMMUTIBLE AND FUNCTIONAL

# a_tuple = (1,3,8)
# print a_tuple;
# print a_tuple[2];

# # loop like lists, just no assignment
# for number in a_tuple:
# 	print number;


# teams = ('falcons','hawks','atl_united','silverbacks','braves');
# for team in teams:
# 	if team == 'hawks':
# 		print 'Go Hawks';
# 	else:
# 		print "It's basketball season"


# team_a = 'Falcons';
# print team_a == 'Falcons';

# team_b = "Braves";
# cond1 = team_a == "Falcons"
# cond2 = team_b == "Braves"
# if cond1 and cond2:
# 	print 'Go ATL'

# # indexof in Pythons is just in
# print 'hawks' in teams;

# for team in teams:
# 	if team == 'hawks':
# 		print 'Go Hawks!';
# 	elif team == 'falcons':
# 		print 'Sad Super Bowl'

# if 'hawks' in teams:
# 	print 'Go Hawks';
# elif 'falcons' in teams:
# 	print "Falcons get it right..."

# height = raw_input("How tall are you?\n");
# if(int(height) >= 42):
# 	print "High enough for the roller coaster.";
# else:
# 	print "Maybe try the kiddie ride.";

# current = 1;
# while(current , 10):
# 	print current;
# 	current+=1;

answer = 'play';
game = true;
while answer != "quit":
	game = true;
user = upper(raw_input("A wizard approaches and says you are needed and must join him in the Battle of Dragon Island. What do you do? JOIN him, RUN away, or ask WHY ME","Choose one: JOIN, RUN, WHY ME"));


switch(user) {
	case 'JOIN':
	 	var wand = prompt("How brave! Did you bring your wand?").toUpperCase();
	 	var risk = prompt("Are you willing to risk your life to save the world?").toUpperCase();
	 	if(wand === 'YES' && risk === 'YES') {
	 		console.log("The wizard says: 'Hurry! There's no time to lose. We need your powers to defeat the schlerberglers.'");
	 	} else {
	 		console.log("Well then you are of no use to us!");
	 	}
	 	break;
 	case 'RUN':
 		var fast = prompt("GTFO! Are you like super fast (YES or NO)?").toUpperCase();
 		var invisible = prompt("Do you have an invisibility cloak you can hide under?").toUpperCase();
 		if(fast === 'YES' || invisible === 'YES') {
 			console.log("You get away, and the wizard shouts: 'You fool! It will be your fault the schlerberglers take over the world!'");
 		} else {
 			console.log("The wizard scoops you up over his shoulder, runs off and says: 'You're not escaping this. You WILL help us.'")
 		}
 		break;
 	case 'WHY ME':
 		console.log("The wizard says: 'Don't you know? You have special powers that can defeat terrible monsters, like the schlerberglers that are taking over Dragon Island!'");
 		break;
 	default:
 		console.log("You must select one of the following responses: JOIN, RUN, WHY ME");
}