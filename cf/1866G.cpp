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

vi a, d, ord;
int n;

bool can(int x) {
	vi f(n, 0);
	set<int> avail;
	for (int i = 0;i < n;i++) avail.insert(i);
	for (auto idx : ord) {
		int cur = a[idx];
		auto l = lower_bound(avail.begin(), avail.end(), idx-d[idx]);
		while (cur) {
			if (l == avail.end()) return false;
			int amt = min(cur, x - f[*l]);
			f[*l] += amt;
			auto r = next(l);
			if (f[*l] == x) {
				avail.erase(l);
			}
			l = r;
			cur -= amt;
		}
	}
	return true;
}

void solve() {
    cin >> n;
	a = vi(n);
	d = vi(n);
	ord = vi(n);
	ll sm = 0;
	for (int i = 0;i < n;i++) {
		cin >> a[i];
		sm += a[i];
	}
	for (int i = 0;i < n;i++) {
		cin >> d[i];
		ord[i] = i;
	}
	sort(ord.begin(), ord.end(), [&](int x, int y) {
		return x+d[x] < y+d[y];
	});
	int l = (int)((sm + n - 1)/n), r = (int)1e9;

	// cout << l << endl;

	while (l < r) {
		int mi = (l+r)/2;
		// cout << mi << endl;
		if (can(mi)) {
			
			r = mi;
		} else {
			l = mi + 1;
		}
	}
	cout << l << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);solve();
    return 0;
}