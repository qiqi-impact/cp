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

using ppp = pair<pair<ll, ll>, pii>;

void solve() {
    int n, m;
	ll p;
	cin >> n >> m >> p;
	vll w(n);
	for (int i = 0;i < n;i++) cin >> w[i];
	vector<unordered_map<int, int>> g(n);
	for (int i = 0;i < m;i++) {
		int a, b, s;
		cin >> a >> b >> s;
		a--;
		b--;
		if (!g[a].contains(b) || g[a][b] > s) {
			g[a][b] = s;
		}
	}
	map<pii, pair<ll, ll>> dist;
	auto comp = [&](ppp &a, ppp &b) {
		return a.first > b.first;
	};
	priority_queue<ppp, vector<ppp>, decltype(comp)> dijk(comp);
	dijk.push(ppp(pair<ll, ll>(0LL, -p), pii(0, w[0])));
	dist[pii(0, w[0])] = pair<ll, ll>(0LL, -p);
	while (!dijk.empty()) {
		auto [y, x] = dijk.top();
		dijk.pop();
		
		if (dist[x] != y) continue;

		if (x.first == n-1) {
			cout << y.first << endl;
			return;
		}
		
		for (auto [nei, cost] : g[x.first]) {
			ll nyf = y.first;
			ll nys = -y.second - cost;
			if (nys < 0) {
				ll pf = (ll)(-nys + x.second - 1) / x.second;
				nyf += pf;
				nys += (ll)pf * x.second;
			}
			int nxf = nei;
			int nxs = max(x.second, (int)w[nei]);

			pii P = pii(nxf, nxs);
			pair<ll, ll> Q = pair<ll, ll>(nyf, -nys);

			if (!dist.contains(P) || dist[P] > Q) {
				dist[P] = Q;
				dijk.push(ppp(Q, P));
			}
		}
	}
	cout << -1 << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}