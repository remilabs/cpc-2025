#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;

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
      h = (int)ceil(h / 2);
      count++;
    }
    if (w > ww) {
      w = (int)ceil(w / 2);
      count++;
    }
    a = max(h, w);
    b = min(h, w);
    h = a;
    w = b;
  }
  cout << count << endl;
  return 0;
}
