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
	vi a(n), b, c;
	int mxi = 0, mni = 0;
	for (int i = 0;i < n;i++) {
		cin >> a[i];
		if (a[i] > a[mxi]) mxi = i;
		if (a[i] < a[mni]) mni = i;
		if (a[i] < 0) b.push_back(i);
		if (a[i] > 0) c.push_back(i);
	}

	int bd = 0, cd = 0;
	if (b.size() && c.size()) {
		if (-a[mni] < a[mxi]) bd = 5;
		cd = 5-bd;
	}

	if (!b.size() || cd+b.size() < bd+c.size()) {
		cout << (n-1+cd+b.size()) << endl;
		for (int i = 0;i < cd;i++) cout << (1+mxi) << " " << (1+mxi) << endl;
		for (auto x: b) cout << (1+x) << " " << (1+mxi) << endl;
		for (int i = 0;i < n-1;i++) cout << i+2 << " " << i+1 << endl;
	} else {
		cout << (n-1+bd+c.size()) << endl;
		for (int i = 0;i < bd;i++) cout << (1+mni) << " " << (1+mni) << endl;
		for (auto x: c) cout << (1+x) << " " << (1+mni) << endl;
		for (int i = n-1;i >= 1;i--) cout << i << " " << i+1 << endl;
	}
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}