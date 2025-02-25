r = lambda: [*map(int,input().split())]

def kuhn_algorithm(n, m, adj_matrix):
  match_right = [-1] * m  # Stores matchings for right set (V)
  visited = set()
  def dfs(u):
    if u in visited:
      return False
    visited.add(u)
    for v in range(m):
      if adj_matrix[u][v] and (match_right[v] == -1 or dfs(match_right[v])):
        match_right[v] = u
        return True
    return False
  match_count = 0
  for u in range(n):
    visited.clear()
    if dfs(u):
      match_count += 1
  return match_count

n,m = r()

for _ in range(n):
  input()
s = set()
for _ in range(int(input())):
  a,b = r()
  s.add((b,a))
g = [[0] * m for _ in range(n)]
for _ in range(int(input())):
  a,b = r()
  if (a,b) in s:
    g[b][a] = 1
print(kuhn_algorithm(n,m,g))


