#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;
typedef long l;

int main() {
  int h, w, hh, ww;
  cin >> h >> w >> hh >> ww;
  int oh = h, ow = w;
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
  h = oh; w = ow;
  swap(hh,ww);
  int count2 = 0;
  while (h > hh || w > ww) {
    if (h > hh) {
      h = ceil(h / 2.0);
      count2++;
    }
    if (w > ww) {
      w = ceil(w / 2.0);
      count2++;
    }
  }
  cout << min(count,count2) << endl;
  return 0;
}
