#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<ll>;
using vvi = vector<vector<ll>>;

int main() {
    int n, m;
    cin >> n >> m;
    
    vi ct(n), a(n);
    ll sm = 0;
    for (int i = 0;i < n;i++) {
        cin >> a[i];
        if (i > 0) {
            ct[i] += ct[i-1];
            if (a[i] != a[i-1]) ct[i] += i;
        }
        ct[i]++;
        sm += ct[i];
    }

    for (int i = 0;i < m;i++) {
        int idx, v;
        cin >> idx >> v;
        idx--;

        if (idx > 0) {
            if (a[idx] != a[idx-1] && v == a[idx-1]) {
                sm -= (ll)idx * ((ll)n - idx);
            }
            if (a[idx] == a[idx-1] && v != a[idx-1]) {
                sm += (ll)idx * ((ll)n - idx);
            }
        }

        if (idx < n-1) {
            if (a[idx] != a[idx+1] && v == a[idx+1]) {
                sm -= (ll)(idx+1) * ((ll)n - (idx+1));
            }
            if (a[idx] == a[idx+1] && v != a[idx+1]) {
                sm += (ll)(idx+1) * ((ll)n - (idx+1));
            }
        }

        cout << sm << endl;
        a[idx] = v;

    }



    return 0;
}