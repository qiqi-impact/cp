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


int solve() {
    int m;
    cin >> m;
    vvi a(2, vi(m)), rt(2, vi(m));
    for (int i = 0;i < m;i++) {
        cin >> a[0][i];
        if (a[0][i]) a[0][i]++;
    }
    for (int i = 0;i < m;i++) {
        cin >> a[1][i];
        if (a[1][i]) a[1][i]++;
    }
    rt[0][m-1] = max(a[0][m-1], a[1][m-1] - 1);
    rt[1][m-1] = max(a[1][m-1], a[0][m-1] - 1);
    for (int j = m-2;j >= 0;j--) {
        rt[0][j] = max(rt[0][j+1] - 1, max(a[0][j], a[1][j] - ((m - j) * 2 - 1)));
        rt[1][j] = max(rt[1][j+1] - 1, max(a[1][j], a[0][j] - ((m - j) * 2 - 1)));
    }

    int ret = 2e9;
    int x = 0, y = 0;
    int ctime = 0;
    for (int i = 0;i < 2*m-1;i++) {
        if (i != 2*m-2 && (x+y)%2==0) {
            ret = min(ret, max(ctime, rt[x][y]) + (m - y) * 2 - 1);
        }
        int xx = x%2, yy = y%2; 
        if (xx == 0) {
            if (yy == 0) {
                x++;
            } else {
                y++;
            }
        } else {
            if (yy == 0) {
                y++;
            } else {
                x--;
            }
        }
        ctime = max(ctime+1, a[x][y]);
    }
    ret = min(ret, ctime);
    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) cout << solve() << endl;
    return 0;
}