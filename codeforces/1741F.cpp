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

vi ans(vvi &seg) {
	int n = seg.size();
	int tp = 0;
	vi ret(n, INT_MAX);
	vi last_time(n, INT_MIN);
	vvi best; // {val, color}
	for (int i = 0;i < n;i++) {
		int ctime = seg[i][0];
		int idx = seg[i][3];
		while (tp != seg.size() && seg[tp][0] == ctime) {
			int c = seg[tp][2];
			int e = seg[tp][1];
			if (last_time[c] < e) {
				vvi nb;
				for (auto &x : best) {
					if (x[1] != c) {
						nb.push_back(x);
					}
				}
				best = nb;
				last_time[c] = e;
				best.push_back({e, c});
			}
			tp++;
		}
		sort(best.begin(), best.end());
		reverse(best.begin(), best.end());
		if (best.size() > 2) {
			best.resize(2);
		}
		dbg(best);
		for (auto &v : best) {
			if (v[1] != seg[i][2]) {
				dbg(idx, ret[idx], seg[i][0], v[0]);
				ret[idx] = min(ret[idx], max(0, seg[i][0] - v[0]));
				break;
			}
		}
		dbg(ret);
	}
	return ret;
}

void solve() {
	int n, k;
	cin >> n;
	vvi seg; // time, start/end, color, index
	vvi rseg;
	for (int i = 0;i < n;i++) {
		int a, b, c;
		cin >> a >> b >> c;
		c--;
		seg.push_back({a, b, c, i});
		rseg.push_back({-b, -a, c, i});
	}
	sort(seg.begin(), seg.end());
	sort(rseg.begin(), rseg.end());
	vi left = ans(seg);
	dbg(left);
	vi right = ans(rseg);
	
	dbg(right);
	for (int i = 0;i < n;i++) {
		cout << min(left[i], right[i]) << " ";
	}
	cout << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}