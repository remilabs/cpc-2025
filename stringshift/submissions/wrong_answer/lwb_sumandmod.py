s = input()
n = int(input())

o = []
for _ in range(n):
	op = input().split()
	direction = op[0]
	value = int(op[1])
	if direction == 'l':
		value *= -1
	o.append(value)

shift_amount = sum(o) % len(s)
ret = s[shift_amount:] + s[:shift_amount]

print(ret)
