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
ll avg;
vll a, ss;

ll ssc(int idx, int p) {
	ll ret = a[idx] - avg;
	for (auto x : g[idx]) {
		if (x != p) {
			ret += ssc(x, idx);
		}
	}
	if (ret > 0) {
		cout << (idx+1) << " " << (p+1) << " " << ret << endl;
	}
	return ret;
}

void dist(int idx, int p) {
	for (auto x : g[idx]) {
		if (x != p && ss[x] < 0) {
			cout << (idx+1) << " " << (x+1) << " " << -ss[x] << endl;
		}
	}
	for (auto x : g[idx]) {
		if (x != p) {
			dist(x, idx);
		}
	}
}

void solve() {
	int n;
	cin >> n;
	a = vll(n);
	ss = vll(n);
	ll tot = 0;
	for (int i = 0;i < n;i++) {
		cin >> a[i];
		tot += a[i];
	}
	avg = tot / n;
	g = vvi(n);

	for (int i = 0;i < n-1;i++) {
		int x, y;
		cin >> x >> y;
		x--;y--;
		g[x].push_back(y);
		g[y].push_back(x);
	}

	ssc(0, -1);
	dist(0, -1);
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}