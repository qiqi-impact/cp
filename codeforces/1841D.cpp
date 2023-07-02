#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
using vi = vector<int>;
using vvi = vector<vector<int>>;

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
		pr("{",x.f,", ",x.s,"}"); 
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
	int n;
	cin >> n;
	vvi g = vvi(n, vi());
	vi deg = vi(n, 0);
	vvi seg = vvi();
	for (int i = 0;i < n;i++) {
		int x, y;
		cin >> x >> y;
		for (int j = 0;j < seg.size();j++) {
			int a = seg[j][0];
			int b = seg[j][1];
			if (max(a, x) <= min(b, y)) {
				g[i].push_back(j);
				g[j].push_back(i);
				deg[i]++;
				deg[j]++;
			}
		}
		seg.push_back({x,y});
	}
	while (1) {
		int mx = 0;
		int mxi = 0;
		int sm = 0;
		for (int i = 0;i < n;i++) {
			if (deg[i] > mx) {
				mx = deg[i];
				mxi = i;
			}
			sm += deg[i];
		}
		if (mx <= 1) {
			return (n - sm/2*2);
		}
		deg[mxi] = 0;
		for (auto x : g[mxi]) {
			deg[x] = max(0, deg[x]-1);
		}
	}
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) cout << solve() << endl;
    return 0;
}