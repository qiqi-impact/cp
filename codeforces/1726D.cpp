#include <bits/stdc++.h>
#include <unordered_set>
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

void dfs(vector<unordered_map<int, int>> &g, unordered_set<int> &vis, int x) {
    if (vis.count(x)) return;
    vis.insert(x);
    // cout << x << endl;
    vvi assign;

    vi adj;
    for (auto &[k, v] : g[x]) {
        adj.push_back(k);
    }

    for (auto &k : adj) {
        if (g[x][k] == 2) {
            int t = vis.count(k);
            g[x][k] = t;
            g[k][x] = t;
            dfs(g, vis, k);
        }
    }
};

void solve() {
    int n, m;
    cin >> n >> m;
    vector<unordered_map<int, int>> g(n);
    vvi edges;
    for (int i = 0;i < m;i++) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        g[a][b] = 2;
        g[b][a] = 2;
        edges.push_back({a, b});
    }
    unordered_set<int> vis;
    dfs(g, vis, 0);
    for (auto &y : edges) {
        cout << g[y[0]][y[1]];
    }
    cout << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}