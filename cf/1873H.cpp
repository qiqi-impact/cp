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

vvi g;
vi v, m, mark;
bool ret;
int depth;

int dfs(int cur, int p) {
	if (mark[cur] != -1) {
		if (v[cur] < m[cur]) ret = true;
		return mark[cur];
	}
	mark[cur] = depth++;
	for (auto x : g[cur]) {
		if (x != p) {
			int q = dfs(x, cur);
			if (q <= mark[cur]) {
				if (v[cur] < m[cur]) ret = true;
				return q;
			}
		}
	}
	return INT_MAX;
}

void solve() {
    int n, a, b;
	cin >> n >> a >> b;
	a--; b--;
	g = vvi(n);
	v = vi(n, INT_MAX);
	m = vi(n, INT_MAX);
	mark = vi(n, -1);
	depth = 1;
	ret = false;
	for (int i = 0;i < n;i++) {
		int x, y;
		cin >> x >> y;
		x--; y--;
		g[x].push_back(y);
		g[y].push_back(x);
	}
	deque<int> md;
	md.push_back(a);
	m[a] = 0;
	while (!md.empty()) {
		int cur = md.front();
		md.pop_front();
		for (auto x : g[cur]) {
			if (m[x] > 1 + m[cur]) {
				m[x] = 1 + m[cur];
				md.push_back(x);
			}
		}
	}
	deque<int> vd;
	vd.push_back(b);
	v[b] = 0;
	while (!vd.empty()) {
		int cur = vd.front();
		vd.pop_front();
		for (auto x : g[cur]) {
			if (v[x] > 1 + v[cur]) {
				v[x] = 1 + v[cur];
				vd.push_back(x);
			}
		}
	}
	dfs(0, -1);
	cout << (ret ? "YES" : "NO") << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}