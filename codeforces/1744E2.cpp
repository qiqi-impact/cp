#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

ll a, b, c, d;
vvi fac;
ll x, y;

bool dfs(int idx, ll acc) {
    if (idx == fac.size()) {
        ll inv = a * b / acc;
        ll p = a + (acc - a%acc);
        if (p > c) return false;
        ll q = b + (inv - b%inv);
        if (q > d) return false;
        x = p;
        y = q;
        return true;
    }
    auto v = fac[idx];
    for (int i = 0;i <= v[1];i++) {
        if (dfs(idx+1, acc)) return true;
        acc *= v[0];
        if (acc > (ll)1e9) break;
    }
    return false;
}

void solve() {
    cin >> a >> b >> c >> d;
    int aa = a, bb = b;
    fac.clear();
    for (int i = 2;i < (int)1e5;i++) {
        int ct = 0;
        while (aa % i == 0) {
            aa /= i;
            ct++;
        }
        while (bb % i == 0) {
            bb /= i;
            ct++;
        }
        if (ct) fac.push_back({i, ct});
    }
    if (aa > 1 && aa == bb) {
        fac.push_back({aa, 2});
    } else {
        if (aa > 1) fac.push_back({aa, 1});
        if (bb > 1) fac.push_back({bb, 1});
    }
    if (dfs(0, 1)) {
        cout << x << " " << y << endl;
    } else {
        cout << -1 << " " << -1 << endl;
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) solve();
}