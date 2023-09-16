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

void solve() {
	ll MOD = 998244353;
    int h, w;
	cin >> h >> w;
	vvi cy(h+1, vi(w+1, 0));
	for (int i = 0;i < h;i++) {
		string s;
		cin >> s;
		for (int j = 0;j < (int)s.length();j++) {
			char c = s[j];
			cy[i+1][j+1] = cy[i][j+1] + cy[i+1][j] - cy[i][j] + (int)(c == 'Y');
		}
	}
	int k = cy[h][w] / 2;
	vi div;
	for (int i = 1;i <= (int)sqrt(k);i++) {
		if (k % i == 0) {
			div.push_back(i);
		}
	}
	ll ret = 0;
	for (auto x : div) {
		int y = k / x;
		vvi tt = {{x, y}};
		if (x != y) tt.push_back({y, x});
		for (auto v : tt) {
			int a = v[0];
			int b = v[1];
			unordered_map<int, int> rc, cc;
			vi rx{0}, cx{0};
			bool fail = false;

			int ct = 1;
			for (int j = 1;j <= h;j++) {
				rc[cy[j][w]]++;
				if (cy[j][w] >= ct * 2 * b) {
					if (cy[j][w] != ct * 2 * b) {
						fail = true;
						break;
					}
					rx.push_back(j);
					ct++;
				}
			}
			if (fail) continue;

			ct = 1;
			for (int i = 1;i <= w;i++) {
				cc[cy[h][i]]++;
				if (cy[h][i] >= ct * 2 * a) {
					if (cy[h][i] != ct * 2 * a) {
						fail = true;
						break;
					}
					cx.push_back(i);
					ct++;
				}
			}
			if (fail) continue;

			ll cur = 1;
			for (int i = 2 * b;i < 2 * k;i += 2 * b) {
				cur *= rc[i];
				cur %= MOD;
			} 
			for (int i = 2 * a;i < 2 * k;i += 2 * a) {
				cur *= cc[i];
				cur %= MOD;
			}

			for (int i = 1;i < (int)rx.size();i++) {
				for (int j = 1;j < (int)cx.size();j++) {
					if (cy[rx[i]][cx[j]] - cy[rx[i-1]][cx[j]] - cy[rx[i]][cx[j-1]] + cy[rx[i-1]][cx[j-1]] != 2) {
						fail = true;
						break;
					}
				}
			}
			if (fail) continue;

			ret += cur;
			ret %= MOD;
		}
	}
	cout << ret << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
	solve();
    return 0;
}