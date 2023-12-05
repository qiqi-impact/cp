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
    int n, q;
	cin >> n >> q;
	string s;
	cin >> s;
	map<int, map<int, vector<int>>> fw, bk;
	fw[0][0].push_back(-1);
	bk[0][0].push_back(n);
	
	vector<pair<int, int>> fwtot;
	fwtot.push_back(pii(0, 0));

	vector<pair<int, int>> bktot;
	bktot.push_back(pii(0, 0));

	int cx = 0, cy = 0;
	for (int i = 0;i < n;i++) {
		if (s[i] == 'U') cy++;
		if (s[i] == 'D') cy--;
		if (s[i] == 'L') cx--;
		if (s[i] == 'R') cx++;
		fw[cx][cy].push_back(i);
		fwtot.push_back(pii(cx, cy));
	}
	cx = 0, cy = 0;
	for (int i = n-1;i >= 0;i--) {
		if (s[i] == 'U') cy++;
		if (s[i] == 'D') cy--;
		if (s[i] == 'L') cx--;
		if (s[i] == 'R') cx++;
		bk[cx][cy].push_back(i);
		bktot.push_back(pii(cx, cy));
	}

	// dbg(fwtot);
	// dbg(bktot);

	int x, y, l, r;
	for (int i = 0;i < q;i++) {
		cin >> x >> y >> l >> r;
		l--; r--;
		if (x == 0 && y == 0) {
			cout << "YES" << endl;
			continue;
		}
		int idx = lower_bound(fw[x][y].begin(), fw[x][y].end(), 0) - fw[x][y].begin();
		if (idx < fw[x][y].size() && fw[x][y][idx] < l) {
			cout << "YES" << endl;
			continue;
		}
		idx = lower_bound(fw[x][y].begin(), fw[x][y].end(), r+1) - fw[x][y].begin();
		if (idx < fw[x][y].size()) {
			cout << "YES" << endl;
			continue;
		}
		pii fwa = fwtot[l];
		pii bka = bktot[n-(r+1)];
		int dx = x - fwa.first;
		int dy = y - fwa.second;
		// dbg(dx, dy, z, bk[x][y]);
		auto z = &(bk[bka.first+dx][bka.second+dy]);
		auto pt = lower_bound(z->rbegin(), z->rend(), l);
		if (pt != z->rend() && *pt <= r) {
			cout << "YES" << endl;
			continue;
		}
		cout << "NO" << endl;
	}
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0); solve();
    return 0;
}