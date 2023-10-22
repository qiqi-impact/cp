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
    int n, m;
	cin >> n >> m;
	vi l(n), r(n);
	set<int> norm;
	norm.insert(1);
	norm.insert(m);
	for (int i = 0;i < n;i++) {
		cin >> l[i] >> r[i];
		norm.insert(l[i]);
		norm.insert(r[i]);
	}
	int ns = norm.size();
	map<int, int> mp;
	int q = 0;
	for (auto x : norm) {
		mp[x] = q++;
	}
	vvi st(ns), ed(ns);
	for (int i = 0;i < n;i++) {
		int a = mp[l[i]];
		int b = mp[r[i]];
		st[a].push_back(i);
		ed[b].push_back(i);
	}
	// dbg(st, ed);
	int df = 0, L = 0, R = 0, cur = 0;
	for (int i = 0;i < ns;i++) {
		for (auto x : st[i]) {
			cur++;
			if (mp[l[x]] == mp[1]) {
				L++;
			}
			if (mp[r[x]] == mp[m]) {
				R++;
			}
			df = max(df, cur - L);
			df = max(df, cur - R);
			// dbg(cur, L, R);
		}
		for (auto x : ed[i]) {
			if (mp[l[x]] == mp[1]) {
				L--;
			}
			if (mp[r[x]] == mp[m]) {
				R--;
			}
			cur--;
		}
	}
	cout << df << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}