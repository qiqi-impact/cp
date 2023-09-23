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

vvi g, nx, memo;
string s;

void dfs(int node, int p, int o) {
	nx[node][o] = p;
	for (auto x : g[node]) {
		if (x != p) {
			dfs(x, node, o);
		}
	}
}

int dp(int x, int y) {
	if (x > y) return dp(y, x);
	if (x == y) return 1;
	if (memo[x][y] != -1) return memo[x][y];
	int ret = 0;
	if (s[x] == s[y]) {
		if (y == nx[x][y]) ret = 2; else
		ret = 2 + dp(nx[x][y], nx[y][x]);
	} else {
		ret = max(dp(x, nx[y][x]), dp(nx[x][y], y));
	}
	memo[x][y] = ret;
	return ret;
}

void solve() {
    int n;
	cin >> n;
	cin >> s;
	g = vvi(n);
	nx = vvi(n, vi(n));
	for (int i = 0;i < n-1;i++) {
		int a, b;
		cin >> a >> b;
		a--; b--;
		g[a].push_back(b);
		g[b].push_back(a);
	}

	for (int i = 0;i < n;i++) dfs(i, -1, i);
	
	int ans = 1;

	memo = vvi(n, vi(n, -1));

	for (int i = 0;i < n;i++) {
		for (int j = 0;j < n;j++) {
			if (i != j)
			ans = max(ans, dp(i, j));
		}
	}
	cout << ans << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}