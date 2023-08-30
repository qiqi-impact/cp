#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
using vi = vector<int>;
using vvi = vector<vi>;
using vll = vector<ll>;
using vvll = vector<vll>;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

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
    int n, m, h;
	cin >> n >> m >> h;
	vi a(n), b(n);
	for (int i = 0;i < n;i++) {
		cin >> a[i] >> b[i];
		b[i]--;
	}
	ll sm = 0;
	vll cum(m, 0);
	vll ret(m+1, n);
	set<pair<ll, ll>> left, right;
	for (int i = 0;i < m;i++) left.insert(pll(0, i));
	for (int i = 0;i < n;i++) {
		pll p = pll(cum[b[i]], b[i]);
		if (left.find(p) != left.end()) {
			left.erase(p);
			cum[b[i]] += a[i];
			left.insert(pll(cum[b[i]], b[i]));
			sm += a[i];
		} else {
			right.erase(p);
			cum[b[i]] += a[i];
			right.insert(pll(cum[b[i]], b[i]));
		}
		while (left.size() && right.size() && left.rbegin()->first > right.begin()->first) {
			auto x = *(left.rbegin());
			auto y = *(right.begin());

			left.erase(x);
			right.erase(y);
			left.insert(y);
			right.insert(x);

			sm += y.first - x.first;
		}
		while (sm >= h) {
			ret[right.size()] = i;
			auto x = *(left.rbegin());
			left.erase(x);
			right.insert(x);
			sm -= x.first;
		}
	}
	for (auto x : ret) cout << x << " ";
	cout << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
	solve();
    return 0;
}