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

#ifndef ATCODER_INTERNAL_BITOP_HPP
#define ATCODER_INTERNAL_BITOP_HPP 1

#ifdef _MSC_VER
#include <intrin.h>
#endif

#if __cplusplus >= 202002L
#include <bit>
#endif

namespace atcoder {

namespace internal {

#if __cplusplus >= 202002L

using std::bit_ceil;

#else

// @return same with std::bit::bit_ceil
unsigned int bit_ceil(unsigned int n) {
    unsigned int x = 1;
    while (x < (unsigned int)(n)) x *= 2;
    return x;
}

#endif

// @param n `1 <= n`
// @return same with std::bit::countr_zero
int countr_zero(unsigned int n) {
#ifdef _MSC_VER
    unsigned long index;
    _BitScanForward(&index, n);
    return index;
#else
    return __builtin_ctz(n);
#endif
}

// @param n `1 <= n`
// @return same with std::bit::countr_zero
constexpr int countr_zero_constexpr(unsigned int n) {
    int x = 0;
    while (!(n & (1 << x))) x++;
    return x;
}

}  // namespace internal

}  // namespace atcoder

#endif  // ATCODER_INTERNAL_BITOP_HPP

#ifndef ATCODER_LAZYSEGTREE_HPP
#define ATCODER_LAZYSEGTREE_HPP 1

#include <algorithm>
#include <cassert>
#include <functional>
#include <vector>

// #include "atcoder/internal_bit"

namespace atcoder {

#if __cplusplus >= 201703L

template <class S,
          auto op,
          auto e,
          class F,
          auto mapping,
          auto composition,
          auto id>
struct lazy_segtree {
    static_assert(std::is_convertible_v<decltype(op), std::function<S(S, S)>>,
                  "op must work as S(S, S)");
    static_assert(std::is_convertible_v<decltype(e), std::function<S()>>,
                  "e must work as S()");
    static_assert(
        std::is_convertible_v<decltype(mapping), std::function<S(F, S)>>,
        "mapping must work as S(F, S)");
    static_assert(
        std::is_convertible_v<decltype(composition), std::function<F(F, F)>>,
        "compostiion must work as F(F, F)");
    static_assert(std::is_convertible_v<decltype(id), std::function<F()>>,
                  "id must work as F()");

#else

template <class S,
          S (*op)(S, S),
          S (*e)(),
          class F,
          S (*mapping)(F, S),
          F (*composition)(F, F),
          F (*id)()>
struct lazy_segtree {

#endif

  public:
    lazy_segtree() : lazy_segtree(0) {}
    explicit lazy_segtree(int n) : lazy_segtree(std::vector<S>(n, e())) {}
    explicit lazy_segtree(const std::vector<S>& v) : _n(int(v.size())) {
        size = (int)internal::bit_ceil((unsigned int)(_n));
        log = internal::countr_zero((unsigned int)size);
        d = std::vector<S>(2 * size, e());
        lz = std::vector<F>(size, id());
        for (int i = 0; i < _n; i++) d[size + i] = v[i];
        for (int i = size - 1; i >= 1; i--) {
            update(i);
        }
    }

    void set(int p, S x) {
        assert(0 <= p && p < _n);
        p += size;
        for (int i = log; i >= 1; i--) push(p >> i);
        d[p] = x;
        for (int i = 1; i <= log; i++) update(p >> i);
    }

    S get(int p) {
        assert(0 <= p && p < _n);
        p += size;
        for (int i = log; i >= 1; i--) push(p >> i);
        return d[p];
    }

    S prod(int l, int r) {
        assert(0 <= l && l <= r && r <= _n);
        if (l == r) return e();

        l += size;
        r += size;

        for (int i = log; i >= 1; i--) {
            if (((l >> i) << i) != l) push(l >> i);
            if (((r >> i) << i) != r) push((r - 1) >> i);
        }

        S sml = e(), smr = e();
        while (l < r) {
            if (l & 1) sml = op(sml, d[l++]);
            if (r & 1) smr = op(d[--r], smr);
            l >>= 1;
            r >>= 1;
        }

        return op(sml, smr);
    }

    S all_prod() { return d[1]; }

    void apply(int p, F f) {
        assert(0 <= p && p < _n);
        p += size;
        for (int i = log; i >= 1; i--) push(p >> i);
        d[p] = mapping(f, d[p]);
        for (int i = 1; i <= log; i++) update(p >> i);
    }
    void apply(int l, int r, F f) {
        assert(0 <= l && l <= r && r <= _n);
        if (l == r) return;

        l += size;
        r += size;

        for (int i = log; i >= 1; i--) {
            if (((l >> i) << i) != l) push(l >> i);
            if (((r >> i) << i) != r) push((r - 1) >> i);
        }

        {
            int l2 = l, r2 = r;
            while (l < r) {
                if (l & 1) all_apply(l++, f);
                if (r & 1) all_apply(--r, f);
                l >>= 1;
                r >>= 1;
            }
            l = l2;
            r = r2;
        }

        for (int i = 1; i <= log; i++) {
            if (((l >> i) << i) != l) update(l >> i);
            if (((r >> i) << i) != r) update((r - 1) >> i);
        }
    }

    template <bool (*g)(S)> int max_right(int l) {
        return max_right(l, [](S x) { return g(x); });
    }
    template <class G> int max_right(int l, G g) {
        assert(0 <= l && l <= _n);
        assert(g(e()));
        if (l == _n) return _n;
        l += size;
        for (int i = log; i >= 1; i--) push(l >> i);
        S sm = e();
        do {
            while (l % 2 == 0) l >>= 1;
            if (!g(op(sm, d[l]))) {
                while (l < size) {
                    push(l);
                    l = (2 * l);
                    if (g(op(sm, d[l]))) {
                        sm = op(sm, d[l]);
                        l++;
                    }
                }
                return l - size;
            }
            sm = op(sm, d[l]);
            l++;
        } while ((l & -l) != l);
        return _n;
    }

    template <bool (*g)(S)> int min_left(int r) {
        return min_left(r, [](S x) { return g(x); });
    }
    template <class G> int min_left(int r, G g) {
        assert(0 <= r && r <= _n);
        assert(g(e()));
        if (r == 0) return 0;
        r += size;
        for (int i = log; i >= 1; i--) push((r - 1) >> i);
        S sm = e();
        do {
            r--;
            while (r > 1 && (r % 2)) r >>= 1;
            if (!g(op(d[r], sm))) {
                while (r < size) {
                    push(r);
                    r = (2 * r + 1);
                    if (g(op(d[r], sm))) {
                        sm = op(d[r], sm);
                        r--;
                    }
                }
                return r + 1 - size;
            }
            sm = op(d[r], sm);
        } while ((r & -r) != r);
        return 0;
    }

  private:
    int _n, size, log;
    std::vector<S> d;
    std::vector<F> lz;

    void update(int k) { d[k] = op(d[2 * k], d[2 * k + 1]); }
    void all_apply(int k, F f) {
        d[k] = mapping(f, d[k]);
        if (k < size) lz[k] = composition(f, lz[k]);
    }
    void push(int k) {
        all_apply(2 * k, lz[k]);
        all_apply(2 * k + 1, lz[k]);
        lz[k] = id();
    }
};

}  // namespace atcoder

#endif  // ATCODER_LAZYSEGTREE_HPP

using namespace atcoder;

struct S {
    int min_index;
	ll min_value;
};

using F = ll;

S op(S l, S r) {
	int mi;
	ll mv;
	
	if (l.min_value <= r.min_value) {
		mi = l.min_index;
		mv = l.min_value;
	} else {
		mi = r.min_index;
		mv = r.min_value;
	}
	// dbg(l.min_value, r.min_value, mv);

    return S{mi, mv};
}

S e() { return S{-1, (ll)1e18}; }

S mapping(F l, S r) {
    return S{r.min_index, min(l, r.min_value)};
}

F composition(F l, F r) { return min(l, r); }

F id() { return (ll)1e18; }

// struct S2 {
//     vi three;
// };

// using F2 = int;

// S2 op2(S2 l, S2 r) {
// 	copy(r.begin(), r.end(), back_inserter(l));
//     return S2{
//         l
//     };
// }

// S2 e2() { return vi(); }

// S2 mapping2(F2 l, S2 r) {
// 	r.push_back(l);
//     return S2{r};
// }

// F2 composition2(F2 l, F2 r) { return l + r; }

// F2 id2() { return -1; }

struct Node {
	int _l, _r;
	Node *_left, *_right;
	set<int> _v;
	public:
    	Node(int l, int r) : _l(l), _r(r) {
			_v = set<int>();
			if (l != r) {
				int mi = (l + r) / 2;
				_left = new Node(l, mi);
				_right = new Node(mi + 1, r);
			}
		}
		void add(int p, int l, int r) {
			if (_l > r || _r < l) return;
			if (_l >= l && _r <= r) {
				_v.insert(p);
			} else {
				_left->add(p, l, r);
				_right->add(p, l, r);
			}
		}
		void get(int idx, set<int> &z) {
			if (_l == _r) {
				for (auto x : _v) z.insert(x);
				_v = set<int>();
			} else {
				if (idx <= (_l + _r) / 2) {
					_left->get(idx, z);
				} else {
					_right->get(idx, z);
				}
				for (auto x : _v) z.insert(x);
				_v = set<int>();
			}
		}
};


int main() {
    cin.tie(0)->sync_with_stdio(false);
	int n, q, s;
	cin >> n >> q >> s;
	s--;
	lazy_segtree<S, op, e, F, mapping, composition, id> A(n);
	Node B(0, n-1);
    // lazy_segtree<S2, op2, e2, F2, mapping2, composition2, id2> B(n);
	vvi plans;
	map<int, vi> two;
	map<int, vi> one;
	for (int i = 0;i < q;i++) {
		int t;
		cin >> t;
		if (t == 3) {
			int v, l, r, w;
			cin >> v >> l >> r >> w;
			v--; l--; r--;
			plans.push_back({v, l, r, w});
			B.add(i, l, r);
		} else if (t == 2) {
			int v, l, r, w;
			cin >> v >> l >> r >> w;
			v--; l--; r--;
			plans.push_back({v, l, r, w});
			two[v].push_back(i);
		} else {
			int v, u, w;
			cin >> v >> u >> w;
			v--; u--;
			plans.push_back({v, u, w});
			one[v].push_back(i);
		}
	}
	for (int i = 0;i < n;i++) A.set(i, S{i, (ll)1e18});
	A.set(s, S{s, (ll)0});
	vll ret(n, -1);
	for (int j = 0;j < n;j++) {
		S ss = A.all_prod();
		int cur = ss.min_index;
		ll v = ss.min_value;
		// dbg(cur, v);
		if (v > (ll)1e17) {
			break;
		}
		ret[cur] = v;
		for (auto p : one[cur]) {
			A.apply(plans[p][1], v + plans[p][2]);
		}
		for (auto p : two[cur]) {
			A.apply(plans[p][1], plans[p][2] + 1, v + plans[p][3]);
		}
		set<int> z;
		B.get(cur, z);
		// dbg(z);
		for (auto p : z) {
			A.apply(plans[p][0], v + plans[p][3]);
		}
		// dbg(A.all_prod().min_index);
		A.set(cur, S{cur, (ll)1e18});
		// dbg(A.all_prod().min_index);

	}
	for (auto x : ret) {
		cout << x << " ";
	}
	cout << endl;
}