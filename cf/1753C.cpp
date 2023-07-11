#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

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
	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		int ct = 0;
		vi a(n);
		int miss = 0;
		for (int i = 0;i < n;i++) {
			cin >> a[i];
			ct += (int)(1-a[i]);
		}
		for (int i = ct;i < n;i++) {
			if (!a[i]) miss++;
		}
		mi num = {(ll)n * (n-1) / 2};

		mi ret = {0};
		for (ll i = 1;i <= miss;i++) {
			ret += num * inv(mi(i*i));
		}
		cout << ret.v << endl;
	}
	return 0;
}