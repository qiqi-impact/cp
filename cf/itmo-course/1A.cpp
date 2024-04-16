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

#include <algorithm>
#include <array>
#include <cassert>
#include <functional>
#include <iostream>
#include <limits>
#include <vector>
using namespace std;

// http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/p0200r0.html
template<class Fun> class y_combinator_result {
    Fun fun_;
public:
    template<class T> explicit y_combinator_result(T &&fun): fun_(std::forward<T>(fun)) {}
    template<class ...Args> decltype(auto) operator()(Args &&...args) { return fun_(std::ref(*this), std::forward<Args>(args)...); }
};
template<class Fun> decltype(auto) y_combinator(Fun &&fun) { return y_combinator_result<std::decay_t<Fun>>(std::forward<Fun>(fun)); }


// TODO: segment_change can be eliminated entirely in favor of just updating with a new segment instead.
struct segment_change {
    // Use a sentinel value rather than a boolean to save significant memory (4-8 bytes per object).
    static const int SENTINEL = numeric_limits<int>::lowest();

    // Note that to_set goes first, and to_add goes after.
    // TODO: check if these values can overflow int.
    int to_set, to_add;

    // TODO: make sure the default constructor is the identity segment_change.
    segment_change(int _to_add = 0, int _to_set = SENTINEL) : to_set(_to_set), to_add(_to_add) {}

    bool has_set() const {
        return to_set != SENTINEL;
    }
};

struct segment {
    // TODO: check if these values can overflow int.
    int maximum;
    int64_t sum;
    int first, last, max_diff;

    // TODO: make sure the default constructor is the identity segment.
    segment(int _maximum = numeric_limits<int>::lowest(), int64_t _sum = 0, int _first = 0, int _last = 0,
            int _max_diff = -1) : maximum(_maximum), sum(_sum), first(_first), last(_last), max_diff(_max_diff) {}

    bool empty() const {
        return max_diff < 0;
    }

    void apply(const segment_change &change) {
        if (change.has_set()) {
            maximum = first = last = change.to_set;
            sum = change.to_set;
            max_diff = 0;
        }

        maximum += change.to_add;
        sum += change.to_add;
        first += change.to_add;
        last += change.to_add;
    }

    void join(const segment &other) {
        if (empty()) {
            *this = other;
            return;
        } else if (other.empty()) {
            return;
        }

        maximum = max(maximum, other.maximum);
        sum += other.sum;
        max_diff = max({max_diff, other.max_diff, abs(last - other.first)});
        last = other.last;
    }

    // TODO: decide whether to re-implement this for better performance. Mainly relevant when segments contain arrays.
    void join(const segment &seg0, const segment &seg1) {
        *this = seg0;
        join(seg1);
    }
};

struct basic_seg_tree {
    // TODO: POWER_OF_TWO_MODE is necessary in order to call query_full().
    static const bool POWER_OF_TWO_MODE = true;

    static int highest_bit(unsigned x) {
        return x == 0 ? -1 : 31 - __builtin_clz(x);
    }

    int tree_n = 0;
    vector<segment> tree;

    basic_seg_tree(int n = -1) {
        if (n >= 0)
            init(n);
    }

    void init(int n) {
        if (POWER_OF_TWO_MODE) {
            tree_n = 1;

            while (tree_n < n)
                tree_n *= 2;
        } else {
            tree_n = n;
        }

        tree.assign(2 * tree_n, {});
    }

    // Builds our tree from an array in O(n).
    void build(const vector<segment> &initial) {
        int n = int(initial.size());
        init(n);
        copy(initial.begin(), initial.end(), tree.begin() + tree_n);

        for (int position = tree_n - 1; position > 0; position--)
            tree[position].join(tree[2 * position], tree[2 * position + 1]);
    }

    template<typename T_range_op>
    void process_range(int a, int b, T_range_op &&range_op) const {
        assert(0 <= a && a <= b && b <= tree_n);
        a += tree_n;
        b += tree_n;
        a--;
        int anc_depth = highest_bit(a ^ b);
        int anc_mask = (1 << anc_depth) - 1;

        // Iterate the 0-bits of `a` bottom-up and the 1-bits of `b` top-down.
        for (int v = ~a & anc_mask; v != 0; v &= v - 1) {
            int i = __builtin_ctz(v);
            if (range_op((a >> i) + 1)) return;  // Early return used for search only
        }

        for (int v = b & anc_mask, i; v != 0; v ^= 1 << i) {
            i = highest_bit(v);
            if (range_op((b >> i) - 1)) return;
        }
    }

    segment query(int a, int b) const {
        segment answer;

        process_range(a, b, [&](int position) -> bool {
            answer.join(tree[position]);
            return false;
        });

        return answer;
    }

    segment query_full() const {
        assert(POWER_OF_TWO_MODE);
        return tree[1];
    }

    segment query_single(int index) const {
        assert(0 <= index && index < tree_n);
        return tree[tree_n + index];
    }

    void join_up(int position) {
        while (position > 1) {
            position /= 2;
            tree[position].join(tree[2 * position], tree[2 * position + 1]);
        }
    }

    void update(int index, const segment_change &change) {
        assert(0 <= index && index < tree_n);
        int position = tree_n + index;
        tree[position].apply(change);
        join_up(position);
    }

    void set(int index, const segment &seg) {
        assert(0 <= index && index < tree_n);
        int position = tree_n + index;
        tree[position] = seg;
        join_up(position);
    }

    // Finds the end of the last subarray starting at `first` satisfying `should_join` via binary search in O(log n).
    template<typename T_bool>
    int find_last_subarray(T_bool &&should_join, int n, int first = 0) const {
        assert(0 <= first && first <= n);
        segment current;

        // Check the degenerate case.
        if (!should_join(current, current))
            return first - 1;

        int node = -1;

        // Try to build the range [first, tree_n); when a node fails, search down instead.
        // We use the range [first, tree_n) instead of [first, n) for a boost in speed.
        process_range(first, tree_n, [&](int position) -> bool {
            if (should_join(current, tree[position])) {
                current.join(tree[position]);
                return false;
            }

            node = position;
            return true;
        });

        if (node < 0)
            return n;

        while (node < tree_n)
            if (should_join(current, tree[2 * node])) {
                current.join(tree[2 * node]);
                node = 2 * node + 1;
            } else {
                node = 2 * node;
            }

        return node - tree_n;
    }
};

void solve() {
    int n, q;
	cin >> n >> q;
	basic_seg_tree tree(n);
	tree.build(vector<segment>(n, segment()));
	for (int i = 0;i < n;i++) {
		int x;
		cin >> x;
		tree.update(i, segment_change(0, x));
	}
	for (int i = 0;i < q;i++) {
		int t, l, r;
		cin >> t >> l >> r;
		if (t == 1) {
			tree.update(l, segment_change(0, r));
		} else {
			cout << tree.query(l, r).sum << '\n';
		}
	}
}

int main() {
    cin.tie(0)->sync_with_stdio(false);
    solve();
    return 0;
}