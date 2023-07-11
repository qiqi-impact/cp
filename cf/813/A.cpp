#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        vi v(n);
        int ret = 0;
        for (int i = 0;i < n;i++) cin >> v[i];
        sort(v.begin(), v.begin()+k);
        for (int i = 0;i < k;i++) {
            if (v[i] > k) ret++;
        }
        cout << ret << endl;
    }
    return 0;
}