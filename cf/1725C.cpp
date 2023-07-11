#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<ll>;
using vvi = vector<vector<ll>>;

const ll MOD = 998244353;

struct mi { // WARNING: needs some adjustment to work with FFT
 	int v; explicit operator int() const { return v; } 
	mi():v(0) {}
	mi(ll _v):v(int(_v%MOD)) { v += (v<0)*MOD; }
};
mi& operator+=(mi& a, mi b) { 
	if ((a.v += b.v) >= MOD) a.v -= MOD; 
	return a; }
mi& operator-=(mi& a, mi b) { 
	if ((a.v -= b.v) < 0) a.v += MOD; 
	return a; }
mi operator+(mi a, mi b) { return a += b; }
mi operator-(mi a, mi b) { return a -= b; }
mi operator*(mi a, mi b) { return mi((ll)a.v*b.v); }
mi& operator*=(mi& a, mi b) { return a = a*b; }
mi pow(mi a, ll p) { assert(p >= 0); // won't work for negative p
	return p==0?1:pow(a*a,p/2)*(p&1?a:1); }
mi inv(mi a) { assert(a.v != 0); return pow(a,MOD-2); }
mi operator/(mi a, mi b) { return a*inv(b); }
bool operator==(mi a, mi b) { return a.v == b.v; }

int main() {
    ll n, m;
    cin >> n >> m;
    vector<ll> d(n);
    vector<ll> arc(1, 0);
    for (int i = 0;i < n;i++) {
        cin >> d[i];
        arc.push_back(arc[i] + d[i]);
    }
    ll tot = arc.back();
    int k = 0;
    if (tot%2==0) {
        for (int i = 0;i < n;i++) {
            int idx = lower_bound(arc.begin(), arc.end(), arc[i] - tot/2) - arc.begin();
            if (arc[i] - arc[idx] == tot/2) {
                k++;
            }
        }
    }

    mi choose(1);
    mi samecolor(1);

    mi ret(0);

    for (int i = 0;i <= k;i++) {
        mi term = choose * samecolor;
        mi x = pow(mi(m)-i, (ll)n-(2*i)-(k-i));
        mi y = pow(mi(m-i-1), k-i);
        ret += term * x * y;

        choose *= k-i;
        choose *= inv(i+1);
        samecolor *= m-i;
    }
    cout << ret.v << endl;
    return 0;

}