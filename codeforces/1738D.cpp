#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

void solve() {
    int n;
    cin >> n;
    vi a(n+1);
    int k = n;
    unordered_map<int, vector<int>> inv;

    vector<int> cur;
    int forcelast;

    for (int i = 1;i <= n;i++) {
        cin >> a[i];
        inv[a[i]].push_back(i);
        if (a[i] < i && k == n) k = i-1;
        if (a[i] == 0 || a[i] == n+1) cur.push_back(i);
    }

    cout << k << endl;
    while (1) {
        forcelast = -1;
        for (auto x: cur) {
            if (inv[x].size()) forcelast = x;
        }
        if (forcelast == -1) break;

        for (auto x: cur) if (x != forcelast) cout << x << " ";
        cout << forcelast << " ";
        cur = inv[forcelast];
    }
    for (auto x: cur) cout << x << " ";
    cout << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}