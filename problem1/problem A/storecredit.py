ans = open("A-large-practice.out", 'w')

with open("A-large-practice.in") as f:
	no_test_cases = int(f.readline())
	for k in range(1, no_test_cases+1):
		total_money = int(f.readline())
		no_of_items = int(f.readline())
		items = list(map(lambda x: int(x), f.readline().split(" ")))
		for i in range(0, len(items)):
			value = items[i]
			for j in range(i+1, len(items)):
				value_2 = items[j]
				if value + value_2 == total_money:
					an = (i+1, j+1)
					break
		ans.write("Case #{}: {} {}\n".format(k, an[0], an[1]))
ans.close()