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

void sv(vi &aa) {
	int n = aa.size();
	dbg(aa);
	vi a(n+1), p(n+1), q(n+1), ai(n+1);
	for (int i = 1;i <= n;i++) a[i] = aa[i-1];
	set<pii> avail;
	for (int i = 1;i <= n;i++) {
		// cin >> a[i];
		ai[a[i]] = i;
		avail.insert(pii(-2, i));
	}
	for (int i = 1;i <= n;i++) {
		int found = -1;
		// dbg(avail);
		for (auto &[x, y]: avail) {
			if (y != i && y != ai[i]) {
				found = y;
				break;
			}
		}
		if (found == -1) {
			cout << "Impossible" << endl;
			return;
		}
		avail.erase(pii(-2, found));
		avail.erase(pii(-1, found));

		for (int j = 1;j <= 2;j++) {
			for (auto t : {i, ai[i]}) {
				if (avail.find(pii(-j, t)) != avail.end()) {
					avail.erase(pii(-j, t));
					avail.insert(pii(-j+1, t));
					break;
				}
			}
		}

		q[i] = found;
	}

	for (int i = 1;i <= n;i++) {
		p[q[i]] = ai[i];
	}

	cout << "Possible" << endl;
	for (auto x: p) if (x) cout << x << " "; cout << endl;
	for (auto x: q) if (x) cout << x << " "; cout << endl;
}

void solve() {
    int n;
	cin >> n;
	vi aa(n), bb(n);
	for (int i = 0;i < n;i++) {
		aa[i] = i+1;
		bb[i] = i;
	}
	do {
		bool s = false;
		vi p = bb;
		do {
			vi q = bb;
			do {
				// dbg(p, q);
				bool should = true;
				for (int i = 0;i < n;i++) {
					if (i == p[i] || i == q[i] || aa[p[q[i]]] != i+1) {
						should = false;
						break;
					}
				}
				if (should) {
					dbg(p, q, should);
					s = true;
					break;
				}
			} while (next_permutation(q.begin(), q.end()));
			if (s) break;
		} while (next_permutation(p.begin(), p.end()));

		dbg(s);
		sv(aa);
	} while (next_permutation(aa.begin(), aa.end()));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}