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
	// vvi v;
	vvi ev;
	for (int i = 0;i < n;i++) {
		int a, b, c, d;
		cin >> a >> b >> c >> d;
		// v.push_back({a,b,c,d});
		ev.push_back({d, 1});
		ev.push_back({b, 2});
		ev.push_back({a, 0});
	}
	int k;
	cin >> k;
	vi q;
	for (int i = 0;i < k;i++) {
		int x;
		cin >> x;
		ev.push_back({x, 3});
		q.push_back(x);
	}
	sort(ev.rbegin(), ev.rend());

	int st = 0;
	int mx = 0;
	map<int, int> ans;

	for (auto v : ev) {
		int x = v[0];
		int y = v[1];
		if (y == 3) {
			ans[x] = max(x, mx);
		} else if (y == 2) {
			// st++;
		} else if (y == 1) {
			st++;
			if (mx == 0) mx = x;
		} else {
			st--;
			if (st == 0) mx = 0;
		}
	}

	for (auto x : q) cout << ans[x] << " ";
	cout << endl;

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}