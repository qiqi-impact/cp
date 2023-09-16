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
    int n, q;
	cin >> n >> q;
	vi a(n);
	// dbg(a);
	vector<vector<pair<int, int>>> st(n), ed(n);
	vi ret(q, -1);
	unordered_map<int, set<int>> m;
	// dbg(ret);
	for (int i = 0;i < n;i++) cin >> a[i];
	for (int i = 0;i < q;i++) {
		int x, y, z;
		cin >> x >> y >> z;
		x--;
		y--;
		st[x].emplace_back(i, z);
		ed[y].emplace_back(i, z);
	}
	// dbg(m);
	for (int i = 0;i < n;i++) {
		for (auto [x, y] : st[i]) {
			m[y].insert(x);
		}
		vi del;
		for (auto &[x, y] : m) {
			if (x != a[i]) {
				del.push_back(x);
				for (auto z : y) {
					ret[z] = i+1;
				}
			}
		}
		for (auto x : del) {
			m.erase(x);
		}
		for (auto [x, y] : ed[i]) {
			m[y].erase(x);
		}
	}
	for (auto x : ret) cout << x << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0); solve();
    return 0;
}