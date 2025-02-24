#include <bits/stdc++.h>
using namespace std;

int f(int x,int t) {
  if (x < t) return 100000000;
  int c = 0;
  while (x > t) x = (x+1)/2,++c;
  return c;
}

int main() {
  int w,h,x,y,m;
  cin >> w >> h >> x >> y;
  m = f(h,x) + f(w,y);
  m = min(m,f(w,x)+f(h,y));
  cout << m << endl;
}
