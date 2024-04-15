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

struct segtree {
    struct node {
        // initial values for leaves
        long long mx = 0;
		long long mn = 0;
        long long sum = 0;
        long long add = 0;

        void apply(int l, int r, long long v) {
            mx += v;
			mn += v;
            sum += (r - l + 1) * v;
            add += v;
        }
    };

    static node unite(const node &a, const node &b) {
        node res;
        res.mx = max(a.mx, b.mx);
        res.mn = min(a.mn, b.mn);
        res.sum = a.sum + b.sum;
        return res;
    }

    void push(int x, int l, int r) {
        int m = (l + r) >> 1;
        int y = x + ((m - l + 1) << 1);
        if (tree[x].add != 0) {
            tree[x + 1].apply(l, m, tree[x].add);
            tree[y].apply(m + 1, r, tree[x].add);
            tree[x].add = 0;
        }
    }

    void pull(int x, int y) { tree[x] = unite(tree[x + 1], tree[y]); }

    int n;
    vector<node> tree;

    void build(int x, int l, int r) {
        if (l == r) {
            return;
        }
        int m = (l + r) >> 1;
        int y = x + ((m - l + 1) << 1);
        build(x + 1, l, m);
        build(y, m + 1, r);
        pull(x, y);
    }

    template <class T>
    void build(int x, int l, int r, const vector<T> &v) {
        if (l == r) {
            tree[x].apply(l, r, v[l]);
            return;
        }
        int m = (l + r) >> 1;
        int y = x + ((m - l + 1) << 1);
        build(x + 1, l, m, v);
        build(y, m + 1, r, v);
        pull(x, y);
    }

    node get(int x, int l, int r, int ll, int rr) {
        if (ll <= l && r <= rr) {
            return tree[x];
        }
        int m = (l + r) >> 1;
        int y = x + ((m - l + 1) << 1);
        push(x, l, r);
        node res;
        if (rr <= m) {
            res = get(x + 1, l, m, ll, rr);
        } else {
            if (ll > m) {
                res = get(y, m + 1, r, ll, rr);
            } else {
                res = unite(get(x + 1, l, m, ll, rr), get(y, m + 1, r, ll, rr));
            }
        }
        pull(x, y);
        return res;
    }

    template <class T>
    void modify(int x, int l, int r, int ll, int rr, const T &v) {
        if (ll <= l && r <= rr) {
            tree[x].apply(l, r, v);
            return;
        }
        int m = (l + r) >> 1;
        int y = x + ((m - l + 1) << 1);
        push(x, l, r);
        if (ll <= m) {
            modify(x + 1, l, m, ll, rr, v);
        }
        if (rr > m) {
            modify(y, m + 1, r, ll, rr, v);
        }
        pull(x, y);
    }

    segtree(int _n) : n(_n) {
        assert(n > 0);
        tree.resize(2 * n - 1);
        build(0, 0, n - 1);
    }

    template <class T>
    segtree(const vector<T> &v) {
        n = v.size();
        assert(n > 0);
        tree.resize(2 * n - 1);
        build(0, 0, n - 1, v);
    }

    node get(int ll, int rr) {
        assert(0 <= ll && ll <= rr && rr <= n - 1);
        return get(0, 0, n - 1, ll, rr);
    }

    node get(int p) {
        assert(0 <= p && p <= n - 1);
        return get(0, 0, n - 1, p, p);
    }

    template <class T>
    void modify(int ll, int rr, const T v) {
        assert(0 <= ll && ll <= rr && rr <= n - 1);
        modify(0, 0, n - 1, ll, rr, v);
    }

    int find_first(int ll, int rr, const function<bool(const node &)> &f, int x, int l, int r) {
        if (ll <= l && r <= rr && !f(tree[x])) {
            return -1;
        }
        if (l == r) {
            return l;
        }
        push(x, l, r);
        int m = (l + r) >> 1;
        int y = x + ((m - l + 1) << 1);
        int res = -1;
        if (ll <= m) {
            res = find_first(ll, rr, f, x + 1, l, m);
        }
        if (rr > m && res == -1) {
            res = find_first(ll, rr, f, y, m + 1, r);
        }
        pull(x, y);
        return res;
    }

    // calls all FALSE elements to the left of the sought position exactly once
    int find_first(int ll, int rr, const function<bool(const node &)> &f) {
        assert(0 <= ll && ll <= rr && rr <= n - 1);
        return find_first(ll, rr, f, 0, 0, n - 1);
    }
};

// Returns min(p | p<=rr && sum[ll..p]>=sum). If no such p exists, returns -1
int sum_lower_bound(segtree &t, int ll, int rr, long long sum) {
    long long sumSoFar = 0;
    return t.find_first(ll, rr, [&](const segtree::node &node) {
        if (sumSoFar + node.sum >= sum)
            return true;
        sumSoFar += node.sum;
        return false;
    });
}

void solve() {
	int n, q;
	cin >> n >> q;
	vi a(n);
	for (int i = 0;i < n;i++) cin >> a[i];
	segtree st(a);
	for (int i = 0;i < q;i++) {
		char c;
		int l, r;
		cin >> c >> l >> r;
		dbg(c, l, r);
	}
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    solve();
    return 0;
}