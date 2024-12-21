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

ll tot(ll x, ll u) {
	return u * x - (x * (x - 1) / 2);
}

void solve() {
    int n;
	cin >> n;
	vll a(n), pf(n+1);
	for (int i = 0;i < n;i++) {
		cin >> a[i];
	}
	pf[0] = 0;
	for (int i = 0;i < n;i++) {
		pf[i+1] = pf[i] + a[i];
	}
	int q;
	cin >> q;
	vi ret;
	for (int i = 0;i < q;i++) {
		int l;
		ll u;
		cin >> l >> u;
		l--;
		int a = l, b = n-1;
		// dbg(i, a, b);
		ll best = (ll)-1e18;
		int bi = 0;
		while (a <= b) {
			int mi = a + (b - a) / 2;
			// dbg(mi);
			ll x = pf[mi+1] - pf[l];
			if (x == u) {
				bi = mi;
				break;
			} else if (x < u) {
				if (tot(x, u) > best) {
					best = tot(x, u);
					bi = mi;
				} else if (tot(x, u) == best) {
					bi = min(bi, mi);
				}
				a = mi + 1;
			} else {
				if (tot(x, u) > best) {
					best = tot(x, u);
					bi = mi;
				} else if (tot(x, u) == best) {
					bi = min(bi, mi);
				}
				b = mi - 1;
			}
		}
		ret.push_back(bi + 1);
	}
	for (auto x : ret) {
		cout << x << " ";
	}
	cout << endl;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}