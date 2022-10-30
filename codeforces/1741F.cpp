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

vi ans(vvi &evt, int n) {
	vi ret(n, 1e9+1);
	vi last_seen(n, -(1e9+1));
	vi stack_count(n, 0);
	int smstack = 0;
	priority_queue<pii, vector<pii>> h;

	int ep = 0;
	while (ep < evt.size()) {
		int ct = evt[ep][0];
		// dbg(evt[ep]);
		vvi to_modify;
		while (ep < evt.size() && evt[ep][0] == ct) {
			vi v = evt[ep];
			int se = v[1], c = v[2], idx = v[3];
			if (se == 1) {
				stack_count[c]++;
				smstack++;
				to_modify.push_back({idx, c});
			} else {
				stack_count[c]--;
				smstack--;
				if (last_seen[c] != ct) {
					last_seen[c] = ct;
					h.push({ct, c});
				}
			}
			ep++;	
		}
		// dbg(to_modify);
		for (auto &v : to_modify) {
			int idx = v[0], c = v[1];
			if (smstack - stack_count[c] > 0) {
				ret[idx] = 0;
				// dbg(idx, ret[idx]);
				continue;
			}
			while (!h.empty() && last_seen[h.top().second] != h.top().first) h.pop();
			if (h.empty()) continue;
			int lst = h.top().first;
			if (h.top().second == c) {
				pii x = h.top();
				h.pop();
				while (!h.empty() && last_seen[h.top().second] != h.top().first) h.pop();
				if (h.empty()) continue;
				lst = h.top().first;
				h.push(x);
			}
			ret[idx] = ct - lst;
			// dbg(idx, ret[idx]);
		}
	}
	return ret;
}

void solve() {
	int n, k;
	cin >> n;
	vvi evt; // time, start/end, color, index
	vvi revt;
	for (int i = 0;i < n;i++) {
		int a, b, c;
		cin >> a >> b >> c;
		c--;
		evt.push_back({a, 1, c, i});
		evt.push_back({b, 0, c, i});
		revt.push_back({-a, 0, c, i});
		revt.push_back({-b, 1, c, i});
	}
	sort(evt.begin(), evt.end());
	sort(revt.begin(), revt.end());
	vi left = ans(evt, n);
	vi right = ans(revt, n);
	dbg(left);
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