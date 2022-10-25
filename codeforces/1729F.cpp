#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

void solve() {
    string s;
    cin >> s;
    int w, q;
    cin >> w >> q;
    vvi mod_index(9);
    vi ps(1, 0);
    for (int i = 0;i < s.size();i++) ps.push_back(ps[i] + s[i] - '0');
    int cur = 0;
    for (int i = 0;i < w;i++) {
        cur += s[i] - '0';
    }
    mod_index[cur%9].push_back(1);
    for (int i = w;i < s.size();i++) {
        cur += s[i] - '0' - (s[i - w] - '0');
        if (mod_index[cur%9].size() < 2)
            mod_index[cur%9].push_back(i - w + 2);
    }

    for (int i = 0;i < q;i++) {
        int l, r, k;
        cin >> l >> r >> k;
        l--; r--;
        int lrs = (ps[r+1] - ps[l]) % 9;
        vi ret = {(int)1e9, (int)1e9};
        for (int j = 0;j < 9;j++) {
            if (!mod_index[j].empty() && mod_index[j][0] < ret[0]) {
                int p = ((k - j * lrs) % 9 + 9) % 9;
                if (j == p) {
                    if (mod_index[j].size() == 2) {
                        ret = {mod_index[j][0], mod_index[j][1]};
                    }
                } else {
                    if (!mod_index[p].empty()) {
                        ret = {mod_index[j][0], mod_index[p][0]};
                    }
                }
            }
        }
        if (ret[0] == (int)1e9) cout << "-1 -1" << endl; else cout << ret[0] << " " << ret[1] << endl;
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}