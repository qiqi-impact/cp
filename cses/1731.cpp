#include <bits/stdc++.h>
#define pb push_back
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

const ll MOD = (ll)(1e9)+7;
struct trie {
    struct node {
        array<int, 26> child;
        int eow = 0, cnt = 0;
        node() { fill(child.begin(), child.end(), -1); }
        inline bool has(int c) const { return child[c] != -1; }
        int operator[](int c) const { return child[c]; }
    };

    vector<node> nodes;

    trie() { alloc(); }

    int alloc() {
        nodes.push_back(node());
        return nodes.size() - 1;
    }

    void add(string word) {
        int now = 0;
        for (char ch : word) {
            int id = ch - 'a';
            if (!nodes[now].has(id))
                nodes[now].child[id] = alloc();
            ++nodes[now].cnt;
            now = nodes[now].child[id];
        }
        ++nodes[now].eow;
        ++nodes[now].cnt;
    }

    node *search(string word) {
        int now = 0;
        for (char ch : word) {
            int id = ch - 'a';
            if (!nodes[now].has(id))
                return nullptr;
            now = nodes[now].child[id];
        }
        return (!nodes[now].eow) ? nullptr : &nodes[now];
    }

    pair<node &, int> prefix(string pre) {
        int now = 0, len = 0;
        for (char ch : pre) {
            int id = ch - 'a';
            if (!nodes[now].has(id))
                return {nodes[now], len};
            now = nodes[now].child[id];
            ++len;
        }
        return {nodes[now], len};
    }

    node &operator[](int i) { return nodes[i]; }
};

ll solve() {
    string ss;
	cin >> ss;
	int k;
	cin >> k;

	trie T;

	// set<string> s;
	for (int i = 0;i < k;i++) {
		string t;
		cin >> t;
		// s.insert(t);
		T.add(t);
	}
	int n = ss.length();

	vector<ll> dp(n+1, -1);
	dp[n] = 1;
	for (int idx = n-1;idx >= 0;idx--) {
		ll ret = 0;
		int root = 0;
		for (int i = idx;i < n;i++) {
			if (!T[root].has(ss[i] = 'a')) break;
			root = T[root][ss[i] - 'a'];
			if (T[root].eow) {
				ret += dp[i+1];
				ret %= MOD;
			}
		}
		dp[idx] = ret;
	};
	return dp[0];
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    cout << solve() << endl;
    return 0;
}