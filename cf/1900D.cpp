//fail

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

const int MXN = 100001;
vi dd[MXN];
vvi ind;

void solve() {
    int n;
	cin >> n;
	vi a(n);
	int mx = 0;
	for (int i = 0;i < n;i++) {
		cin >> a[i];
		mx = max(mx, a[i]);
	}
	sort(a.begin(), a.end());
	ind = vvi(mx+1);
	for (int i = 0;i < n;i++) {
		for (auto x : dd[a[i]]) {
			ind[x].push_back(i);
		}
	}
	ll ret = 0;
	vll ct(mx+1);
	for (int i = mx;i >= 1;i--) {
		for (int j = 0;j < ind[i].size();j++) {
			int x = ind[i][j];
			ct[i] += (ll)j * (n - 1 - x);
		}
		for (int j = 2*i;j <= mx;j += i) {
			ct[i] -= ct[j];
		}
		ret += ct[i] * i;
	}
	cout << ret << endl;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    int t;
    cin >> t;

	for (int i = 1;i < MXN;i++) {
		for (int j = i;j < MXN;j += i) {
			dd[j].push_back(i);
		}
	}

    while (t--) solve();
    return 0;
}