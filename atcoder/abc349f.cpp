#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
using vi = vector<int>;
using vvi = vector<vi>;
using vll = vector<ll>;
using vvll = vector<vll>;
using pii = pair<int, int>;

namespace output {
	void pr(int x) { cout << x; }
	void pr(long x) { cout << x; }
	void pr(ll x) { cout << x; }
	void pr(unsigned x) { cout << x; }
	void pr(unsigned long x) { cout << x; }
	void pr(unsigned long long x) { cout << x; }
	void pr(float x) { cout << x; }
	void pr(double x) { cout << x; }
	void pr(ld x) { cout << x; }
	void pr(char x) { cout << x; }
	void pr(const char* x) { cout << x; }
	void pr(const string& x) { cout << x; }
	void pr(bool x) { pr(x ? "true" : "false"); }
	template<class T> void pr(const complex<T>& x) { cout << x; }
	
	template<class T1, class T2> void pr(const pair<T1,T2>& x);
	template<class T> void pr(const T& x);
	
	template<class T, class... Ts> void pr(const T& t, const Ts&... ts) { 
		pr(t); pr(ts...); 
	}
	template<class T1, class T2> void pr(const pair<T1,T2>& x) { 
		pr("{",x.first,", ",x.second,"}"); 
	}
	template<class T> void pr(const T& x) { 
		pr("{"); // const iterator needed for vector<bool>
		bool fst = 1; for (const auto& a: x) pr(!fst?", ":"",a), fst = 0; 
		pr("}");
	}
	
	void ps() { pr("\n"); } // print w/ spaces
	template<class T, class... Ts> void ps(const T& t, const Ts&... ts) { 
		pr(t); if (sizeof...(ts)) pr(" "); ps(ts...); 
	}
	
	void pc() { pr("]\n"); } // debug w/ commas
	template<class T, class... Ts> void pc(const T& t, const Ts&... ts) { 
		pr(t); if (sizeof...(ts)) pr(", "); pc(ts...); 
	}
	#define dbg(x...) pr("[",#x,"] = ["), pc(x);
}

using namespace output;

vvll dp;
int n;
int fl;
vector<pair<ll, int>> fac;
const ll MOD = 998244353LL;
// vi valid, bb;
vi bmct;

ll f(int idx, int bm) {
	// TODO - combine A_i by bitmask/count to reduce complexity
	if (idx == 1 << fl) {
		return (int)(bm == (1 << fl) - 1);
	}
	if (dp[idx][bm] != -1) return dp[idx][bm];
	ll r = f(idx+1, bm);
	if (bmct[idx]) r += ((1LL << bmct[idx]) - 1) * f(idx+1, bm | idx) % MOD;
	r %= MOD;
	dp[idx][bm] = r;
	return r;
}

void solve() {
	ll m;
	cin >> n >> m;
	vi a(n);
	// valid = vi(n, 0);
	// bb = vi(n, 0);

	

	for (int i = 0;i < n;i++) cin >> a[i];
	fac = vector<pair<ll, int>>();
	int ct = 0;
	while (m%2 == 0) {
		m /= 2;
		ct++;
	}
	if (ct) fac.push_back(pair<ll, int>(2, ct));
	for (ll p = 3;p < (ll)1e8;p += 2) {
		int ct = 0;
		while (m%p == 0) {
			m /= p;
			ct++;
		}
		if (ct) fac.push_back(pair<ll, int>(p, ct));
	}
	if (m != 1) fac.push_back(pair<ll, int>(m, 1));
	fl = fac.size();
	dp = vvll(1 << fl, vll(1 << fl, -1));
	bmct = vi(1 << fl);
	
	for (int i = 0;i < n;i++) {
		int fail = 0;
		int bm = 0;
		for (int j = 0;j < fl;j++) {
			auto &[x, y] = fac[j];
			int ct = 0;
			while (a[i] % x == 0) {
				a[i] /= x;
				ct++;
			}
			if (ct > y) {
				fail = 1;
				break;
			} else if (ct == y) {
				bm ^= 1 << j;
			}
		}
		if (a[i] != 1) fail = 1;
		if (!fail) bmct[bm]++;
	}
	// dbg(valid, bb);

	cout << f(0, 0) << endl;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    solve();
    return 0;
}