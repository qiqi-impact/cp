#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
using vi = vector<int>;
using vvi = vector<vi>;
using vll = vector<ll>;
using vvll = vector<vll>;
using pii = pair<int, int>;
using vvvll = vector<vvll>;

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

ll MOD = (ll)1e9+7;

ll inv(ll a) {
  return a <= 1 ? a : MOD - (long long)(MOD/a) * inv(MOD % a) % MOD;
}

void solve() {
	int n, r, g, b;
	cin >> n >> r >> g >> b;

	// vvll comb(n+1, vll(n+1));
	// comb[0][0] = 1;
	// for (int i = 1;i <= n;i++) {
	// 	for (int j = 0;j <= i;j++) {
	// 		comb[i][j] = comb[i-1][j];
	// 		if (j > 0) comb[i][j] += comb[i-1][j-1];
	// 		comb[i][j] %= MOD;
	// 	}
	// }

	vll fac(n+1);
	fac[0] = 1;
	for (int i = 1;i <= n;i++) fac[i] = fac[i-1] * i % MOD;

	vvvll dp(n+1, vvll(r+1, vll(g+1)));
	dp[0][r][g] = 1;
	for (int i = 1;i <= n;i++) {
		for (int rr = 0;rr <= r;rr++) {
			for (int gg = 0;gg <= g;gg++) { 
				int bb = b - ((ll)(i-1) * i / 2 - (r - rr) - (g - gg));
				if (bb > b) continue;
				for (int m = 1;m < 8;m++) {
					int amt = __builtin_popcount(m);
					if (i % amt) continue;
					int t = i / amt;
					if (rr < t && (1 & m >> 0)) continue;
					if (gg < t && (1 & m >> 1)) continue;
					if (bb < t && (1 & m >> 2)) continue;
					int R = rr, G = gg;
					if (1 & m >> 0) R -= t;
					if (1 & m >> 1) G -= t;
					ll comb = fac[i];
					for (int j = 0;j < amt;j++) {
						comb *= inv(fac[t]);
						comb %= MOD;
					}
					// dbg(i, t, amt, comb, fac[t] * inv(fac[t]) % MOD);
					dp[i][R][G] += dp[i-1][rr][gg] * comb;
					dp[i][R][G] %= MOD;
				}
			}
		}
	}
	ll ret = 0;
	for (int i = 0;i <= r;i++) {
		for (int j = 0;j <= g;j++) {
			ret += dp[n][i][j];
		}
	}
	cout << (ret % MOD) << endl;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
	solve();
    return 0;
}