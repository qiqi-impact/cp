#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<ll>;
using vvi = vector<vector<ll>>;

int main() {
    while (1) {
        int n;
        cin >> n;
        if (!n) break;
        vvi m(n, vi(n, 0));
        for (int i = 0;i < n;i++) {
            for (int j = 0;j < i+1;j++) {
                cin >> m[i][j];
                if (i > 0) m[i][j] += m[i-1][j];
            }
        }
        vvi dp(n, vi(n, 0));
        for (int j = n-1;j >= 0;j--) {
            for (int i = j;i < n;i++) {
                dp[i][j] = m[i][j];
                if (j < n-1) dp[i][j] += dp[min(n-1, i+1)][j+1];
                if (i > 0) {
                    dp[i][j] = max(dp[i][j], dp[i-1][j]);
                } else {
                    dp[i][j] = max(dp[i][j], 0LL);
                }
                // cout << dp[i][j] << " ";
            }
            // cout << endl;
        }
        cout << dp[n-1][0] << endl;
    }

    return 0;
}