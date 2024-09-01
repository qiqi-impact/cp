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

int mx(vi &v) {
	int m = 0;
	for (auto x : v) m = max(m, x);
	return m;
}

int sm(vi &v) {
	int m = 0;
	for (auto x : v) m += x;
	return m;
}

int solve() {
	int n;
	cin >> n;
	string s;
	cin >> s;
	vi p(26), q(26), lp(26), lq(26);
	int pt = 0, qt = 0;
	for (int i = 0;i < s.size();i++) {
		if (i%2) {
			q[s[i]-'a']++;
		} else {
			p[s[i]-'a']++;
		}
	}
	int ret = 1e9;
	if (n%2 == 0) {
		ret = (n+1)/2 - mx(p) + n/2 - mx(q);
		// cout << ret << endl;
	} else {
		for (int i = 0;i < s.size();i++) {
			vi np(26), nq(26);
			if (i%2) {
				q[s[i]-'a']--;
			} else {
				p[s[i]-'a']--;
			}
			for (int j = 0;j < 26;j++) {
				np[j] = lp[j] + q[j] - lq[j];
				nq[j] = lq[j] + p[j] - lp[j];
			}
			// dbg(i);
			// dbg(np);
			// dbg(nq);
			ret = min(ret, sm(np) + sm(nq) - mx(np) - mx(nq));
			if (i%2) {
				q[s[i]-'a']++;
				lq[s[i]-'a']++;
			} else {
				p[s[i]-'a']++;
				lp[s[i]-'a']++;
			}
		}
		ret++;
	}
	return ret;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    int t;
    cin >> t;
    while (t--) cout << solve() << endl;
    return 0;
}