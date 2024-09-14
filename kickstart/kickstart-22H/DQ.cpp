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

vector<int> p, cyc, lengths;
unordered_map<int, int> cts;
vector<vector<int>> dp;

int dfs(int i, int depth) {
	if (cyc[i] == -1) {
		cyc[i] = depth;
		return depth;
	} else {
		cyc[i] = -1;
		int k = dfs(p[i], depth+1);
		cyc[i] = -1;
		return k;
	}
}

void solve() {
	int n;
	cin >> n;
	p = vector<int>(n);
	cyc = vector<int>(n, 0);

	for (int i = 0;i < n;i++) {
		cin >> p[i];
		p[i]--;
	}

	// lengths.clear();
	cts.clear();
	for (int i = 0;i < n;i++) {
		if (cyc[i] == 0) {
			int l = dfs(i, 0);
			// lengths.push_back(l);
			cyc[i] = l;
			cts[l]++;
		}
	}
	
	lengths.clear();
	for (auto [k, v] : cts) {
		lengths.push_back(k);
		// dbg(k, v);
	}
	// dbg(lengths);

	dp = vector<vector<int>>(lengths.size()+1, vector<int>(n+1, INT_MAX));

	vector<int> ret;

	dp[0][0] = -1;
	for (int i = 1;i <= lengths.size();i++) {
		int l = lengths[i-1];
		int qty = cts[lengths[i-1]];
		dp[i][0] = -1;
		for (int m = 0;m < l;m++) {
			deque<int> q;
			for (int j = m;j <= n;j += l) {
				dp[i][j] = min(dp[i][j], dp[i-1][j]);
				// if (j == l) {
				// 	dp[i][j] = 0;
				// 	continue;
				// }
				while (!q.empty() && q.front() + qty * l < j) {
					q.pop_front();
				}
				while (!q.empty() && (dp[i-1][q.back()] - (q.back() - m)/l >= (dp[i-1][j] - (j - m)/l))) {
					q.pop_back();
				}
				q.push_back(j);
				// dbg(i, m, j, q);
				if (j != 0)
					dp[i][j] = (j - q.front())/l + (dp[i-1][q.front()]);
			}
		}

		// for (int j = 0;j <= n;j++) {
		// 	if (lengths[i-1] == j) dp[i][j] = 0;
		// 	else {
		// 		dp[i][j] = dp[i-1][j];
		// 		if (j > lengths[i-1] && dp[i-1][j - lengths[i-1]] != INT_MAX) {
		// 			dp[i][j] = min(dp[i][j], 1 + dp[i-1][j - lengths[i-1]]);
		// 		}
		// 	}
		// }
	}
	// dbg(dp);

	for (int lev = 1;lev <= n;lev++) {
		ret.push_back(dp[lengths.size()][lev]);
	}

	int mn = 1e9;
	for (int lev = n-1;lev >= 0;lev--) {
		ret[lev] = min(ret[lev], mn + 1);
		mn = min(mn, ret[lev]);
	}

	for (auto x: ret) {
		cout << x << " ";
	}
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    for (int i = 1;i <= t;i++) {
        cout << "Case #" << i << ": ";
		solve();
		cout << endl;
    }
    return 0;
}