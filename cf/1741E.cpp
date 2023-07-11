#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

void solve() {
    int n;
    cin >> n;
    vi arr(n), dp(n+1, 0);
    dp[n] = 1;
    for (int i = 0;i < n;i++) {
        cin >> arr[i];
    }
    for (int i = n-1;i >= 0;i--) {
        int o = i + arr[i] + 1;
        if (o <= n) {
            dp[i] |= dp[o];
        }
        o = i - arr[i];
        if (o >= 0) {
            dp[o] |= dp[i+1];
        }
    }
    cout << (dp[0] ? "YES" : "NO") << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}