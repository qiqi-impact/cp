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
    int n;
	cin >> n;
	vvi used(n, vi(n, 0));
	for (int i = 0;i < n;i++) {
		for (int j = i;j < n;j++) {
			used[i][j] = -1;
		}
	}

	vector<pair<int, int>> dir;
	dir.push_back(pii(0, -1));
	dir.push_back(pii(1, 0));
	dir.push_back(pii(0, 1));
	dir.push_back(pii(-1, 0));

	for (int i = 0;i < n;i++) {
		int pp;
		cin >> pp;
		int cx = i, cy = i;
		used[i][i] = pp;
		for (int j = 0;j < pp-1;j++) {
			bool found = false;
			for (auto p: dir) {
				int nx = cx + p.first;
				int ny = cy + p.second;
				if (0 <= nx && nx < n && 0 <= ny && ny < n && !used[nx][ny]) {
					used[nx][ny] = pp;
					cx = nx;
					cy = ny;
					found = true;
					break;
				}
			}
			if (!found) {
				cout << -1 << endl;
				return;
			}
		}
		// dbg(used);
	}

	for (int i = 0;i < n;i++) {
		for(int j = 0;j <= i;j++) {
			cout << used[i][j] << " ";
		}
		cout << endl;
	}
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);solve();
    return 0;
}