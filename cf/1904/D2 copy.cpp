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

int n;
vi parent;
vi sz;
vi mx;

int find(int a) { 
	if (a != parent[a]) {
		a = find(parent[a]);
	}
	return parent[a];
}

void join(int a, int b) {
	int fa = find(a);
	int fb = find(b);
	if (fa != fb) {
		if (sz[fa] < sz[fb]) {
			parent[fa] = fb;
			sz[fb] += sz[fa];
			mx[fb] = max(mx[fb], mx[fa]);
		} else {
			parent[fb] = fa;
			sz[fa] += sz[fb];
			mx[fa] = max(mx[fa], mx[fb]);
		}
	}
}

void solve() {
    int n;
	cin >> n;
	vi a(n), b(n), oa(n), ob(n);
	parent = vi(n);
	sz = vi(n, 1);
	mx = vi(n);
	vi seen(n, 0);
	for (int i = 0;i < n;i++) {
		cin >> a[i];
		mx[i] = a[i];
		parent[i] = i;
		oa[i] = i;
	}
	for (int i = 0;i < n;i++) {
		cin >> b[i];
		ob[i] = i;
	}
	sort(oa.begin(), oa.end(), [&](int i, int j) {
		return a[i] < a[j];
	});
	sort(ob.begin(), ob.end(), [&](int i, int j) {
		return b[i] < b[j];
	});
	dbg(oa);
	dbg(ob);
	int ap = 0, bp = 0;
	for (int i = 1;i <= n;i++) {
		while (ap < oa.size() && a[oa[ap]] == i) {
			seen[oa[ap]] = 1;
			
			if (oa[ap] > 0 && seen[oa[ap]-1]) {
				join(oa[ap], oa[ap] - 1);
			}

			if (oa[ap] < n-1 && seen[oa[ap]+1]) {
				join(oa[ap], oa[ap] + 1);
			}

			ap++;
		}
		dbg(i, parent, sz, mx);
		while (bp < ob.size() && b[ob[bp]] == i) {
			if (mx[find(ob[bp])] != i) {
				cout << "NO" << endl;
				return;
			}
			bp++;
		}
	}
	cout << "YES" << endl;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}