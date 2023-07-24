#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
using vi = vector<int>;
using vvi = vector<vector<int>>;

namespace op {
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

using namespace op;

void solve() {
    int n;
	cin >> n;
	vi a(n);
	for (int i = 0;i < n;i++) {
		cin >> a[i];
	}

	// dbg(a);

	ll ret = (ll)n * (n+1) * (n-1) / 6;
	for (int i = 0;i < n;i++) {
		int k = -1;
		for (int j = i-1;j >= 0;j--) {
			if (a[j] < a[i]) {
				k = j;
				break;
			}
		}
		// if (k == -1) continue;

		int x = -1;
		for (int j = k-1;j >= 0;j--) {
			if (a[j] > a[i]) {
				x = j;
				break;
			}
		}

		int y = n;
		for (int j = i+1;j < n;j++) {
			if (a[j] < a[i]) {
				y = j;
				break;
			}
		}

		// dbg(x, k, i, y, (ll)(y - i) * (ll)(k - x));
		ret -= (ll)(y - i) * (ll)(k - x);
	}
	cout << ret << endl;
	return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}