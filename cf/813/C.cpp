#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vi v(n);
        unordered_set<int> seen;
        int np = -1;
        for (int i = 0;i < n;i++) cin >> v[i];
        for (int i = 0;i < n-1;i++) {
            if (v[i] > v[i+1] || (!seen.count(v[i]) && seen.count(v[i+1]))) {
                while (np < i) {
                    np++;
                    seen.insert(v[np]);
                }
            }
        }
        cout << seen.size() << endl;
    }
    return 0;
}