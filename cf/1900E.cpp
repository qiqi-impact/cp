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

vvi adj;
vvi adj_rev;
vi order;
vi component;
vvi components;
vi used;
vector<pair<int, ll>> mx;
vector<set<int>> cond_adj;
vector<pair<int, ll>> val;

void dfs1(int v) {
	used[v] = 1;
	for (auto u : adj[v]) {
		if (!used[u]) {
			dfs1(u);
		}
	}
	order.push_back(v);
}

void dfs2(int v) {
	used[v] = 1;
	component.push_back(v);
	for (auto u : adj_rev[v]) {
		if (!used[u]) {
			dfs2(u);
		}
	}
}

pair<int, ll> dfs3(int i) {
	if (mx[i].first != 0) return mx[i];
	for (auto x : cond_adj[i]) {
		auto y = dfs3(x);
		mx[i] = max(mx[i], y);
	}
	mx[i].first += val[i].first;
	mx[i].second += val[i].second;
	return mx[i];
}

void solve() {
    int n, m;
	cin >> n >> m;
	vi a(n);
	for (int i = 0;i < n;i++) cin >> a[i];
	// dbg(a);
	adj = vvi(n);
	adj_rev = vvi(n);
	order = vi();
	component = vi();
	components = vvi();
	used = vi(n, 0);
	for (int i = 0;i < m;i++) {
		int x, y;
		cin >> x >> y;
		x--; y--;
		adj[x].push_back(y);
		adj_rev[y].push_back(x);
	}
	// dbg(adj);
	for (int i = 0;i < n;i++) {
		if (!used[i]) {
			dfs1(i);
		}
	}
	reverse(order.begin(), order.end());
	used = vi(n, 0);
	for (auto v : order) {
		if (!used[v]) {
			dfs2(v);
			components.push_back(component);
			component = vi();
		}
	}

	// dbg(components);

	int cs = components.size();
	map<int, int> itoc;
	val = vector<pair<int, ll>>(cs);
	mx = vector<pair<int, ll>>(cs, {0, 0});
	for (int i = 0;i < cs;i++) {
		for (auto x : components[i]) {
			itoc[x] = i;
			val[i].first++;
			val[i].second -= a[x];
		}
	}

	// dbg(val);
	cond_adj = vector<set<int>>(cs);
	vi ind(cs);
	for (int i = 0;i < n;i++) {
		for (auto x : adj[i]) {
			if (itoc[i] != itoc[x] && !cond_adj[itoc[i]].contains(itoc[x])) {
				cond_adj[itoc[i]].insert(itoc[x]);
				ind[itoc[x]]++;
			}
		}
	}
	// dbg(ind, cond_adj);
	pair<int, ll> ret;
	for (int i = 0;i < cs;i++) {
		if (ind[i] == 0) ret = max(ret, dfs3(i));
	}
	cout << ret.first << " " << -ret.second << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}