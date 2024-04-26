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
	ll ans, ct;
	ct = 0;
	ans = 0;
	int n;
	cin >> n;
	vi ord(n), perm(n), av(n), used(n);
	vll a(n);
	for (int i = 0;i < n;i++) {
		ord[i] = i;
		cin >> a[i];
	}
	for (int i = 0;i < n;i++) {
		cin >> perm[i];
		perm[i]--;
	}
	sort(ord.begin(), ord.end(), [&](int x, int y) {
		return a[x] > a[y];
	});
	int op = 0;
	int cur = 0;
	for (int l = 1;l <= n;l++) {
		if (l >= 2) {
			av[perm[l-2]] = 1;
			if (used[perm[l-2]]) cur--;
		}
		while (op != n && cur < l) {	
			int v = ord[op];
			used[v] = 1;
			if (!av[v]) cur++;
			op++;
		}
		if (cur == l) {
			ll x = a[ord[op-1]];
			
			if (x * l > ans) {
				ans = x * l;
				ct = l;
			}
		}
	}
	cout << ans << " " << ct << endl;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
	int t;
	cin >> t;
    while (t--) solve();
    return 0;
}