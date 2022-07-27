#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vll = vector<ll>;
using vvi = vector<vector<int>>;

int main() {
    int n;
    ll k;
    cin >> n >> k;
    vll a(n);
    for (int i = 0;i < n;i++) cin >> a[i];
    sort(a.begin(), a.end());
    int mid = (n-1)/2;
    int ptr = mid; // last one we have totally filled up
    while (ptr < n-1) {
        // cout << ptr << " " << k << endl;
        if (k >= (a[ptr+1] - a[ptr]) * (ptr+1-mid)) {
            k -= (a[ptr+1] - a[ptr]) * (ptr+1-mid);
            ptr++;
        } else {
            ll x = k / (ll)(ptr+1-mid);
            cout << (a[ptr] + x) << endl;
            return 0;
        }
    }
    cout << (k / (ll)(n-mid) + a[n-1]) << endl;
    return 0;
}