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

const int MX = 222222;
vector<ll> T(MX);

void solve() {
    int n;
	cin >> n;
	vi a(n), inv(n);
	for (int i = 0;i < n;i++) {
		cin >> a[i];
		inv[a[i]] = i;
	}
	int lb = n, rb = -1;
	ll ret = 1;
	for (int i = 0;i < n;i++) {
		int p = inv[i];
		if (p > lb && p < rb) continue;	
		if (i) {
			int left, right, k = 2*i-(rb - lb + 1);
			if (p < lb) {
				left = lb - p;
				right = n - rb;
			} else {
				left = lb - (-1);
				right = p - rb;
			}
			// dbg(left, right, ret, T[k+1], T[k+1-left], T[k+1-right], T[k+1-left-right]);
			ret += T[max(0, k+1)] - T[max(0, k+1-left)] - T[max(0, k+1-right)] + T[max(0, k+1-left-right)];
		}
		lb = min(lb, p);
		rb = max(rb, p);
		if (!i) continue;
	}
	cout << ret << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

	for (int i = 0;i < MX;i++) T[i] = (ll)i * (ll)(i+1) / 2;

    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}