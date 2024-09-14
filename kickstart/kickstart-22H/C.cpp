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

int dfs(vector<vector<int>> &g, vector<int> &cap, vector<int> &dp, int idx) {
	if (dp[idx] != -1) return dp[idx];
	int ret = 1;
	for (auto &x : g[idx]) {
		if (cap[x] < cap[idx]) {
			ret += dfs(g, cap, dp, x);
		}
	}
	dp[idx] = ret;
	return ret;
}

int solve() {
	int n;
	cin >> n;
	vector<int> cap(n);
	for (int i = 0;i < n;i++) cin >> cap[i];
    vector<vector<int>> g(n);
	for (int i = 0;i < n-1;i++) {
		int a, b;
		cin >> a >> b;
		a--; b--;
		g[a].push_back(b);
		g[b].push_back(a);
	}
	// dbg(g);
	// vector<bool> vis(n);
	vector<int> ord;
	vector<int> dp(n, -1);
	for (int i = 0;i < n;i++) ord.push_back(i);
	sort(ord.begin(), ord.end(), [&](int i, int j) {
		return cap[i] > cap[j];
	});

	// for (auto x : ord) cout << x << endl;
	int ret = 0;
	for (int i = 0;i < n;i++) {
		int idx = ord[i];
		if (dp[idx] == -1) {
			ret = max(ret, dfs(g, cap, dp, idx));
		}
	}
	return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    for (int i = 1;i <= t;i++) {
        cout << "Case #" << i << ": " << solve() << endl;
    }
    return 0;
}