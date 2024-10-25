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

int dp[2][101][51 * 51 + 1];

void solve() {
	string s;
	cin >> s;
	int n = s.length();
	for (int i = 0;i <= n;i++) {
		for (int j = 0;j <= (n+1) * (n+1) / 4;j++) {
			dp[0][i][j] = -1;
			dp[1][i][j] = -1;
		}
	}
	dp[0][0][0] = 0;
    int ctz = 0;
    for (int ct = 0;ct < n;ct++) {
        ctz += s[ct] == '0';
        for (int i = 0;i <= n;i++) {
            for (int j = 0;j <= (n+1) * (n+1) / 4;j++) {
                if (dp[0][i][j] == -1) continue;
                if (i < n) {
                    if (dp[1][i+1][j] == -1) dp[1][i+1][j] = n;
                    dp[1][i+1][j] = min(dp[1][i+1][j], dp[0][i][j] + (s[ct] != '0'));
                }
                if (j+i <= (n+1) * (n+1) / 4) {
                    if (dp[1][i][j+i] == -1) dp[1][i][j+i] = n;
                    dp[1][i][j+i] = min(dp[1][i][j+i], dp[0][i][j] + (s[ct] != '1'));
                }
            }
        }
        for (int i = 0;i <= n;i++) {
            for (int j = 0;j <= (n+1) * (n+1) / 4;j++) {
                dp[0][i][j] = dp[1][i][j];
                dp[1][i][j] = -1;
                // cout << dp[0][i][j] << " ";
            }
        }
        // cout << endl;
    }
    // cout << ctz << " " << ctz*(n-ctz)/2 << endl;
	cout << (dp[0][ctz][ctz*(n-ctz)/2]/2) << endl;
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    solve();
    return 0;
}