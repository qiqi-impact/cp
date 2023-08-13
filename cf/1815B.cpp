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
    int n, nl;
	cin >> n;
	cout << "+ " << (n+1) << endl << flush;
	cin >> nl;
	cout << "+ " << (n+2) << endl << flush;
	cin >> nl;
	vi a(n, 0);
	int mx = 0, mxi = 1;
	for (int i = 2;i <= n;i++) {
		cout << "? " << 1 << " " << i << endl << flush;
		cin >> a[i-1];
		if (a[i-1] > mx) {
			mx = a[i-1];
			mxi = i;
		}
	}
	vi d(n, 0);
	for (int i = 1;i <= n;i++) {
		if (i == mxi) continue;
		cout << "? " << mxi << " " << i << endl << flush;
		cin >> d[i-1];
	}
	vi nums;
	for (int i = 0;i < n/2;i++) {
		nums.push_back(i);
		nums.push_back(n-1-i);
	}
	if (n%2) nums.push_back(n/2);
	vi e(n), f(n);
	for (int i = 0;i < n;i++) {
		e[i] = nums[d[i]];
		f[i] = nums[(n-1)-d[i]];
	}
	cout << "! ";
	for (auto x : e) cout << (x+1) << " ";
	for (auto x : f) cout << (x+1) << " ";
	cout << endl << flush;
	cin >> nl;
}

int main() {
    // ios::sync_with_stdio(false);
    // cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}