#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i = a; i < b; i++)
#define per(i,a,b) for(int i = a; i >= b; i--)
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef tuple<int,int> ii;
typedef vector<ii> vii;

int s = 101;
int xx,yy,n;

using namespace std;
vii spiral(){
    vii res;
    int x = s+1, y = s;
    int dx = 0, dy = 1;
    int side = 1;
    while (!(x == 0 && y == 0)) {
        res.push_back({x, y});
        if (dx == 0 && dy == 1) {
            if (y == s + side) {
                dx = -1;
                dy = 0;
            }
        } else if (dx == -1 && dy == 0) {
            if (x == s - side) {
                dx = 0;
                dy = -1;
            }
        } else if (dx == 0 && dy == -1) {
            if (y == s - side) {
                dx = 1;
                dy = 0;
            }
        } else if (dx == 1 && dy == 0) {
            if (x == s + side) {
                dx = 0;
                dy = 1;
                side++;
            }
        }
        x += dx;
        y += dy;
    }
    res.push_back({0, 0});
    return res;
}

vii parents(int x, int y, vvi &blocked) {
    vii res;
    if (blocked[x][y]) return res;
    if (x >= s && y > s) {
        per(i, x, 0) {
            if (blocked[i][y]) break;
            if (i < 2 * s - x) res.push_back({i, y});
        }
    }
    if (x < s && y >= s) {
        per(i, y, 0) {
            if (blocked[x][i]) break;
            if (i < 2 * s - y) res.push_back({x, i});
        }
    }
    if (x <= s && y < s) {
        rep(i, x, 2*s+2) {
            if (blocked[i][y]) break;
            if (i > 2 * s - x) res.push_back({i, y});
        }
    }
    if (x > s && y <= s) {
        rep(i, y, 2*s+2) {
            if (blocked[x][i]) break;
            if (i > 2 * s - y) res.push_back({x, i});
        }
    }
    return res;
}
int main() {
    int q = s*2;
    cin >> xx >> yy >> n;
    vvi a(s*2+2, vi(s*2+2, 0));
    vvi blocked(s*2+2, vi(s*2+2, 0));
    vector<bool> visited(q*q, false);

    rep(i,0, s*2+2) {
        a[i][s] = 1;
        a[s][i] = 1;
    }

    rep(i, 0, n) {
        int x,y;
        cin >> x >> y;
        blocked[x+s][y+s] = 1;
    }

    for (auto [x, y] : spiral()) {
        int v = x*q + y;
        if (visited[v]) continue;
        visited[v] = true;
        if (blocked[x][y]) continue;
        for (auto [px, py] : parents(x, y, blocked)) {
            a[px][py] += a[x][y];
            a[px][py] %= 1000000007;
        }
    }

    cout << a[xx+s][yy+s] << endl;
    return 0;
}
