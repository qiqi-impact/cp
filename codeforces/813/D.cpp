#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using pii = pair<int, int>;

bool f(int ans, vi &v, int k) {
    // cout << ans << " ";
    int ct = 0, mx = 0, mn = 1e9;
    for (auto x: v) {
        if (2*x < ans) {
            ct++;
        } else {
            mn = min(x, mn);
        }
        mx = max(x, mx);
    }
    // cout << ct << " " << k << endl;
    if (ct > k) return false;
    int left = k - ct;
    if (left == 0) {
        int mxdf = 0;
        for (int i = 0;i < v.size()-1;i++) {
            int m = 1e9;
            m = min(m, (2 * v[i] < ans) ? (int)1e9 : v[i]);
            m = min(m, (2 * v[i+1] < ans) ? (int)1e9 : v[i+1]);
            m = min(m, 2 * mn);
            mxdf = max(mxdf, m);
        }
        return mxdf >= ans;
    }
    if (k >= 2) return true;
    return mx >= ans;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        vi v(n);

        int mn = 1e9;
        for (int i = 0;i < n;i++) {
            cin >> v[i];
            mn = min(mn, v[i]);
        }

        int lo = 1, hi = 1e9;
        while (lo < hi) {
            int mi = (lo+hi+1)/2;
            if (f(mi, v, k)) {
                lo = mi;
            } else {
                hi = mi - 1;
            }
        }
        cout << lo << endl;
    }
    return 0;
}