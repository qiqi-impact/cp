#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vvll = vector<vector<ll>>;

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

const ll MX = 1e12;

void solve() {
    int n, m;
	cin >> n >> m;
	// vector<unordered_map<int, int>> g;

	vvll dist(n, vector<ll>(n, MX));
	for (int i = 0;i < n;i++) dist[i][i] = 0;

	for (int i = 0;i < m;i++) {
		int u, v, y;
		cin >> u >> v >> y;
		u--;
		v--;
		dist[u][v] = dist[v][u] = y;
	}

	for (int k = 0;k < n;k++) {
		for (int i = 0;i < n;i++) {
			for (int j = 0;j < n;j++) {
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
			}
		}
	}
	
	vi ord;
	for (int i = 0;i < n;i++) ord.push_back(i);
	sort(ord.begin(), ord.end(), [&](int a, int b) {
		if (dist[0][a] != dist[0][b]) return dist[0][a] < dist[0][b];
		return a < b;
	});

	int fin;
	for (fin = 0;fin < n;fin++) {
		if (ord[fin] == n-1) break;
	}

	if (dist[0][n-1] == MX) {
		cout << "inf" << endl;
		return;
	}

	cout << dist[0][n-1] << " " << fin << endl;

	vi inc(n, 0);
	for (int i = 0;i < fin;i++) {
		int v = ord[i];
		inc[v] = 1;
		for (int i = 0;i < n;i++) {
			cout << inc[i];
		}
		cout << " " << (dist[0][ord[i+1]] - dist[0][ord[i]]) << endl;
	}
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    // int t;
    // cin >> t;
    // while (t--) solve();
	solve();
    return 0;
}