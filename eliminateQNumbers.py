import re

with open('questionsSafe.txt', 'r') as readFile:
	with open('questionsProcessed.txt', 'w') as writeFile:
		for line in readFile:
			# print(re.sub(r'^\d+\.\s+', '', line).strip())
			# print(line)
			writeFile.write(re.sub(r'^\d+\.\s+', '', line))