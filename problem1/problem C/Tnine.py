ans = open("C-large-practice.out", 'w')

letters = {
	'2': 'abc',
	'3': 'def',
	'4': 'ghi',
	'5': 'jkl',
	'6': 'mno',
	'7': 'pqrs',
	'8': 'tuv',
	'9': 'wxyz',
	'0': ' '
}

with open("C-large-practice.in") as f:
	no_test_cases = int(f.readline())
	for k in range(1, no_test_cases+1):
		sentences = list(f.readline().strip("\n"))
		lst = []
		prev_key = ""
		for letter in sentences:
			s = list(filter(lambda tpl: letter.lower() in tpl[1], letters.items()))
			key = s[0][0]
			repeat = s[0][1].find(letter) + 1
			if prev_key == key:
				lst.append(" ")
			lst.append(key*repeat)
			prev_key = key
		a = "".join(lst)
		soln = "Case #{}: {}\n".format(k, a)
		print(soln)
		ans.write(soln)
ans.close()