#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using pii = pair<int, int>;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;

        vi v(n);
        auto cmp = [&](int left, int right) {
            if (v[left] == v[right]) {
                // cout << left << right << endl;
                int ll = left > 0 ? v[left-1] : 0;
                int lr = left < n-1 ? v[left+1] : 0;
                int rl = right > 0 ? v[right-1] : 0;
                int rr = right < n-1 ? v[right+1] : 0;
                // cout << ll << lr << rl << rr << n << endl;
                return max(ll, lr) < max(rl, rr);
            }
            return v[left] > v[right];
        };
        priority_queue<int, vi, decltype(cmp)> pq(cmp);

        for (int i = 0;i < n;i++) {
            cin >> v[i];
        }

        for (int i = 0;i < n;i++) {
            pq.push(i);
        }

        int kk = k;
        while (k-- && !pq.empty()) {
            int q = pq.top();
            // cout << q << endl;
            pq.pop();
            v[q] = (int)1e9;
        }

        if (pq.empty()) {
            cout << (int)1e9 << endl;
        } else {
            int largest = 0;
            int smallest = v[pq.top()];
            while (!pq.empty()) {
                largest = v[pq.top()];
                pq.pop();
            }
            // cout << smallest << largest << endl;

            // int mn = largest;

            int mn = 0;
            for (int i = 0;i < n-1;i++) {
                mn = max(mn, min(v[i], v[i+1]));
            }
            mn = min(mn, 2 * smallest);
            mn = min((int)1e9, mn);
            cout << mn << endl;
        }

        // int q;
        // int o = -1;
        // int diff = 0;
        // int mx = 0;
        // for (int i = 0;i < n;i++) {
        //     cin >> q;
        //     if (i > 0) {
        //         diff = max(abs(q - o), diff);
        //     }
        //     mx = max(mx, q);
        //     o = q;
        // }
        // if (k == 0) cout << diff << endl;
        // else if (k == 1) cout << mx << endl;
        // else cout << 1e9 << endl;
    }
    return 0;
}