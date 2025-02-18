s = input()
n = int(input())

def shift(val, dir):
	return val[-dir:] + val[:-dir]

for _ in range(n):
	op = input().split()
	direction = op[0]
	value = int(op[1])
	if direction == 'l':
		s = shift(s, -value)
	elif direction == 'r':
		s = shift(s, value)

print(s)
