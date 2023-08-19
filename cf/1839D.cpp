#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
using vi = vector<int>;
using vvi = vector<vi>;
using vvvi = vector<vvi>;
using vll = vector<ll>;
using vvll = vector<vll>;

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

int dp(int idx, int left, vvi &memo, vvi &g) {
	if (memo[idx][left] != -1) {
		return memo[idx][left];
	}
	int n = g.size();
	int ret = 1000;
	if (left == 0) {
		ret = idx != n-2;
	} else {
		for (auto i : g[idx]) {
			ret = min(ret, dp(i, left-1, memo, g) + (i != idx+1));
		}
	}
	memo[idx][left] = ret;
	return ret;
}

void solve() {
    int n;
	cin >> n;
	vi a;
	vvi g(n+2);
	a.push_back(0);
	bool sorted = true;
	for (int i = 0;i < n;i++) {
		int x;
		cin >> x;
		if (x < a[a.size()-1]) sorted = false;
		a.push_back(x);
	}

	if (sorted) {
		for (int i = 0;i < n;i++) cout << 0 << " ";
		cout << endl;
		return;
	}

	a.push_back(n+1);
	for (int i = 0;i < n+2;i++) {
		for (int j = i+1;j < n+1;j++) {
			if (a[i] < a[j]) g[i].push_back(j);
		}
	}
	vvi memo(n+2, vi(n+1, -1));
	
	vi ret;
	for (int i = 1;i <= n;i++) {
		ret.push_back(dp(0, i, memo, g));
	}

	vi ans(n);
	int ptr = 0;
	for (int i = 0;i < n;i++) {
		while (ret[ptr] <= i+1) {
			ptr++;
		}
		ans[i] = n-ptr;
	}
	for (auto x: ans) cout << x << " ";
	cout << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}