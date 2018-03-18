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

print(answers)

scaleDictionary = {
	'Emotional Deprivation' : {'low' : 8, 'medium' : 18, 'high' : 0}
}

def getScoreDictionary(answers):
	scoreDictionary = {
		'Emotional Deprivation' : 0,
		'Abandonment' : 0,
		'Mistrust/Abuse' : 0,
		'Social Isolation' : 0,
		'Defectiveness' : 0,
		'Failure' : 0,
		'Dependence' : 0,
		'Vulnerability' : 0,
		'Enmeshment' : 0,
		'Subjugation' : 0,
		'Self-Sacrifice' : 0,
		'Emotional Inhibition' : 0,
		'Unrelenting Standards' : 0,
		'Entitlement' : 0,
		'Insufficient Self-Control' : 0,
		'Approval-Seeking' : 0,
		'Negativity/Pessimism' : 0,
		'Punitiveness' : 0,
	}
	for index, answer in enumerate(answers):
		questionNumber = index + 1
		if questionNumber <= 9 and answer > 3:
			scoreDictionary['Emotional Deprivation'] += answer
		elif questionNumber <= 26 and answer > 3:
			scoreDictionary['Abandonment'] += answer
		elif questionNumber <= 43 and answer > 3:
			scoreDictionary['Mistrust/Abuse'] += answer
		elif questionNumber <= 53 and answer > 3:
			scoreDictionary['Social Isolation'] += answer
		elif questionNumber <= 68 and answer > 3:
			scoreDictionary['Defectiveness'] += answer
		elif questionNumber <= 77 and answer > 3:
			scoreDictionary['Failure'] += answer
		elif questionNumber <= 92 and answer > 3:
			scoreDictionary['Dependence'] += answer
		elif questionNumber <= 104 and answer > 3:
			scoreDictionary['Vulnerability'] += answer
		elif questionNumber <= 115 and answer > 3:
			scoreDictionary['Enmeshment'] += answer
		elif questionNumber <= 125 and answer > 3:
			scoreDictionary['Subjugation'] += answer
		elif questionNumber <= 142 and answer > 3:
			scoreDictionary['Self-Sacrifice'] += answer
		elif questionNumber <= 151 and answer > 3:
			scoreDictionary['Emotional Inhibition'] += answer
		elif questionNumber <= 167 and answer > 3:
			scoreDictionary['Unrelenting Standards'] += answer
		elif questionNumber <= 178 and answer > 3:
			scoreDictionary['Entitlement'] += answer
		elif questionNumber <= 193 and answer > 3:
			scoreDictionary['Insufficient Self-Control'] += answer
		elif questionNumber <= 207 and answer > 3:
			scoreDictionary['Approval-Seeking'] += answer
		elif questionNumber <= 218 and answer > 3:
			scoreDictionary['Negativity/Pessimism'] += answer
		elif questionNumber <= 232 and answer > 3:
			scoreDictionary['Punitiveness'] += answer
	return scoreDictionary

def getDiagnosticDictionary(answers):
	scoreDictionary = getScoreDictionary(answers)
	diagnosticDictionary = {

	}
	return diagnosticDictionary

scoreDictionary = getScoreDictionary(answers)
for key, value in scoreDictionary.items():
	print('{} : {}'.format(key, value))

