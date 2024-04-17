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
	vi a(n), mex(n);
	for (int i = 0;i < n;i++) cin >> a[i];
	int lst = n;
	ll cur = 0;
	for (int i = n-1;i >= 0;i--) {
		mex[i] = lst;
		cur += lst;
		lst = min(lst, a[i]);
	}
	vvi st;
	for (int i = 0;i < n;i++) {
		if (st.empty() || st[st.size()-1][0] < mex[i]) {
			st.push_back({mex[i], i, i});
		} else if (!st.empty() && st[st.size()-1][0] == mex[i]) {
			st[st.size()-1][2]++;
		}
	}
	ll ret = cur;
	// dbg(st, cur);
	int le = 0;
	for (int i = 0;i < n;i++) {
		cur -= st[le][0];
		if (st[le][1] == st[le][2]) {
			le++;
		} else {
			st[le][1]++;
		}
		int left = i + n;
		while (st.size() > le && st[st.size()-1][0] >= a[i]) {
			left = st[st.size()-1][1];
			cur += ((ll)a[i] - st[st.size()-1][0]) * (st[st.size()-1][2] - left + 1);
			st.pop_back();
		}
		if (left <= i + n - 1) st.push_back({a[i], left, i + n - 1});
		st.push_back({n, i + n, i + n});
		cur += n;
		ret = max(ret, cur);
		// dbg(st, cur);
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