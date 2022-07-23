#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

bool bs(double t, vi &x, vi &v) {
    double mn = DBL_MIN;
    double mx = DBL_MAX;
    for (int i = 0;i < x.size();i++) {
        mn = max(mn, x[i]-v[i]*t);
        mx = min(mx, x[i]+v[i]*t);
        if (mn > mx) return false;
    }
    return true;
}

int main() {
    int n;
    cin >> n;
    vi x(n), v(n);
    for (int i = 0;i < n;i++) {
        cin >> x[i];
    }
    for (int i = 0;i < n;i++) {
        cin >> v[i];
    }
    double l = 0, r = pow(10, 9);
    while (r - l > pow(10, -7)) {
        double mi = (l+r)/2;
        if (bs(mi, x, v)) {
            r = mi;
        } else {
            l = mi;
        }
    }
    cout << fixed << setprecision(10) << l << endl;
    return 0;
}