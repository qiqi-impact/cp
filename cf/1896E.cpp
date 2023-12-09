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

vi fw;
int n;

void inc(int i, int amt) {
	for (;i <= 2 * n;i += i & -i) {
		fw[i] += amt;
	}
}

int prefix_sum(int i) {
	int ret = 0;
	for(;i > 0; i -= i & -i) {
		ret += fw[i];
	}
	return ret;
}

void solve() {
    cin >> n;
	vi a(n);
	vector<pii> path;
	for (int i = 0;i < n;i++) {
		cin >> a[i];
		a[i]--;
		if (a[i] >= i) {
			path.push_back(pii(i, a[i]));
			path.push_back(pii(i + n, a[i] + n));
		} else {
			path.push_back(pii(i, a[i] + n));
		}
	}
	sort(path.rbegin(), path.rend());
	fw = vi(2 * n + 1);
	vi ret(n);
	// dbg(path);
	for (auto [l, r] : path) {
		if (l < n) {
			int v = (prefix_sum(r+1) - prefix_sum(l));
			// dbg(l, r, v, a[l]);
			ret[a[l]] = r - l - v;
		}
		inc(r+1, 1);
	}
	for (auto x : ret) cout << x << " ";
	cout << endl;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}