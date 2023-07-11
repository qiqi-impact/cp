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

void solve() {
    int n;
    cin >> n;
    vi a(n+1), b(n+1);
    int x;
    for (int i = 0;i < n;i++) {
        cin >> x;
        a[x] = i;
    }
    for (int i = 0;i < n;i++) {
        cin >> x;
        b[x] = i;
    }
    ll ret = 1;
    ll mn = min(a[1], b[1]);
    ret += mn * (mn + 1) / 2;
    ll mx = max(a[1], b[1]);
    ret += (mx - mn - 1) * (mx - mn) / 2;
    ret += (n - 1 - mx) * (n - 1 - mx + 1) / 2;
    // cout << 1 << " " << ret << endl;

    for (int mex = 2;mex <= n;mex++) {
        ll L = min(a[mex], b[mex]);
        ll R = max(a[mex], b[mex]);
        if (!((mn <= a[mex] && a[mex] <= mx) || (mn <= b[mex] && b[mex] <= mx))) {
            ll cur;
            if (mn > R) {
                cur = (mn - R) * (n - mx);
            } else if (mx < L) {
                cur = (L - mx) * (mn + 1);
            } else {
                cur = (mn - L) * (R - mx);
            }
            ret += cur;
        }
        mn = min(mn, L);
        mx = max(mx, R);
    }
    cout << ret << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    solve();
    return 0;
}