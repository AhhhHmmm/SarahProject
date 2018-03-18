import csv

def getAnswers(filename):
	answers = []
	with open(filename) as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',')
		for row in csvreader:
			answers.append(int(row[1]))
	return answers

answers = getAnswers('CR.csv')

# Sarah, the lines of text above here open up the answer document.
# It reads each line and then adds only the answer (not the question) number
# to a list called answers.
# I've printed out the answer list below so that you can see what it looks like.
# The values in the list are already of type int.
# Please do not change any code above this line, but can you fill in the rest so that it scores
# the result for all categories instead of just printing out the answers?

# print(answers)

###Below is first version
### 1. Emotional Deprivation 1-9
# emotionalDeprivationAnswers = answers[0:9]
# print(emotionalDeprivationAnswers)

# resultsEmotionalDeprivation = {'4s': 0, '5s': 0, '6s' : 0}

# for answer in emotionalDeprivationAnswers:
# 	if answer == 4:
# 		resultsEmotionalDeprivation['4s'] = resultsEmotionalDeprivation['4s'] + 1
# 	elif answer == 5:
# 		resultsEmotionalDeprivation['5s'] = resultsEmotionalDeprivation['5s'] + 1
# 	elif answer == 6:
# 		resultsEmotionalDeprivation['6s'] = resultsEmotionalDeprivation['6s'] + 1

# print('4s:' + str(resultsEmotionalDeprivation['4s']))
# print('5s:' + str(resultsEmotionalDeprivation['5s']))
# print('6s:' + str(resultsEmotionalDeprivation['6s']))

# emotionalDeprivationScore = ((resultsEmotionalDeprivation['4s'] * 4) + (resultsEmotionalDeprivation['5s'] * 5) + (resultsEmotionalDeprivation['6s'] * 6))

# print('Total Emotional Deprivation Score: ' + str(emotionalDeprivationScore))

# if emotionalDeprivationScore in range(0,9):
# 	print('score = low')
# elif emotionalDeprivationScore in range(9,19):
# 	print('score = medium')
# elif emotionalDeprivationScore in range(19,31):
# 	print('score = high')
# elif emotionalDeprivationScore in range(31,55):
# 	print('score = very high')



####FUNCTION FOR ALL###

def scoreSchema(schemaName,startQuestion,endQuestion,lowRangeCut, mediumRangeCut, highRangeCut, veryHighRangeCut):	
	# use the values from the pdf brainlessly
	startIndex = startQuestion - 1
	endIndex = endQuestion

	schemaAnswers = answers[startIndex:endIndex]
	#print(schemaAnswers)

	resultsSchema = {'4s': 0, '5s': 0, '6s' : 0}

	for answer in schemaAnswers:
		if answer == 4:
			resultsSchema['4s'] = resultsSchema['4s'] + 1
		elif answer == 5:
			resultsSchema['5s'] = resultsSchema['5s'] + 1
		elif answer == 6:
			resultsSchema['6s'] = resultsSchema['6s'] + 1

	# print('4s:' + str(resultsSchema['4s']))
	# print('5s:' + str(resultsSchema['5s']))
	# print('6s:' + str(resultsSchema['6s']))

	schemaScore = ((resultsSchema['4s'] * 4) + (resultsSchema['5s'] * 5) + (resultsSchema['6s'] * 6))

	print('Total {} Score: {}'.format(schemaName, schemaScore))

	# The '+ 1' below are included so that we don't have to be smart about matching values
	# in the table to values for the ranges
	if schemaScore in range(0,lowRangeCut + 1):
		print('score = low')
	elif schemaScore in range(lowRangeCut + 1, mediumRangeCut + 1):
		print('score = medium')
	elif schemaScore in range(mediumRangeCut + 1, highRangeCut + 1):
		print('score = high')
	elif schemaScore in range(highRangeCut + 1,veryHighRangeCut + 1):
		print('score = very high')

	print('-'*67)

#1. Emotional Deprivation 1-9
scoreSchema('Emotional Deprivation', 1, 9, 8, 18, 30, 60)

# Abandonment 10-26
scoreSchema('Abandonment', 10, 26, 12, 25, 39, 102)

# Mistrust/Abuse 27-43
scoreSchema('Mistrust/Abuse', 27, 43, 12, 25, 39, 102)

# Social Isolation 44-53
scoreSchema('Social Isolation', 44, 53, 8, 18, 30, 60)

# Defectiveness 54-68
scoreSchema('Defectiveness', 54, 68, 12, 25, 39, 90)

# Failure 69-77
scoreSchema('Failure', 69, 77, 8, 18, 30, 54)

# Dependence 78-92
scoreSchema('Dependence', 78, 92, 12, 25, 39, 90)

# Vulnerablity 93-104
scoreSchema('Vulnerablity', 93, 104, 8, 18, 30, 72)

# Enmeshment 105-115
scoreSchema('Enmeshment', 105, 115, 8, 18 , 30, 66)
# Subjugation 116-125
scoreSchema('Subjugation', 116, 125, 8, 19, 30, 60)

# Self-Sacrifice 126-142
scoreSchema('Self-Sacrifice', 126, 142, 12, 25, 39, 102)

# Emotional Inhibition 143-151
scoreSchema('Emotional Inhibition', 143, 151, 8, 18, 30, 54)

# Unrelenting Standards 152-167
scoreSchema('Unrelenting Standards', 152, 167, 12, 25, 39, 96)

# Entitlement 168-178
scoreSchema('Entitlement', 168, 178, 8, 18, 30, 66)

# Insufficient Self-Control 179-193
scoreSchema('Insufficient Self-Control', 179, 193, 12, 25, 39, 90)

# Approval Seeking 194-207
scoreSchema('Approval Seeking', 194, 207, 12, 25, 39, 84)

# Negativity/Pessimism 208-218
scoreSchema('Negativity/Pessimism', 208, 218, 8, 18, 30, 66)

# Punitiveness 219-232
scoreSchema('Punitiveness', 219, 232, 12, 25, 39, 84)
