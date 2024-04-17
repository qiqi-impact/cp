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

vvi a, b;
int n, m;

bool can(int x) {
	b[0][0] = 1;
	for (int i = 0;i < n;i++) {
		for (int j = 0;j < m;j++) {
			if (i+j == 0) continue;
			b[i][j] = 0;
			if (a[i][j]%x != 0) continue;
			int ct = 0;
			if (i > 0 && b[i-1][j]) {
				b[i][j] = 1;
			}
			if (j > 0 && b[i][j-1]) {
				b[i][j] = 1;
			}
		}
	}
	return b[n-1][m-1] == 1;
}

void solve() {
	cin >> n >> m;
	a = vvi(n, vi(m));
	b = vvi(n, vi(m));
	for (int i = 0;i < n;i++) {
		for (int j = 0;j < m;j++) {
			cin >> a[i][j];
		}
	}
	int x = gcd(a[0][0], a[n-1][m-1]);

	vi factors;
	for (int i = 1;i <= 1000;i++) {
		if (x%i == 0) {
			factors.push_back(i);
			factors.push_back(x/i);
		}
	}

	sort(factors.rbegin(), factors.rend());

	for (auto x: factors) {
		if (can(x)) {
			cout << x << endl;
			return;
		}
	}
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}