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

void dfs(int idx, vvi &seen, vvi &g, double *ans) {
	if (idx == 9) {
		*ans += 1./362880;
		return;
	}

	for (int i = 0;i < 3;i++) {
		if (
			(seen[i][0] && seen[i][1] && !seen[i][2] && seen[i][0] == seen[i][1]) ||
			(seen[i][0] && seen[i][2] && !seen[i][1] && seen[i][0] == seen[i][2]) ||
			(seen[i][2] && seen[i][1] && !seen[i][0] && seen[i][2] == seen[i][1])
		) {
			return;
		}
	}
	for (int j = 0;j < 3;j++) {
		if (
			(seen[0][j] && seen[1][j] && !seen[2][j] && seen[0][j] == seen[1][j]) ||
			(seen[0][j] && seen[2][j] && !seen[1][j] && seen[0][j] == seen[2][j]) ||
			(seen[2][j] && seen[1][j] && !seen[0][j] && seen[2][j] == seen[1][j])
		) {
			return;
		}
	}
	if (
		(seen[0][0] && seen[1][1] && !seen[2][2] && seen[0][0] == seen[1][1]) ||
		(seen[0][0] && seen[2][2] && !seen[1][1] && seen[0][0] == seen[2][2]) ||
		(seen[2][2] && seen[1][1] && !seen[0][0] && seen[2][2] == seen[1][1])
	) {
		return;
	}
	if (
		(seen[0][2] && seen[1][1] && !seen[2][0] && seen[0][2] == seen[1][1]) ||
		(seen[0][2] && seen[2][0] && !seen[1][1] && seen[0][2] == seen[2][0]) ||
		(seen[2][0] && seen[1][1] && !seen[0][2] && seen[2][0] == seen[1][1])
	) {
		return;
	}
	for (int i = 0;i < 3;i++) for (int j = 0;j < 3;j++) {
		if (!seen[i][j]) {
			seen[i][j] = g[i][j];
			dfs(idx+1, seen, g, ans);
			seen[i][j] = 0;
		}
	}
}

void solve() {
    vvi g(3, vi(3));
	for (int i = 0;i < 3;i++) for (int j = 0;j < 3;j++) {
		cin >> g[i][j];
	}
	vvi seen(3, vi(3, 0));

	double ans = 0;
	dfs(0, seen, g, &ans);
	// cout << ans << endl;
	printf("%0.10f\n", ans);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
	solve();
    return 0;
}