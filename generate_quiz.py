#generate_quiz.py
# Generate 35 random quiz questions and answers
# save them to a text file and save answers also to another file

import random

# The quiz data
# state names are keys and the values are the capitals

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
   'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West'
   'Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# To generate 35 quiz and answers files

for quiznum in range(35):
	# open a quiz file
	quizfile = open("c:/users/wizzy/desktop/python projects/quiz35 project/quiz%s.txt" % str(quiznum+1), 'w')

	#create an answers file for the peculiar quiz questions

	answersfile = open("c:/users/wizzy/desktop/python projects/quiz35 project/answers/quiz%s_answer.txt" % str(quiznum+1), 'w')

	quizfile.write("CAPITALS QUIZ\n\nName:\nDate:\nPeriod:\n\n")
	quizfile.write(" " * 20 + "Type %s\n\n" % str(quiznum+1))	
	answersfile.write("QUIZ ANSWERS FOR QUIZ %s\n\n" % str(quiznum+1))
	
	states = list(capitals) # creating a list for the dictionary keys - the states

	random.shuffle(states) # list of shuffled dictionary keys. Shuffled states

	# to create unique questions and the options in each file

	for quizoption in range(50):
		correct_ans = capitals[states[quizoption]] # using the key returned by shuffled states to access capitals dict
		# to generate wrong answers. We want 4 options, 1 correct and 3 wrong
		capitals_values = list(capitals.values())
		capitals_values.remove(correct_ans) # To make sure the correct answer is not in the list that wrong answers will be 
												# selected from
		wrong_answers = random.sample(capitals_values, 3) # returns a list of 3 values selected randomly from capitals_values

		answers = wrong_answers + [correct_ans] # A list of our required 4 options

		# To make sure our correct answer is not always the fourth one

		random.shuffle(answers)

		quizfile.write('\n%s. What is the capital of %s?\n' % (str(quizoption + 1), states[quizoption]))
		# To write the random options
		options_str = 'ABCD'
		for i in range(4):
			quizfile.write(' %s. %s\n' % (options_str[i], answers[i]))
		              
		# write the correct answer to answersfile
		     
		answersfile.write("%s. %s\n" % (str(quizoption + 1), options_str[answers.index(correct_ans)]))
	quizfile.write("\nGOODLUCK!!!!")
	quizfile.close()
	answersfile.close()










