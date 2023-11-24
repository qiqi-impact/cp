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

int n;
vvi g;
vll a;
ll ret;

ll dp(int idx, int p) {
	vll dps;
	ll top = a[idx];
	for (auto x : g[idx]) {
		if (x != p) {
			ll y = dp(x, idx);
			dps.push_back(y);
			top = max(top, y);
		}
	}
	sort(dps.rbegin(), dps.rend());
	ll acc = a[idx];
	if (dps.size() >= 2) {
		for (int i = 0;i < dps.size();i++) {
			if (i >= 2 && dps[i] <= 0) break;
			acc += dps[i];
		}
	}
	top = max(top, acc);
	
	acc = a[idx];
	ll ot = 0;
	for (int i = 0;i < dps.size();i++) {
		ot += dps[i];
		if (i == 1) {
			acc = max(acc, ot);
		} else {
			acc = max(acc, ot + a[idx]);
		}
	}
	ret = max(ret, acc);
	return top;
}

void solve() {
	cin >> n;
	a = vll(n);
	for (int i = 0;i < n;i++) {
		cin >> a[i];
	}
	g = vvi(n);
	for (int i = 0;i < n-1;i++) {
		int x, y;
		cin >> x >> y;
		x--; y--;
		g[x].push_back(y);
		g[y].push_back(x);
	}
	ret = 0;
	dp(0, -1);
	ret = max(ret, a[0]);
	cout << ret << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}