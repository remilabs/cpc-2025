s=input()
v=-sum([[1,-1][l=='l']*int(n)for l,n in[input().split()for _ in range(int(input()))]])%len(s)
print(s[v:]+s[:v])