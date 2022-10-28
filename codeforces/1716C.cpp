#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

void solve() {
    int m;
    cin >> m;
    vvi a(2, vi(m)), rt(2, vi(m));
    for (int i = 0;i < m;i++) {
        cin >> a[0][i];
    }
    for (int i = 0;i < m;i++) {
        cin >> a[1][i];
    }
    rt[0][m-1] = max(a[0][m-1], a[1][m-1] - 1);
    rt[1][m-1] = max(a[1][m-1], a[0][m-1] - 1);
    for (int j = m-2;j >= 0;j--) {
        rt[0][j] = max(rt[0][j+1] - 1, a[0][j], a[1][j] - ((m - i) * 2 - 1)
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}