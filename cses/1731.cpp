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

const ll MOD = (ll)(1e9)+7;

ll solve() {
    string ss;
	cin >> ss;
	int k;
	cin >> k;
	unordered_set<string> s;
	for (int i = 0;i < k;i++) {
		string t;
		cin >> t;
		s.insert(t);
	}
	int n = ss.length();

	vector<int> memo(n, -1);
	auto dp = [&](auto &&dp, int idx) -> ll {
		if (idx == n) {
			return 1;
		}
		if (memo[idx] != -1) {
			return memo[idx];
		}
		ll ret = 0;
		string q;
		for (int i = idx;i < n;i++) {
			q += ss[i];
			if (s.contains(q)) {
				ret += dp(dp, i + 1);
				ret %= MOD;
			}
		}
		memo[idx] = ret;
		return ret;
	};
	return dp(dp, 0);
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    cout << solve() << endl;
    return 0;
}