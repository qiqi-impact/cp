#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

bool solve() {
    int n, k;
    cin >> n >> k;
    vi a(n);
    k--;

    for (int i = 0;i < n;i++) cin >> a[i];

    ll h = a[k];
    ll ap = k, bp = k;
    ll ac = 0, bc = 0;
    while (1) {
        bool did = false;
        while (ap >= 0 && ac + h >= 0) {
            did = true;
            ap--;
            if (ap == -1) return true; 
            ac += a[ap];
            if (ac > 0) {
                h += ac;
                ac = 0;
            }
        }
        while (bp < n && bc + h >= 0) {
            did = true;
            bp++;
            if (bp == n) return true; 
            bc += a[bp];
            if (bc > 0) {
                h += bc;
                bc = 0;
            }
        }
        if (!did) return false;
    }
    return false;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        cout << (solve() ? "YES" : "NO") << endl;
    }
    return 0;
}