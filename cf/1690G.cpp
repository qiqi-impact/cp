#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, q;
        cin >> n >> q;
        vi speeds(n);
        int mn = INT_MAX;
        map<int, int> mp;
        for (int i = 0;i < n;i++) {
            cin >> speeds[i];
            if (speeds[i] < mn) {
                mp[i] = mn = speeds[i];
            }
        }
        while (q--) {
            int idx, val;
            cin >> idx >> val;
            idx--;
            speeds[idx] -= val;
            if (mp.find(idx) == mp.end()) {
                auto it = prev(mp.upper_bound(idx));
                if (speeds[idx] < it->second) {
                    mp[idx] = speeds[idx];
                }
            } else {
                mp[idx] = speeds[idx];
            }
            auto it = mp.upper_bound(idx);
            // cout << idx << p->first << it->first << endl;
            while (it != mp.end()) {
                // cout << it->second << " " << speeds[idx] << endl;
                if (it->second >= speeds[idx]) {
                    auto oit = it;
                    it = next(it);
                    mp.erase(oit);
                } else {
                    break;
                }
            }
            cout << mp.size() << " ";
        }
        cout << endl;
    }
    return 0;
}