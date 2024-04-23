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
    int n, m, k;
	cin >> n >> m >> k;
	vvi a, ct;
	int z = 0;
	map<int, vi> open, close;
	for (int i = 0;i < m;i++) {
		int x, y;
		cin >> x >> y;
		x--; y--;
		a.push_back({x, y});
		open[x].push_back(i);
		close[y+1].push_back(i);
	}
	
	vi pf = {0}, pf2 = {0};
	set<int> s;
	for (int i = 0;i < n;i++) {
		for (auto x : open[i]) {
			s.insert(x);
		}
		for (auto x : close[i]) {
			s.erase(x);
		}
		int df = s.size() == 1;
		pf.push_back(pf.back() + df);
		df = s.size() == 2;
		pf2.push_back(pf2.back() + df);
		if (df) {
			ct.push_back(vi(s.begin(), s.end()));
		} else {
			ct.push_back(vi());
		}
		z += s.size() == 0;
	}

	vi best2;
	for (auto v : a) {
		int c = pf[v[1]+1] - pf[v[0]];
		best2.push_back(c);
		sort(best2.rbegin(), best2.rend());
		if (best2.size() > 2) best2.pop_back();
	}
	int ret = z;
	for (auto x : best2) {
		ret += x;
	}

	for (int i = 0;i < n;i++) {
		int cur = z;
		if (ct[i].size() == 2) {
			for (auto x : ct[i]) {
				cur += pf[a[x][1]+1] - pf[a[x][0]];
			}
			int aa = max(a[ct[i][0]][0], a[ct[i][1]][0]);
			int bb = min(a[ct[i][0]][1], a[ct[i][1]][1]);
			cur += pf2[bb+1] - pf2[aa];
		}
		ret = max(ret, cur);
	}
	cout << ret << '\n';
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}