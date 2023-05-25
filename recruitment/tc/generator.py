import random

s = set()

while len(s) != 10**4:
	s.add(random.randint(-10**8, 10**8))

print(*s)
