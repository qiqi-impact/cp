#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vll = vector<ll>;
using vvi = vector<vector<int>>;
using pii = pair<int, int>;
using umv = unordered_map<int, vector<int>>;

void dfs(umv &g, vi &a, vi &b, int idx, vi &ans, vll &path, ll sofar) {
    path.push_back(path.back() + b[idx]);
    ll ns = sofar + a[idx];
    int ln = upper_bound(path.begin(), path.end(), ns) - path.begin();
    ans[idx] = ln - 2;
    for (auto &x : g[idx]) {
        dfs(g, a, b, x, ans, path, ns);
    }
    path.pop_back();
}

void solve() {
    int n;
    cin >> n;

    umv g;
    vi a(n), b(n);
    b[0] = 0;
    int p;

    for (int i = 1;i < n;i++) {
        cin >> p >> a[i] >> b[i];
        g[p-1].push_back(i);
    }

    vi ans(n);
    vll path;
    path.push_back(0);
    dfs(g, a, b, 0, ans, path, 0LL);
    for (int i = 1;i < n;i++) cout << ans[i] << " ";
    cout << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}