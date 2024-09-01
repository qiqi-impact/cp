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
    int n,q;
	cin >> n >> q;
	vi ct(n+1, 0), pf(n+2, 0);
	int x;
	for (int i = 0;i < n;i++) {
		cin >> x;
		ct[x]++;
	}
	for (int i = 0;i <= n;i++) {
		pf[i+1] = pf[i] + ct[i];
	}
	int lmt = n%2 ? (n+1)/2 : (n+2)/2;

	map<int, int> ans;
	vi ret;

	while (q--) {
		int qq;
		cin >> qq;
		if (ans.count(qq)) {
			cout << ans[qq] << " ";
			continue;
		}
		int l = 0, r = qq-1;
		// cout << l << r << endl;
		while (l < r) {
			// cout << l << r << endl;
			int mi = l + (r - l) / 2;
			int c = 0;
			for (int x = 0;x <= n;x += qq) {
				c += pf[min(n+1, x+mi+1)] - pf[x];
			}
			if (c < lmt) {
				l = mi + 1;
			} else {
				r = mi;
			}
		}
		ans[qq] = r;
		cout << r << " ";
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