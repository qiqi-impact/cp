#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
using vi = vector<int>;
using vvi = vector<vi>;
using vvvi = vector<vvi>;

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

vvi g;
vi ct;

int dfs(int cur) {
	int ret = 1;
	for (auto x: g[cur]) {
		ret += dfs(x);
	}
	ct[cur] = ret;
	return ret;
}

int ss(int p, int idx, int left, vvi &memo) {
	if (idx == g[p].size()) {
		return 0;
	}
	if (memo[idx][left] != -1) return memo[idx][left];
	int ret = ss(p, idx+1, left, memo);
	if (ct[g[p][idx]] <= left) {
		ret = max(ret, ct[g[p][idx]] + ss(p, idx+1, left - ct[g[p][idx]], memo));
	}
	memo[idx][left] = ret;
	return ret;
}

void solve() {
    int n;
	cin >> n;
	g = vvi(n);
	ct = vi(n);
	for (int i = 0;i < n-1;i++) {
		int x;
		cin >> x;
		g[x-1].push_back(i+1);
	}
	dfs(0);
	int ret = 0;
	for (int i = 0;i < n;i++) {
		vvi memo(g[i].size(), vi((ct[i]-1)/2+1, -1));
		int q = ss(i, 0, (ct[i]-1)/2, memo);
		ret += q * (ct[i]-1-q);
	}
	cout << ret << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
	solve();
    return 0;
}