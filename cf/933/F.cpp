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
    int n, m, k;
	cin >> n >> m >> k;
	vll a(n), d(m), f(k);

	

	for (int i = 0;i < n;i++) {
		cin >> a[i];
	}
	for (int i = 0;i < m;i++) {
		cin >> d[i];
	}
	for (int i = 0;i < k;i++) {
		cin >> f[i];
	}
	sort(f.begin(), f.end());

	map<int, int> gapct;
	vll gs;
	ll mx = 0;
	for (int i = 0;i < n-1;i++) {
		gapct[a[i+1] - a[i]]++;
		mx = max(mx, a[i+1] - a[i]);
		gs.push_back(a[i+1] - a[i]);
	}
	if (gapct[mx] > 1) {
		// dbg("gap", mx);
		return mx;
	}

	sort(gs.begin(), gs.end());
	ll m2 = gs.size() > 1 ? gs[gs.size() - 2] : 0;


	for (int i = 0;i < n-1;i++) {
		if (a[i+1] - a[i] == mx) {
			ll tgt = (a[i+1] + a[i]) / 2;
			ll md = (ll)1e18;
			for (auto x : d) {
				int idx = lower_bound(f.begin(), f.end(), tgt - x) - f.begin();
				if (idx < f.size()) {
					if (a[i] < f[idx] + x && f[idx] + x < a[i+1]) {
						ll m = (ll)-1e18;
						m = max(m, a[i+1] - f[idx] - x);
						m = max(m, f[idx] + x - a[i]);
						md = min(md, m);
					}
				}
				if (idx > 0) {
					if (a[i] < f[idx - 1] + x && f[idx - 1] + x < a[i+1]) {
						ll m = (ll)-1e18;
						m = max(m, a[i+1] - f[idx - 1] - x);
						m = max(m, f[idx - 1] + x - a[i]);
						md = min(md, m);
					}
				}
				// dbg(i, mx, x, tgt, md);
			}
			// dbg(mx, m2, md);
			return min(mx, max(m2, md));
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