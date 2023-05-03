#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
using vi = vector<int>;
using vvi = vector<vector<int>>;

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

int MX = 333333;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
	ll n;
	cin >> n;

	vector<double> primes;
	primes.push_back(2);
	for (int i = 3;i < MX;i += 2) {
		bool fail = false;
		for (auto x: primes) {
			if (i%(int)x == 0) {
				fail = true;
				break;
			}
			if (x*x > i) {
				break;
			}
		}
		if (!fail) primes.push_back(i);
	}

	ll ret = 0;
	for (int i = 0;i < (int)primes.size();i++) {
		if (primes[i] > 10000) break;
		for (int j = i+1;j < (int)primes.size();j++) {
			if (primes[j] > 10000) break;
			double cur = primes[i] * primes[i] * primes[j];
			if (cur >= n) break;
			int idx = lower_bound(primes.begin(), primes.end(), sqrt((n+1) / cur)) - primes.begin();
			ret += max(0, idx - j - 1);
		}
	}
	cout << ret << endl;
}