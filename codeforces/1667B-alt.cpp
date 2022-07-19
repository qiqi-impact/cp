/**
 *    author:  tourist
 *    created: 19.04.2022 18:32:02       
**/
#include <bits/stdc++.h>
 
using namespace std;
 
#ifdef LOCAL
#include "algo/debug.h"
#else
#define debug(...) 42
#endif
 
template <typename T>
class fenwick {
 public:
  vector<T> fenw;
  int n;
 
  fenwick(int _n) : n(_n) {
    fenw.resize(n);
  }
 
  void modify(int x, T v) {
    while (x < n) {
      fenw[x] += v;
      x |= (x + 1);
    }
  }
 
  T get(int x) {
    T v{};
    while (x >= 0) {
      v += fenw[x];
      x = (x & (x + 1)) - 1;
    }
    return v;
  }
};
 
const int inf = (int) 1e9;
 
struct node {
  int a = -inf;
 
  inline void operator += (node &other) {
    a = max(a, other.a);
  }
};
 
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int tt;
  cin >> tt;
  while (tt--) {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    vector<long long> pref(n + 1);
    for (int i = 0; i < n; i++) {
      pref[i + 1] = pref[i] + a[i];
    }
    vector<long long> xs = pref;
    sort(xs.begin(), xs.end());
    xs.resize(unique(xs.begin(), xs.end()) - xs.begin());
    int sz = (int) xs.size();
    for (int i = 0; i <= n; i++) {
      pref[i] = (int) (lower_bound(xs.begin(), xs.end(), pref[i]) - xs.begin());
    }
    vector<int> dp(n + 1);
    dp[0] = 0;
    fenwick<node> f0(sz), f2(sz);
    vector<int> f1(sz, -inf);
    for (int i = 0; i <= n; i++) {
      if (i > 0) {
        dp[i] = f1[pref[i]];
        dp[i] = max(dp[i], f0.get(pref[i] - 1).a + i);
        dp[i] = max(dp[i], f2.get(sz - 1 - pref[i] - 1).a - i);
      }
      f0.modify(pref[i], {dp[i] - i});
      f1[pref[i]] = max(f1[pref[i]], dp[i]);
      f2.modify(sz - 1 - pref[i], {dp[i] + i});

      cout << i << endl;

      for (int j = 0;j < sz;j++) {
          cout << f0.get(j).a << " ";
      }
      cout << endl;

      for (int j = 0;j < sz;j++) {
          cout << f1[j] << " ";
      }
      cout << endl;

      for (int j = 0;j < sz;j++) {
          cout << f2.get(j).a << " ";
      }
      cout << endl;

    }
    cout << dp[n] << '\n';
  }
  return 0;
}