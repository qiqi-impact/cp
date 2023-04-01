#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
using vi = vector<int>;
using vvi = vector<vector<int>>;

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
		pr("{",x.f,", ",x.s,"}"); 
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

int diff(vi &freq) {
	int mn = 10, mx = -10;
	for (int i = 0;i < 10;i++) {
		if (freq[i] > 0) {
			mn = min(mn, i);
			mx = max(mx, i);
		}
	}
	return mx - mn;
}

void dfs(ll l, ll r, int dig, ll sofar, vi &freq, int &ans, ll &best) {
	int v = diff(freq);
	if (v >= ans) return;

	if (dig == -1) {
		ans = v;
		best = sofar;
	}

	ll m = 1;
	for (int i = 0;i < dig;i++) m *= 10;

	for (int i = 0;i < 10;i++) {
		if (l <= sofar + m - 1 && sofar <= r) {
			freq[i]++;
			dfs(l, r, dig-1, sofar, freq, ans, best);
			freq[i]--;
		}
		sofar += m;
	}
}

ll solve() {
    ll l, r;
	cin >> l >> r;
	ll x = 1;
	for (int i = 1;i <= 18;i++) {
		x *= 10;
		if (x-1 >= l && x-1 <= r) {
			return x-1;
		}
	}
	int ans = 1e9;
	ll best = 0;

	int dig = 0;
	ll cur = 10;
	while (cur <= l) {
		dig++;
		cur *= 10;
	}
	vi freq(10, 0);

	dfs(l, r, dig, 0, freq, ans, best);
	return best;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) cout << solve() << endl;
    return 0;
}