#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
using vi = vector<int>;
using vvi = vector<vi>;
using vll = vector<ll>;
using vvll = vector<vll>;
using pii = pair<const int, int>;

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
    int n;
	cin >> n;
	vi a(n);
	multiset<int> df;
	map<int, int> sa;
	for (int i = 0;i < n;i++) {
		cin >> a[i];
		sa[a[i]]++;
	}

	for (auto it = sa.begin();it != sa.end();it++) {
		if (next(it) != sa.end()) {
			df.insert(next(it)->first - it->first);
		}
	}
	// dbg(df);

	// for (int i = 0;i < n-1;i++) df.insert(a[i+1] - a[i]);
	int q;
	cin >> q;
	for (int i = 0;i < q;i++) {
		int idx, x;
		cin >> idx >> x;
		idx--;

		// if (i < 2) {

		if (sa[a[idx]] > 1) {
			sa[a[idx]]--;
		} else {
			auto it = sa.find(a[idx]);
			vi cand;
			if (it != sa.begin()) {
				int y = prev(it)->first;
				cand.push_back(y);
				df.erase(df.find(a[idx] - y));
			}
			if (next(it) != sa.end()) {
				int y = next(it)->first;
				cand.push_back(y);
				df.erase(df.find(y - a[idx]));
			}
			// dbg(cand, df);
			if (cand.size() == 2) {
				df.insert(cand[1] - cand[0]);
			}
			sa.erase(a[idx]);
		}

		a[idx] = x;
		if (sa[a[idx]] > 0) {
			sa[a[idx]]++;
		} else {
			sa[a[idx]] = 1;
			vi cand;
			auto it = sa.find(a[idx]);
			if (it != sa.begin()) {
				int y = prev(it)->first;
				cand.push_back(y);
				df.insert(a[idx] - y);
			}
			if (next(it) != sa.end()) {
				int y = next(it)->first;
				cand.push_back(y);
				df.insert(y - a[idx]);
			}
			if (cand.size() == 2) {
				df.erase(df.find(cand[1] - cand[0]));
			}
		}
		// cout << "foo ";

		// }

		cout << (sa.rbegin()->first + (df.empty() ? 0 : *df.rbegin())) << " ";
		// dbg(sa, df);
	}
	cout << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}