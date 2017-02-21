ans = open("A-large-practice.out", 'w')

with open("A-large-practice.in") as f:
	no_test_cases = int(f.readline())
	for k in range(1, no_test_cases+1):
		number_of_int = f.readline()
		vect_a = list(map(lambda x: int(x), f.readline().split(" ")))
		vect_b = list(map(lambda x: int(x), f.readline().split(" ")))
		a = sum(q*w for q,w in zip(sorted(vect_a), sorted(vect_b, reverse=True)))
		soln = "Case #{}: {}\n".format(k, a)
		print(soln)
		ans.write(soln)
ans.close()