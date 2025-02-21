#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
typedef vector<int> vi;

map<int, int> times;
map<int, vi> graph;
map<int, bool> is_sink;

int dfs(int v) {
  vi children = graph[v];
  if (children.size() == 0)
    return times[v];
  int m = -1;
  for (int c : children) {
    int pt = dfs(c);
    m = max(m, pt + times[v]);
  }
  return m;
}

int main() {
  int n, m;
  cin >> n >> m;

  for (int i = 0; i < n; i++) {
    int t;
    cin >> t;
    times[i] = t;
  }

  for (int i = 0; i < m; i++) {
    int ai, bi;
    cin >> ai >> bi;
    graph[bi].push_back(ai);
    is_sink[ai] = false;
  }

  int mt = -1;
  for (int i = 0; i < n; i++) {
    mt = max(mt, dfs(i));
  }
  cout << mt;

  return 0;
}
