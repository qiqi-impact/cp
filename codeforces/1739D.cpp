#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

int need(vvi &g, int limit, int idx, int depth, int k) {
    int ret = 1e9;

    if (depth <= limit) {
        int a = 0;
        for (auto &x : g[idx]) {
            a += need(g, limit, x, depth+1, k);
            if (a > k) {
                a = 1e9;
                break;
            }
        }
        ret = min(ret, a);
    }

    int b = 1;
    for (auto &x : g[idx]) {
        b += need(g, limit, x, 2, k);
        if (b > k) {
            b = 1e9;
            break;
        }
    }
    ret = min(ret, b);

    return ret;
}

int solve() {
    int n, k;
    cin >> n >> k;
    vvi g(n+1);
    vi p(n, -1);
    for (int i = 0;i < n-1;i++) {
        cin >> p[i+1];
        p[i+1]--;
        // g[p].push_back(i);
    }
    int l = 1, r = n-1;
    while (l < r) {
        int mi = (l+r)/2;

        vi dp(n, 0);
        int ct = 0;
        for (int i = n-1;i > 0;i--) {
            if (p[i] != 0 && dp[i] > mi - 1) {
                ct++;
            } else {
                dp[p[i]] = max(dp[p[i]], 1 + dp[i]);
            }
        }

        if (ct <= k) {
            r = mi;
        } else {
            l = mi + 1;
        }
    }
    return r;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) {
        cout << solve() << endl;
    }
    return 0;
}