ans = open("B-small-practice.out", 'w')

with open("B-small-practice.in") as f:
	no_test_cases = int(f.readline())
	for k in range(1, no_test_cases+1):
		sentences = f.readline().split(" ")
		sentences = list(map(lambda x: x.strip(), sentences))
		reversedSen = list(reversed(sentences))
		a = " ".join(reversedSen)
		soln = "Case #{}: {}\n".format(k, a)
		print(soln)
		ans.write(soln)
ans.close()