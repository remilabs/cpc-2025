#include <cmath>
#include <iostream>
using namespace std;

int main() {
  int h, w, hh, ww;
  cin >> h >> w >> hh >> ww;
  int count = 0;
  while (h > hh) {
    h = (int)ceil(h / 2);
    count++;
  }
  while (w > ww) {
    w = (int)ceil(w / 2);
    count++;
  }
  cout << count << endl;
  return 0;
}
