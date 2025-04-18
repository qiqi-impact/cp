#include <bits/stdc++.h>

#define sz(x) (x).size()
#define pb push_back
#define all(x) (x).begin(), (x).end()

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

vector<int> primes;

int solve() {
	int aa, bb, ll;
	cin >> aa >> bb >> ll;
	// dbg(aa, bb, ll);
	vector<int> a, b, l;
    // for (auto x : primes) {
	// 	int c = 0;
	// 	while (aa % x == 0) {
	// 		aa /= x;
	// 		c++;
	// 	}
	// 	a.push_back(c);
	// 	c = 0;
	// 	while (bb % x == 0) {
	// 		bb /= x;
	// 		c++;
	// 	}
	// 	b.push_back(c);
	// 	c = 0;
	// 	while (ll % x == 0) {
	// 		ll /= x;
	// 		c++;
	// 	}
	// 	l.push_back(c);
	// }
	// dbg(a, b, l);
	set<int> s;
	for (int i = 0;i < 100000;i++) {
		int left = ll;
		// dbg(ll, bb);
		for (int j = 0;j < 100000;j++) {
			s.insert(left);
			if (left % aa) {
				break;
			}
			left /= aa;
		}
		if (ll % bb) break;
		ll /= bb;
		// int cur = 1;
		// int amt = (int)1e9;
		// for (int j = 0;j < primes.size();j++) {
		// 	int t = l[j] - i * a[j];
		// 	if (t < 0) {
		// 		cur = -1;
		// 		break;
		// 	}
		// 	if (b[j]) amt = min(amt, t / b[j]);
		// }
		// if (cur == -1) break;
		// ret += (amt + 1);
		// dbg(i, amt);
	}
	return s.size();
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    int t;
    cin >> t;

	for (int i = 2;i <= 100;i++) {
		int p = 1;
		for (auto x : primes) {
			if (i % x == 0) p = 0;
		}
		if (p) primes.push_back(i);
	}

    while (t--) cout << solve() << endl;
    return 0;
}