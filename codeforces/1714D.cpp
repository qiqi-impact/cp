#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;

int main() {
    int q;
    cin >> q;
    while (q--) {
        string t;
        cin >> t;
        int n;
        cin >> n;
        vector<string> s(n);
        vector<int> dp(t.size(), 0);
        vector<int> idxs(t.size(), 0);
        vector<int> ans(t.size()+1, 1000000);
        ans[t.size()] = 0;
        for (int i = 0;i < n;i++) {
            cin >> s[i];
            int cur = -1;
            while (1) {
                cur = t.find(s[i],cur+1);
                if (cur == string::npos) {
                    break;
                } else {
                    int p = s[i].size();
                    if (p > dp[cur]) {
                        dp[cur] = p;
                        idxs[cur] = i;
                    }
                }
            }
        }
        vector<int> f(t.size()+1, -1);
        for (int i = t.size()-1;i >= 0;i--) {
            for (int j = 1;j <= dp[i];j++) {
                int idx = i+j;
                if (idx == t.size()+1) break;
                if (1 + ans[idx] < ans[i]) {
                    ans[i] = 1 + ans[idx];
                    f[i] = idx;
                }
            }
        }

        if (ans[0] >= 1000000) {
            cout << -1 << endl;
        } else {
            cout << ans[0] << endl;
            int cur = 0;
            while (cur != t.size()) {
                cout << (1+idxs[cur]) << " " << (1+cur) << endl;
                cur = f[cur];
            }
        }
    }
    return 0;
}