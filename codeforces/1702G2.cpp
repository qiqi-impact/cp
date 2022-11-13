#include <bits/stdc++.h>
#include <unordered_set>
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

struct LCA {
    vector<int> height, euler, first, segtree;
    vector<bool> visited;
    int n;

    LCA(vector<vector<int>> &adj, int root = 0) {
        n = adj.size();
        height.resize(n);
        first.resize(n);
        euler.reserve(n * 2);
        visited.assign(n, false);
        dfs(adj, root);
        int m = euler.size();
        segtree.resize(m * 4);
        build(1, 0, m - 1);
    }

    void dfs(vector<vector<int>> &adj, int node, int h = 0) {
        visited[node] = true;
        height[node] = h;
        first[node] = euler.size();
        euler.push_back(node);
        for (auto to : adj[node]) {
            if (!visited[to]) {
                dfs(adj, to, h + 1);
                euler.push_back(node);
            }
        }
    }

    void build(int node, int b, int e) {
        if (b == e) {
            segtree[node] = euler[b];
        } else {
            int mid = (b + e) / 2;
            build(node << 1, b, mid);
            build(node << 1 | 1, mid + 1, e);
            int l = segtree[node << 1], r = segtree[node << 1 | 1];
            segtree[node] = (height[l] < height[r]) ? l : r;
        }
    }

    int query(int node, int b, int e, int L, int R) {
        if (b > R || e < L)
            return -1;
        if (b >= L && e <= R)
            return segtree[node];
        int mid = (b + e) >> 1;

        int left = query(node << 1, b, mid, L, R);
        int right = query(node << 1 | 1, mid + 1, e, L, R);
        if (left == -1) return right;
        if (right == -1) return left;
        return height[left] < height[right] ? left : right;
    }

    int lca(int u, int v) {
        int left = first[u], right = first[v];
        if (left > right)
            swap(left, right);
        return query(1, 0, euler.size() - 1, left, right);
    }
};

vector<int> depths;
vector<vector<int>> adj;
vector<int> anc;

void dfs(int i, int p, int d) {
	depths[i] = d;
	for (auto x : adj[i]) {
		if (x != p) {
			anc[x] = i;
			dfs(x, i, d+1);
		}
	}
}

int my_lca(LCA &lca, int i, int j) {
	return lca.lca(i, j);
}

void solve() {
    int n;
	cin >> n;
	adj.assign(n, vector<int>());
	anc.assign(n, -1);
	for (int i = 0;i < n-1;i++) {
		int a, b;
		cin >> a >> b;
		a--; b--;
		adj[a].push_back(b);
		adj[b].push_back(a);
	}
	LCA lca(adj);

	depths.assign(n, 0);
	dfs(0, -1, 0);

	int q;
	cin >> q;
	for (int qq = 0;qq < q;qq++) {
		int qc;
		cin >> qc;
		vector<int> qv(qc);
		for (int i = 0;i < qc;i++) {
			cin >> qv[i];
			qv[i]--;
		}
		sort(qv.begin(), qv.end(), [&](int i, int j) {
			return depths[i] > depths[j];
		});
		// dbg(qv);
		int first = qv[0];
		int second = -1;
		int top;
		for (auto x: qv) {
			int l = my_lca(lca, first, x);
			if (l != x) {
				top = l;
				second = x;
				break;
			}
		}
		if (second == -1) {
			cout << "YES" << endl;
			continue;
		}
		bool fail = false;
		for (auto x : qv) {
			int a = my_lca(lca, x, first);
			int b = my_lca(lca, x, second);
			int c = my_lca(lca, a, top);
			int d = my_lca(lca, b, top);
			if ((a != x || c != top) && (b != x || d != top)) {
				fail = true;
				break;
			}
		}
		cout << (!fail ? "YES" : "NO") << endl;
	}
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    solve();
    return 0;
}