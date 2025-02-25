class Graph:
  def bfs(self, s, t, parent):
    v = [False] * self.size
    stack = []
    stack.append(s)
    v[s] = True
    while stack:
      u = stack.pop()
      if u == t: return True
      for ind, val in enumerate(self.adj_matrix[u]):
        if not v[ind] and val > 0:
          stack.append(ind)
          v[ind] = True
          parent[ind] = u
    return Fal

  def __init__(self, size):
    self.adj_matrix = [[0] * size for _ in range(size)]
    self.size = size

  def add_edge(self, u, v, c):
    self.adj_matrix[u][v] = c

  def edmonds_karp(self, source, sink):
    parent = [-1] * self.size
    max_flow = 0
    while self.bfs(source, sink, parent):
      path_flow = float("Inf")
      s = sink
      while(s != source):
        path_flow = min(path_flow, self.adj_matrix[parent[s]][s])
        s = parent[s]
      max_flow += path_flow
      v = sink
      while(v != source):
        u = parent[v]
        self.adj_matrix[u][v] -= path_flow
        self.adj_matrix[v][u] += path_flow
        v = parent[v]
      path = []
      v = sink
      while(v != source):
        path.append(v)
        v = parent[v]
      path.append(source)
      path.reverse()
    return max_flow

r = lambda: list(map(int,input().split()))
n,m = r()
ntoi = lambda x: x+1
mtoi = lambda x: x+n+1
t = n+m+1
g = Graph(t+1)
for i in range(n):
  c = int(input())
  g.add_edge(0, ntoi(i), c)
possible = set()
for _ in range(int(input())):
  a,b = r()
  possible.add((a,b))

for _ in range(int(input())):
  a,b = r()
  if (b,a) in possible:
    g.add_edge(ntoi(b), mtoi(a), 1)

for i in range(m):
  g.add_edge(mtoi(i), t, 1)

print(g.edmonds_karp(0,t))
