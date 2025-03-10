#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

#define rep(i,a,b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

struct PushRelabel {
	struct Edge {
		int dest, back;
		ll f, c;
	};
	vector<vector<Edge>> g;
	vector<ll> ec;
	vector<Edge*> cur;
	vector<vi> hs; vi H;
	PushRelabel(int n) : g(n), ec(n), cur(n), hs(2*n), H(n) {}

	void addEdge(int s, int t, ll cap, ll rcap=0) {
		if (s == t) return;
		g[s].push_back({t, sz(g[t]), 0, cap});
		g[t].push_back({s, sz(g[s])-1, 0, rcap});
	}

	void addFlow(Edge& e, ll f) {
		Edge &back = g[e.dest][e.back];
		if (!ec[e.dest] && f) hs[H[e.dest]].push_back(e.dest);
		e.f += f; e.c -= f; ec[e.dest] += f;
		back.f -= f; back.c += f; ec[back.dest] -= f;
	}
	ll calc(int s, int t) {
		int v = sz(g); H[s] = v; ec[t] = 1;
		vi co(2*v); co[0] = v-1;
		rep(i,0,v) cur[i] = g[i].data();
		for (Edge& e : g[s]) addFlow(e, e.c);

		for (int hi = 0;;) {
			while (hs[hi].empty()) if (!hi--) return -ec[s];
			int u = hs[hi].back(); hs[hi].pop_back();
			while (ec[u] > 0)  // discharge u
				if (cur[u] == g[u].data() + sz(g[u])) {
					H[u] = 1e9;
					for (Edge& e : g[u]) if (e.c && H[u] > H[e.dest]+1)
						H[u] = H[e.dest]+1, cur[u] = &e;
					if (++co[H[u]], !--co[hi] && hi < v)
						rep(i,0,v) if (hi < H[i] && H[i] < v)
							--co[H[i]], H[i] = v + 1;
					hi = H[u];
				} else if (cur[u]->c && H[u] == H[cur[u]->dest]+1)
					addFlow(*cur[u], min(ec[u], cur[u]->c));
				else ++cur[u];
		}
	}
	bool leftOfMinCut(int a) { return H[a] >= sz(g); }
};

int main() {
	int n,m;
	cin >> n >> m;
    PushRelabel g(n+m+2);
	int s = n+m;
	int t = n+m+1;

	// read in contractor capacities and connect to source
	rep(i,0,n) {
		int cap;
		cin >> cap;
		g.addEdge(s,i,cap);
	}

	// add edge of 1 from homeowner to terminal
	rep(i,0,m) {
		g.addEdge(n+i,t,1);
	}

	// map to allow edges to be added only if contractor can service homeowner and homeowner prefers that contractor
	unordered_map<int, unordered_set<int>> pref;
	int c;
	cin >> c;
	rep(i,0,c) {
		int a,b;
		cin >> a >> b;
		pref[a].insert(b);
	}
	int h;
	cin >> h;
	rep(i,0,h) {
		int a,b;
		cin >> a >> b;
		if (pref[b].find(a) != pref[b].end()) {
			g.addEdge(b,n+a,1);
		}
	}

	int res = g.calc(s,t);
	cout << res << endl;
}