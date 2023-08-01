#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
using vi = vector<int>;
using vvi = vector<vector<int>>;
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
		pr("{",x.f,", ",x.s,"}"); 
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

int solve() {
    int n, m;
	cin >> n >> m;
	string s;
	cin >> s;
	int st = 0;
	for (int i = 0;i < n;i++) {
		st ^= (s[i] - '0') << i;
	}

	vi day(m), rm(m, (1 << n)-1), add(m, 0);

	for (int i = 0;i < m;i++) {
		cin >> day[i];
		string a, b;
		cin >> a >> b;
		for (int j = 0;j < n;j++) {
			rm[i] ^= (a[j] - '0') << j;
			add[i] ^= (b[j] - '0') << j;
		}
	}

	if (st == 0) return 0;

	vector<vector<pii>> g(1 << n);
	for (int i = 0;i < (1 << n);i++) {
		for (int j = 0;j < m;j++) {
			g[i].push_back(pii((i & rm[j]) | add[j], day[j]));
		}
	}

	vi dst(1 << n, INT_MAX);
	priority_queue<pii, vector<pii>, greater<>> pq;
	dst[st] = 0;
	pq.push(pii(0, st));
	while (!pq.empty()) {
		auto [a, b] = pq.top();
		pq.pop();

		if (b == 0) return a;

		if (dst[b] != a) continue;

		for (auto [c, d]: g[b]) {
			if (dst[c] > dst[b] + d) {
				dst[c] = dst[b] + d;
				pq.push(pii(dst[c], c));
			}
		}
	}
	return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) cout << solve() << endl;
    return 0;
}