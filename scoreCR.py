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


# Emotional Deprivation 1-9
# Abandonment 10-26
# Mistrust/Abuse 27-43
# Social Isolation 44-53
# Defectiveness 54-68
# Failure 69-77
# Dependence 78-92
# Vulnerablity 93-104
# Enmeshment 105-115
# Subjugation 116-125
# Self-Sacrifice 126-142
# Emotional INhibition 143-151
# Unrelenting Standards 152-167
# Entitlement 168-178
# Insufficient Self-Control 179-193
