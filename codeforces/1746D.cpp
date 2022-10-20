#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;
using vll = vector<ll>;
using vvll = vector<vll>;

vll score(vvi &g, vll &s, int idx, int k) {
    ll sc = s[idx] * k;
    vll mxch;
    int sz = g[idx].size();

    if (!sz) {
        return {s[idx], sc};
    }

    int amt = k / sz;
    int mod = k % sz;

    for (auto &x : g[idx]) {
        vll r = score(g, s, x, amt);
        sc += r[1];
        mxch.push_back(r[0]);
        // cout << r[0] << " " << r[1] << endl;
    }

    sort(mxch.begin(), mxch.end());

    for (int i = 0;i < mod;i++) {
        sc += mxch[sz-1-i];
    }

    return {mxch[sz-1-mod] + s[idx], sc};
}

void solve() {
    int n, k;
    cin >> n >> k;
    vvi g(n);
    vll s(n);
    for (int i = 1;i < n;i++) {
        int p;
        cin >> p;
        p--;
        g[p].push_back(i);
    }
    for (int i = 0;i < n;i++) {
        cin >> s[i];
    }
    // cout << "hello" << endl;
    cout << score(g, s, 0, k)[1] << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}