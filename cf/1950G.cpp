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
	map<string, vi> gm, wm;
	vi gg(n), ww(n);
	for (int i = 0;i < n;i++) {
		string g, w;
		cin >> g >> w;
		gm[g].push_back(i);
		wm[w].push_back(i);
		int j = 0;
		for (auto &[_, x] : gm) {
			for (auto y : x) {
				gg[y] = j;
			}
			j++;
		}
		j = 0;
		for (auto &[_, x] : wm) {
			for (auto y : x) {
				ww[y] = j;
			}
			j++;
		}
	}
	int ret = 1;
	int FULL = 1 << n;
	vvi dp(FULL, vi(n));
	for (int bm = 0;bm < FULL;bm++) {
		for (int idx = 0;idx < n;idx++) {
			if (((bm >> idx) & 1) == 0) continue;
            if (__builtin_popcount(bm) == 1) {
                dp[bm][idx] = 1;
                continue;
            }
			for (int j = 0;j < n;j++) {
				if (((bm >> j) & 1) == 1 && j != idx && (gg[j] == gg[idx] || ww[j] == ww[idx]) && dp[bm ^ (1 << idx)][j]) {
					dp[bm][idx] = 1;
					ret = max(ret, __builtin_popcount(bm));
                    break;
				}
			}
		}
	}
	cout << (n - ret) << endl;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}