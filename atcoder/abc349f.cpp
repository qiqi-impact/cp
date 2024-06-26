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

vll dp;
int n;
int fl;
vector<pair<ll, int>> fac;
const ll MOD = 998244353LL;
vi bmct;
vll pw2;

void solve() {
	ll m;
	cin >> n >> m;
	vll a(n);
	pw2 = vll(n+1);
	pw2[0] = 1;
	for (int i = 1;i <= n;i++) {
		pw2[i] = pw2[i-1] * 2 % MOD;
	}
	for (int i = 0;i < n;i++) cin >> a[i];
	if (m == 1) {
		int ct = 0;
		for (int i = 0;i < n;i++) ct += (int)(a[i] == 1);
		cout << (pw2[ct] - 1 + MOD)%MOD << endl;
		return;
	}

	fac = vector<pair<ll, int>>();
	int ct = 0;
	while (m%2 == 0) {
		m /= 2;
		ct++;
	}
	if (ct) fac.push_back(pair<ll, int>(2, ct));
	for (ll p = 3;p*p <= m;p += 2) {
		int ct = 0;
		while (m%p == 0) {
			m /= p;
			ct++;
		}
		if (ct) fac.push_back(pair<ll, int>(p, ct));
		if (m == 1) break;
	}
	if (m != 1) fac.push_back(pair<ll, int>(m, 1));
	fl = fac.size();
	dp = vll(1 << fl);
	dp[(1 << fl)-1] = 1;
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

	for (int idx = (1<<fl)-1;idx >= 0;idx--) {
		if (bmct[idx]) {
			for (int bm = 0;bm < (1 << fl);bm++) {
				dp[bm] += (pw2[bmct[idx]] - 1 + MOD) % MOD * dp[bm | idx] % MOD;
				dp[bm] %= MOD;
			}
		}
	}
	cout << dp[0] << endl;

}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    solve();
    return 0;
}