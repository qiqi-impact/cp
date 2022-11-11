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

void solve() {
    set<pii> colors;
    int mn = 1;
    vector<pii> v;
    int n;
    cin >> n;
    vector<int> ret(n, 0);
    for (int i = 0;i < n;i++) {
        int k;
        cin >> k;
        v.push_back(pii(k, i));
    }
    sort(v.rbegin(), v.rend());
    for (auto &[val, idx] : v) {
        auto f = colors.lower_bound(pii(idx, 0));
        vector<bool> opt(mn+1, true);
        if (f != colors.end()) {
            opt[f->second] = false;
        }
        if (f != colors.begin()) {
            f--;
            opt[f->second] = false;
        }
        bool found = false;
        for (int i = 1;i <= mn;i++) {
            if (opt[i]) {
                found = true;
                colors.insert(pii(idx, i));
                ret[idx] = i;
                break;
            }
        }
        if (!found) {
            mn++;
            colors.insert(pii(idx, mn));
            ret[idx] = mn;
        }
    }
    cout << mn << endl;
    for (auto &x : ret) {
        cout << x << " ";
    }
    cout << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    freopen("tour.in", "r", stdin);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}