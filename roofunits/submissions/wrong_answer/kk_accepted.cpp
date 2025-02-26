#include <cmath>
#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int deg_to_rise_run(double deg) { return (int)(12 * tan(deg * M_PI / 180)); }

double rise_run_to_deg(int rise) {
  return atan((double)rise / 12.0) * 180 / M_PI;
}

int main() {
  int n;
  cin >> n;
  while (n--) {
    string query;
    cin >> query;
    auto pos = query.find("/");
    if (pos != string::npos) {
      string xs = query.substr(0, pos);
      int x = stoi(xs);
      double deg = rise_run_to_deg(x);
      printf("%.1f\n", deg);
    } else {
      double x = stod(query);
      int rise = deg_to_rise_run(x);
      printf("%d/12\n", rise);
    }
  }
  return 0;
}
