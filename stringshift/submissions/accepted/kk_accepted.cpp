/*#include <cstdio>*/
#include <iostream>
#include <string>
/*#include <string>*/
using namespace std;

int main() {
  string s;
  getline(cin, s);
  int n;
  cin >> n;
  int shift = 0;
  while (n--) {
    string query;
    cin >> query;
    int x;
    cin >> x;
    shift += (query == "l") ? x : -x;
  }
  int l = s.length();
  int part = (shift % l + l) % l;
  cout << s.substr(part) << s.substr(0, part) << endl;
  return 0;
}
