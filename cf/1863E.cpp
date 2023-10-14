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

using pli = pair<ll, int>;

void solve() {
    int n, m, k;
	cin >> n >> m >> k;
	vi h(n), deg(n, 0);
	vvi g(n);
	for (int i = 0;i < n;i++) cin >> h[i];
	for (int i = 0;i < m;i++) {
		int x, y;
		cin >> x >> y;
		x--; y--;
		g[x].push_back(y);
		deg[y]++;
	}
	priority_queue<pli, vector<pli>, greater<pli>> pq;
	for (int i = 0;i < n;i++) {
		if (!deg[i]) {
			pq.push(pli(h[i], i));
		}
	}
	ll start = -1, end = -1;
	while (!pq.empty()) {
		pli p = pq.top();
		pq.pop();
		if (start == -1) {
			start = p.first;
		}
		end = p.first;
		for (auto x : g[p.second]) {
			deg[x]--;
			if (!deg[x]) {
				ll rem = p.first % k;
				if (rem > h[x]) {
					rem = p.first + k + h[x] - rem;
				} else {
					rem = p.first + h[x] - rem;
				}
				pq.push(pli(rem, x));
			}
		}
	}
	cout << end - start << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}