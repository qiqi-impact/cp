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

// vll dp;
int n;
int fl;
vll fac;
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

	fac = vll();
	ll mm = m;
	for (ll p = 2;p*p <= mm;p++) {
		ll cum = 1;
		while (mm%p == 0) {
			mm /= p;
			cum *= p;
		}
		if (cum > 1) fac.push_back(cum);
	}
	if (mm != 1) fac.push_back(mm);
	fl = fac.size();
	// dbg(fac);
	bmct = vi(1 << fl);
	
	for (int i = 0;i < n;i++) {
		if (m % a[i] == 0) {
			int bm = 0;
			for (int j = 0;j < fl;j++) {
				if (a[i] % fac[j] == 0) {
					bm ^= 1 << j;
				}
			}
			bmct[bm]++;
		}
	}

	ll ans = 0;
	for (int i = 0; i < (1 << fl); i++) {
		int cur = i;
		int ct = 0;
		while (1) {
			ct += bmct[cur];
			if (!cur) break;
			cur = (cur - 1) & i;
		}
		ll amt = (pw2[ct] - 1 + MOD) % MOD * (__builtin_popcount(i)%2 == fl%2 ? 1 : -1) % MOD;
		ans = ((ans + amt) % MOD + MOD) % MOD;
	}
	cout << ans << endl;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    solve();
    return 0;
}