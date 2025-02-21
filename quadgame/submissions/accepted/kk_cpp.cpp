#include <climits>
#include <cmath>
#include <iostream>
#include <map>
using namespace std;
typedef long long ll;
map<ll, int> h_counts;

ll inf = LONG_LONG_MAX;

ll check(ll rod, ll a, ll b) {
  ll diff = abs(rod - b);
  ll h = a * a + diff * diff;
  if (h_counts[h] > (h == rod * rod ? 1 : 0)) {
    ll s = a + b + rod + (ll)sqrt(h);
    return s;
  }
  return inf;
}

int main() {
  ll n, a, b;
  cin >> n >> a >> b;
  ll rods[n - 2];

  for (int i = 0; i < n - 2; i++) {
    ll x;
    cin >> x;
    rods[i] = x;
    h_counts[x * x] += 1;
  }

  ll best = inf;
  for (ll rod : rods) {
    best = min(check(rod, a, b), best);
    best = min(check(rod, b, a), best);
  }

  cout << (best == inf ? -1 : best) << endl;
  return 0;
}
