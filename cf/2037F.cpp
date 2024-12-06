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

int n, k;
ll m;
vector<ll> h;
vector<ll> x;

bool can(int t) {
	ll mn = -2e12, mx = 2e12;
	map<ll, int> ev;
	for (int i = 0;i < n;i++) {
		if (h[i] > t * m) continue;
		ll diff = m - (h[i] + t - 1) / t;
		ev[x[i] - diff]++;
		ev[x[i] + diff + 1]--;
	}
	int cur = 0;
	for (auto [a, b] : ev) {
		cur += b;
		if (cur >= k) return true;
	}
	return false;
}

ll solve() {
	cin >> n >> m >> k;
	h = vector<ll>(n);
	x = vector<ll>(n);
	for (int i = 0;i < n;i++) cin >> h[i];
	for (int i = 0;i < n;i++) cin >> x[i];
	ll l = 1, r = 1e9;
	if (!can(r)) {
		return -1;
	}
	while (l < r) {
		int mi = (l + r) / 2;
		if (can(mi)) {
			r = mi;
		} else {
			l = mi + 1;
		}
	}
	return r;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    int t;
    cin >> t;
    while (t--) cout << solve() << endl;
    return 0;
}