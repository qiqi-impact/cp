#include <bits/stdc++.h>

#define sz(x) (x).size()
#define pb push_back
#define all(x) (x).begin(), (x).end()

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

int solve() {
    int n, m;
	cin >> n >> m;

	vvi e;

	set<int> colors;
	unordered_map<int, int> norm;
	unordered_map<int, set<int>> stv;
	unordered_map<int, set<int>> vts;

	unordered_map<int, vvi> g;

	for (int i = 0;i < m;i++) {
		int x, y, c;
		cin >> x >> y >> c;
		x--;
		y--;
		e.push_back({x, y, c});
		colors.insert(c);
		g[x].push_back({y, c});
		g[y].push_back({x, c});
	}

	int src, dst;
	cin >> src >> dst;
	src--;
	dst--;
	if (src == dst) return 0;

	int ct = 0;
	for (auto x : colors) {
		norm[x] = ct++;
	}

	for (auto p : e) {
		int x = p[0];
		int y = p[1];
		int c = p[2];
		int d = norm[c];
		stv[d].insert(x);
		stv[d].insert(y);
		vts[x].insert(d);
		vts[y].insert(d);
	}

	// unordered_map<int, set<int>> sg;

	// for (auto [x, y, c] : e) {
		
	// }


	map<int, int> dist;
	deque<int> q;

	q.push_back(src);
	dist[src] = 0;

	// for (auto x : vts[src]) {
	// 	q.push_back(x);
	// 	dist[x] = 1;
	// }

	while (!q.empty()) {
		int cur = q.front();
		q.pop_front();
		for (auto p : g[cur]) {
			int o = p[0];
			int c = p[1];
			for (auto v : stv[norm[c]]) {
				if (!dist.count(v)) {
					dist[v] = dist[cur] + 1;
					q.push_back(v);
					if (v == dst) {
						return dist[v];
					}
				}
			}
		}
	}
	return -1;

}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    int t;
    cin >> t;
    while (t--) cout << solve() << endl;
    return 0;
}