#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;
typedef long l;

int main() {
  int h, w, hh, ww;
  cin >> h >> w >> hh >> ww;
  int a = max(h, w), b = min(h, w), c = max(hh, ww), d = min(hh, ww);
  h = a;
  w = b;
  hh = c;
  ww = d;
  int count = 0;
  while (h > hh || w > ww) {
    if (h > hh) {
      h = ceil(h / 2.0);
      count++;
    }
    if (w > ww) {
      w = ceil(w / 2.0);
      count++;
    }
  }
  cout << count << endl;
  return 0;
}
