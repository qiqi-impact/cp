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

vi a, d;
set<pii> avail;
vvi start;
int n;
ll sm;

bool can(int x) {
	vi drain(n, 0);
	avail.clear();
	ll tot = 0;

	for (int i = 0;i < n;i++) {
		for (auto x : start[i]) {
			avail.insert(pii(x+d[x], x));
		}
		int left = x;
		while (left && !avail.empty()) {
			auto [lb, idx] = *avail.begin();
			if (lb < i) {
				avail.erase(avail.begin());
				continue;
			}
			int amt = min(left, a[idx] - drain[idx]);
			drain[idx] += amt;
			left -= amt;
			tot += amt;
			if (a[idx] == drain[idx]) {
				avail.erase(avail.begin());
			} else {
				break;
			}
		}
	}
	return tot == sm;
}

void solve() {
    cin >> n;
	a = vi(n);
	d = vi(n);
	start = vvi(n);
	sm = 0;
	for (int i = 0;i < n;i++) {
		cin >> a[i];
		sm += a[i];
	}
	for (int i = 0;i < n;i++) {
		cin >> d[i];
		start[max(0, i - d[i])].push_back(i);
	}
	int l = (int)((sm + n - 1)/n), r = (int)1e9;
	while (l < r) {
		int mi = (l+r)/2;
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