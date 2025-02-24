#include <bits/stdc++.h>

using namespace std;

int main(){
  string s;
  getline(cin, s);
  int n;
  cin >> n;
  int rotations = 0;
  int l = s.size();
  while (n--){
    char d;
    int r;
    cin >> d >> r;
    rotations += d == 'l' ? r : -r;
    rotations %= l;
    if (rotations < 0) rotations += l;
  }
  rotate(s.begin(), s.begin()+rotations, s.end());
  cout << s << endl;
}
