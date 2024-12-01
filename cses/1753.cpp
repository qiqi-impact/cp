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

class KMP {
    string pattern;
    vector <int> fail;

    void initKMP(const string &p) {
        pattern = p;
        int m = pattern.size();
        fail.assign(m + 1, -1);
        for (int i = 0, j = -1; i < m; i++) {
            while (j >= 0 && pattern[i] != pattern[j]) j = fail[j];
            j++;
            if (pattern[i + 1] == pattern[j]) fail[i + 1] = fail[j];
            else fail[i + 1] = j;
        }
    }

    void initMP(const string &p) {
        pattern = p;
        int m = pattern.size();
        fail.assign(m + 1, -1);
        for (int i = 0, j = -1; i < m; i++) {
            while (j >= 0 && pattern[i] != pattern[j]) j = fail[j];
            fail[i+1] = ++j;
        }
    }

public:
    KMP(const string &p) { initKMP(p); }

    int period(int i) { return i - fail[i]; }

    vector <int> match(const string &s) {
        int n = s.size();
        int m = pattern.size();
        vector <int> res;
        for (int i = 0, k = 0; i < n; i++) {
            while (k >= 0 && s[i] != pattern[k]) k = fail[k];
            k++;
            if (k == m) res.push_back(i - m + 1);
        }
        return res;
    }
};

void solve() {
	string s, p;
	cin >> s >> p;
    KMP kmp(p);
    vector <int> ans = kmp.match(s);
	cout << ans.size() << endl;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    solve();
    return 0;
}