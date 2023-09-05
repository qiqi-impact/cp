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

mt19937 gen(0);
 
vi random(int n) {
  vector<int> p(n);
  iota(p.begin(), p.end(), 0);
  shuffle(p.begin(), p.end(), gen);
  return p;
}

void solve() {
    int n;
	cin >> n;
	vi a(n), q(n), p(n), ai(n);
	for (int i = 0;i < n;i++) {
		cin >> a[i];
		a[i]--;
		ai[a[i]] = i;
	}

	bool poss = false;
	if (n < 4) {
		iota(q.begin(), q.end(), 0);
		do {
			bool fail = false;
			for (int i = 0;i < n;i++) {
				p[q[i]] = ai[i];
				if (q[i] == i || q[i] == ai[i]) {
					fail = true;
					break;
				}
			}
			if (!fail) {
				poss = true;
				break;
			}
		} while (next_permutation(q.begin(), q.end()));
	} else {
		poss = true;
		while (1) {
			q = random(n);
			bool fail = false;
			for (int i = 0;i < n;i++) {
				p[q[i]] = ai[i];
				if (q[i] == i || q[i] == ai[i]) {
					fail = true;
					break;
				}
			}
			if (!fail) break;
		}
	}

	if (!poss) {cout << "Impossible" << endl; return;}
	
	cout << "Possible" << endl;
	for (auto x: p) cout << x+1 << " "; cout << endl;
	for (auto x: q) cout << x+1 << " "; cout << endl;
	// for (int i = 0;i < n;i++) cout << a[p[q[i]]]+1 << " "; cout << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}