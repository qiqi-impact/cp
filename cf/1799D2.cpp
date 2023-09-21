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

void solve() {
    int n, k;
	cin >> n >> k;
	vll dp(k+1, 1e18), a(n), hot(k+1), cold(k+1);
	dp[0] = 0;
	for (int i = 0;i < n;i++) {
		cin >> a[i];
	}
	for (int i = 1;i <= k;i++) {
		cin >> cold[i];
	}
	for (int i = 1;i <= k;i++) {
		cin >> hot[i];
	}
	ll add = 0;
	int mindex = 0;
	for (int i = 0;i < n;i++) {
		ll y = a[i];
		ll x = 0;
		if (i > 0) x = a[i-1];
		if (x == y) {
			ll nadd = add + hot[x];
			ll ndpx = min(dp[x] + nadd, dp[mindex] + add + cold[x]);
			if (dp[mindex] + nadd > ndpx) {
				mindex = x;
			}
			dp[x] = ndpx - nadd;
			add = nadd;
		} else {
			ll nadd = add + cold[y];
			ll ndpx = min(dp[x] + nadd, dp[mindex] + add + cold[y]);
			ndpx = min(ndpx, dp[y] + add + hot[y]);
			if (dp[mindex] + nadd > ndpx) {
				mindex = x;
			}
			dp[x] = ndpx - nadd;
			add = nadd;
		}
		// dbg(dp, add, mindex);
	}
	cout << dp[mindex] + add << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}