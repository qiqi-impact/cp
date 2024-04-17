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

const int MXRANGE = 10;
vvll dmg;
int n, m, k;
vll pw3;

void solve() {
	cin >> n >> m >> k;
	vector<pii> path;
	for (int i = 0;i < n;i++) {
		string s;
		cin >> s;
		for (int j = 0;j < m;j++) {
			if (s[j] == '#') path.push_back(pii(i, j));
		}
	}
	
	dmg = vvll();
	for (int i = 0;i < k;i++) {
		int x, y;
		ll p;
		vll v(MXRANGE+1);
		cin >> x >> y >> p;
		x--; y--;
		for (auto &[xx, yy] : path) {
			for (int j = 0;j < MXRANGE+1;j++) {
				if (j*j >= (x-xx)*(x-xx) + (y-yy)*(y-yy)) {
					v[j] += p;
				}
			}
		}
		dmg.push_back(v);
	}

	vll dp(1 << MXRANGE);
	for (int idx = 0;idx < k;idx++) {
		for (int bm = (1 << MXRANGE) - 1;bm >= 0;bm--) {
			dp[bm] += dmg[idx][0];
			for (int j = 0;j < MXRANGE;j++) {
				if ((bm >> j) & 1) {
					ll diff = dmg[idx][j+1] - pw3[j+1];
					dp[bm] = max(dp[bm], diff + dp[bm ^ (1 << j)]);
				}
			}
		}
	}
	cout << *max_element(dp.begin(), dp.end()) << '\n';
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    int t;
    cin >> t;

	pw3 = vll(MXRANGE+1);
	pw3[0] = 1;
	for (int i = 1;i <= MXRANGE;i++) pw3[i] = pw3[i-1] * 3;

    while (t--) solve();
    return 0;
}