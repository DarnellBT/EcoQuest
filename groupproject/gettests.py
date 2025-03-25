import re

fa = ['about', 'achievements', 'challenge', 'dashboard', 'leaderboard', 'login', 'main', 'map', 'qrcodescan', 'quiz', 'registration', 'roleportals']
# ex = r'(?<=def )(.+)(?=\()|(?<=""")(.+)(?=""")|(self.assert.+)|(?<=class )(.+)(?=\()'
ex = r'(?<=def )(.+)(?=\(self)'

for f in fa:
	with open(f+'/tests.py', 'r') as file:
		print('\n'+f)
		i = 1
		for line in file:

			tests_cases = re.findall(ex, line)
			for s in tests_cases:
				i += 1
				print(s)
		if i > 1:
			print(i)