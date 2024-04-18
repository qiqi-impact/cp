//fail

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

int fp[Nmax]; //fp = first prime, i == fp[i] means prime
int np[Nmax]; //np = num primes
vi makeSieve(int lim) {
  vi ret;
  for(int i=2;i<=lim;++i) {
    if(!fp[i]) {
      ret.push_back(i);
      for(int j=i;i*j<=lim;++j) {
        if(!fp[1LL*i*j]) fp[1LL*i*j] = i;
        ++np[j];
      }
      fp[i] = i;
    }
  }
  return ret;
}
vi getPrimes(int x) {
  vi ret;
  while(x > 1) {
    int p = fp[x];
    ret.push_back(p);
    while(x % p == 0) x /= p;
  }
  return ret;
}

void solve() {
    int n;
	cin >> n;
	vi a(n);
	int mx = 0;
	for (int i = 0;i < n;i++) {
		cin >> a[i];
		mx = max(mx, a[i]);
	}
	sort(a.begin(), a.end());
	map<int, int> above, freq;
	set<int> factors;
	for (int i = n - 1;i >= 0;i--) {
		freq[a[i]]++;

		for (int j = 1;j * j <= a[i];j++) {
			factors.insert(j);
			factors.insert(a[i] / j);
		}

		if (i == n - 1 || a[i] < a[i+1]) {
			above[a[i]] = n - i - 1;
		}
	}
	map<int, map<int, ll>> hits;
	for (auto i : factors) {
		int below = 0;
		for (int j = i;j <= mx;j += i) {
			ll ct = 0;
			for (int k = 0;k < freq[j];k++) {
				ct += (ll)(below + k) * (above[j] + freq[j] - k - 1);
			}
			if (freq.count(j)) below += freq[j];
			if (ct) hits[j][i] = ct;
		}
	}
	// dbg(hits);
	ll ret = 0;
	for (auto &[i, hi] : hits) {
		vi ks;
		for (auto &[x, y] : hi) {
			ks.push_back(x);
		}
		sort(ks.rbegin(), ks.rend());
		for (auto x : ks) {
			for (int j = 2*x;j <= mx;j += x) {
				if (hits[i].count(j)) {
					hits[i][x] -= hits[i][j];
				}
			}
			// dbg(i, x, (ll)x * hits[i][x]);
			ret += (ll)x * hits[i][x];
		}
	}
	cout << ret << endl;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}