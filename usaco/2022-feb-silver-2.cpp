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

void solve() {
    int n;
	cin >> n;
	int tx, ty;
	cin >> tx >> ty;
	
	unordered_map<ll, unordered_map<ll, unordered_map<int, int>>> m;
	m[0][0][0] = 1;
	for (int i = 0;i < n/2;i++) {
		unordered_map<ll, unordered_map<ll, unordered_map<int, int>>> nm;
		ll x, y;
		cin >> x >> y;
		for (const auto &p : m) {
			ll cx = p.first;
			auto &mcx = m[cx];
			for (const auto &pp : mcx) {
				ll cy = pp.first;
				auto &mcxcy = mcx[cy];
				auto &f = nm[cx][cy];
				auto &g = nm[cx+x][cy+y];
				for (const auto &tt : mcxcy) {
					int t = tt.first;
					f[t] += mcxcy[t];
					g[t+1] += mcxcy[t];
				}
			}
		}
		m = nm;
	}

	unordered_map<ll, unordered_map<ll, unordered_map<int, int>>> q;
	q[0][0][0] = 1;
	for (int i = n/2;i < n;i++) {
		unordered_map<ll, unordered_map<ll, unordered_map<int, int>>> nq;
		ll x, y;
		cin >> x >> y;
		for (const auto &p : q) {
			ll cx = p.first;
			auto &mcx = q[cx];
			for (const auto &pp : mcx) {
				ll cy = pp.first;
				auto &mcxcy = mcx[cy];
				auto &f = nq[cx][cy];
				auto &g = nq[cx+x][cy+y];
				for (const auto &tt : mcxcy) {
					int t = tt.first;
					f[t] += mcxcy[t];
					g[t+1] += mcxcy[t];
				}
			}
		}
		q = nq;
	}

	vll ret(n+1, 0);
	for (const auto &p : m) {
		ll cx = p.first;
		ll xx = tx - cx;
		for (const auto &pp : m[cx]) {
			ll cy = pp.first;
			ll yy = ty - cy;
			for (const auto &tt : m[cx][cy]) {
				int t = tt.first;
				for (const auto &vv : q[xx][yy]) {
					int v = vv.first;
					ret[t + v] += (ll)m[cx][cy][t] * q[xx][yy][v];
				}
			}
		}
	}
	for (int i = 1;i <= n;i++) cout << ret[i] << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0); solve();
    return 0;
}