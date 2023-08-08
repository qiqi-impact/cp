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
    int n, m;
	cin >> n >> m;
	string s;
	int a = 0, b = 0;
	for (int i = 0;i < n;i++) {
		cin >> s;
		int cur = 0, mn = 0;
		for (int j = 0;j < m;j++) {
			cur += s[j] == '1';
			if (mn < m/4 && j > 0 && s[j] == '1' && s[j-1] == '1') {
				cur -= 2;
				mn++;
				j++;
				if (j < m) cur += s[j] == '1';
			}
		}
		mn += cur;

		cur = 0;
		int mx = 0, t = 0;
		for (int j = 0;j < m;j++) {
			cur += s[j] == '1';
			if (mx < m/4 && j > 0 && !(s[j] == '1' && s[j-1] == '1')) {
				t++;
				cur -= (s[j] == '1');
				cur -= (s[j-1] == '1');
				mx += (s[j] == '1' || s[j-1] == '1');
				j++;
				if (j < m) cur += s[j] == '1';
			}
		}
		if (t < m/4) mx -= (m/4 - t);
		mx += cur;

		a += mn;
		b += mx;
	}
	cout << a << " " << b << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
	solve();
    return 0;
}