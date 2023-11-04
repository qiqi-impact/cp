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
	vi a(n), lstz(32, -1), par(n+1, 0), pp(n+1, 0);
	ll ret = 0;
	for (int i = 0;i < n;i++) {
		int x;
		cin >> x;
		vi clstz(32, -1);
		int ct = __builtin_popcount(x)%2;
		for (int j = 0;j < 32;j++) {
			if (!(1 & (x >> j))) {
				lstz[j] = i;
			}
			clstz[j] = lstz[j];
		}
		par[i+1] = par[i] + ct;
		pp[i+1] = pp[i] + par[i+1]%2;
		sort(clstz.begin(), clstz.end());
		dbg(i);
		dbg(clstz);
		dbg(par);
		dbg(pp);
		for (int j = 1;j < 32;j += 2) {
			int od = (clstz[j] >= 0 ? par[clstz[j]] : 0) - (clstz[j-1] >= 0 ? par[clstz[j-1]] : 0);
			int ev = clstz[j] - clstz[j-1] - od;
			int df = (par[i+1]%2) ? od : ev;
			ret += df;
			// if (df && clstz[j] == i) ret--;
			dbg(j, j-1, od, ev, ret);
		}
	}
	cout << ret << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}