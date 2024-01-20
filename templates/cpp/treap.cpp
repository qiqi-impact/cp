#pragma GCC optimize("Ofast")
// #pragma GCC target("avx,avx2,fma")

#include "bits/stdc++.h"

//#define NDEBUG
#define F first
#define S second
#define vec vector
#define pb push_back
#define pll pair<ll, ll>
#define pdd pair<ld, ld>
#define pii pair<int, int>
#define all(m) m.begin(), m.end()
#define rall(m) m.rbegin(), m.rend()
#define uid uniform_int_distribution
#define timeStamp() std::chrono::steady_clock::now()
#define unify(m) sort(all(m)), m.erase(unique(all(m)), m.end());
#define duration_micro(a) chrono::duration_cast<chrono::microseconds>(a).count()
#define duration_milli(a) chrono::duration_cast<chrono::milliseconds>(a).count()
#define fast cin.tie(0), cout.tie(0), cin.sync_with_stdio(0), cout.sync_with_stdio(0);
using namespace std;
using str = string;
using ll = long long;
using ld = long double;
using uint = unsigned int;
using ull = unsigned long long;
mt19937 rnd(timeStamp().time_since_epoch().count());
mt19937_64 rndll(timeStamp().time_since_epoch().count());
template<typename T, typename U> bool chmin(T& a, const U& b) {return (T)b < a ? a = b, 1 : 0;}
template<typename T, typename U> bool chmax(T& a, const U& b) {return (T)b > a ? a = b, 1 : 0;}
struct custom_hash {static uint64_t xs(uint64_t x) {x += 0x9e3779b97f4a7c15; x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9; x = (x ^ (x >> 27)) * 0x94d049bb133111eb; return x ^ (x >> 31);} template<typename T> size_t operator()(T x) const {static const uint64_t C = timeStamp().time_since_epoch().count(); return xs(hash<T> {}(x) + C);}};
template<typename K> using uset = unordered_set<K, custom_hash>;
template<typename K, typename V> using umap = unordered_map<K, V, custom_hash>;
template<typename T1, typename T2> ostream& operator<<(ostream& out, const pair<T1, T2>& x) {return out << x.F << ' ' << x.S;}
template<typename T1, typename T2> istream& operator>>(istream& in, pair<T1, T2>& x) {return in >> x.F >> x.S;}
template<typename T, size_t N> istream& operator>>(istream& in, array<T, N>& a) {for (auto &x : a) in >> x; return in;}
template<typename T, size_t N> ostream& operator<<(ostream& out, const array<T, N>& a) {for (size_t i = 0; i < a.size(); ++i) {out << a[i];if (i + 1 < a.size()) out << ' ';}return out;}
template<typename T> istream& operator>>(istream& in, vector<T>& a) {for (auto& x : a) in >> x; return in;}
template<typename T> ostream& operator<<(ostream& out, const vector<T>& a) {for (size_t i = 0; i < a.size(); ++i) {out << a[i]; if (i + 1 < a.size()) out << ' ';} return out;}

template<typename I> auto array_cnt(I f, I l) {umap<typename iterator_traits<I>::value_type, int> mp; while (f != l) ++mp[*f], ++f; return mp;}
template<typename I> auto subset_sum(I f, I l) {int a = l - f; vec<typename iterator_traits<I>::value_type> o(1 << a); for (int q = 1; q < (1 << a); ++q) {const int i = __builtin_ctz(q); o[q] = *(f + i) + o[q ^ (1 << i)];} return o;}
template<typename I> vec<pii> get_segs_of_eq_elems(I first, I last) {using T = typename iterator_traits<I>::value_type; vec<pii> ans; if (first == last) return ans; int l = 0; T prev = *first; int r = 1; for (auto cit = next(first); cit != last; ++cit, ++r) {if (*cit != prev) {ans.pb({l, r - 1}); l = r;} prev = *cit;} ans.pb({l, r - 1}); return ans;}
template<typename I> int LCP(I f1, I l1, I f2, I l2) {for (int o = 0; ; ++f1, ++f2, ++o) if (f1 == l1 || f2 == l2 || *f1 != *f2) return o; return -1;}
template<typename I> int min_period(I f, I l) {int a = l - f; vec<int> m(a); for (int q = 1; q < a; ++q) {for (int w = m[q - 1]; w && !m[q]; w = m[w - 1]) {if (*(f + q) == *(f + w)) m[q] = w + 1;} m[q] += !m[q] && *(f + q) == *f;} int p = a - m.back(); return a % p ? a : p;}
template<typename I> bool is_palindrome(I f, I l) {for (--l; f < l; ++f, --l) if (*f != *l) return 0; return 1;}
str from_base_10_to_base_b(ll x, ll b) {str t; if (x == 0) t = "0"; for (; x; x /= b) t += (char)('0' + x % b); reverse(all(t)); return t;}
#define vi vec<int>
#define vl vec<ll>
#define vvi vec<vec<int>>
#define vvvi vec<vec<vec<int>>>
#define vvl vec<vec<ll>>
#define vpi vec<pii>
#define vpl vec<pll>
#define vs vec<str>
#define vvs vec<vec<str>>
const int dx[] = { -1, 0, 1, 0, -1, 1, 1, -1};
const int dy[] = {0, 1, 0, -1, 1, 1, -1, -1};
template<typename T_arr> int LCP(T_arr m1, T_arr m2) {return LCP(all(m1), all(m2));}
template<typename T_arr> T_arr subset_sum(T_arr m) {return subset_sum(all(m));}
template<typename T_arr> vec<pii> get_segs_of_eq_elems(T_arr m) {return get_segs_of_eq_elems(all(m));}
template<typename T> int sum_of_digits(T val) {int o = 0; for (; val; val /= 10) o += val % 10; return o;}
template<typename T> struct static_sum_query {vec<T> m; static_sum_query() = default; template<typename I>static_sum_query(I f, I l) {m.resize(l - f + 1); for (auto it = m.begin() + 1; f != l; ++f, ++it) {*it = *(it - 1) + *f;}} template<typename T_arr> static_sum_query(T_arr& m) {(*this) = static_sum_query(all(m));} inline T query(const int l, const int r) const {return m[r + 1] - m[l];}};
template<typename T> vec<pair<T, int>> zip_with_positions(vec<T> &m) {int a = m.size(); vec<pair<T, int>> ans(a); for (int q = 0; q < a; ++q) ans[q] = {m[q], q}; return ans;}
template<typename T> str join(vec<T> &m, str c) {str o; if constexpr(is_same<str, T>::value) {for (const T &s : m) o += s + c;} else {for (const T &s : m) o += to_string(s) + c;} if (o.size()) o.erase(o.end() - c.size(), o.end()); return o;}
vec<pii> get_reflection_points_in_rect(int a, int b, int x, int y) {assert(0 <= x && x < a); assert(0 <= y && y < b); vec<pii> res = {{x, y}}; if (x != a - x - 1) res.pb({a - x - 1, y}); if (y != a - y - 1) res.pb({x, a - y - 1}); if (x != a - x - 1 && y != a - y - 1) res.pb({a - x - 1, a - y - 1}); return res;}
vec<pii> get_rotation_points_in_square(int a, int x, int y) {assert(0 <= x && x < a); assert(0 <= y && y < a); vec<pii> res = {{x, y}}; if (a % 2 == 1 && x == a / 2 && y == a / 2) return res; res.pb({a - y - 1, x}); res.pb({a - x - 1, a - y - 1}); res.pb({y, a - x - 1}); return res;}
template<typename T> vec<vec<int>> get_cycles_of_perm(vec<T> &m, int permutation_indexation) {int a = m.size(); vec<vec<int>> ans; vec<bool> us(a); for (int q = 0; q < a; ++q) {if (us[q]) continue; vec<int> tyt; for (int w = q; !us[w]; w = m[w] - permutation_indexation) {tyt.pb(w); us[w] = 1;} ans.pb(tyt);} return ans;}
int find_closing_bracket(str &s, int i) {char op = s[i], cl = op == '(' ? ')' : op == '{' ? '}' : op == '[' ? ']' : op == '<' ? '>' : '@'; assert(cl != '@'); int dep = 1; for (int q = i + 1; q < s.size(); ++q) {dep += s[q] == op ? 1 : s[q] == cl ? -1 : 0; if (dep == 0) return q;} return -1;}
template<typename T> vec<pair<T, T>> vv_to_vp(vec<vec<T>> &m) {int a = m.size(); vec<pair<T, T>> ans(a); for (int q = 0; q < a; ++q) ans[q] = {m[q][0], m[q][1]}; return ans;}
template<const int k, typename T> vec<array<T, k>> vv_to_varr(vec<vec<T>> &m) {int a = m.size(); vec<array<T, k>> ans(a); for (int q = 0; q < a; ++q) for (int w = 0; w < k; ++w) ans[q][w] = m[q][w]; return ans;}
template<typename T_arr> int min_period(T_arr m) {return min_period(all(m));}
template<typename T_arr> bool is_palindrome(T_arr m) {return is_palindrome(all(m));}
template<typename T_arr> T_arr reverse(T_arr x) {reverse(all(x)); return x;}
str from_base_10_to_base_b(str x, ll b) {return from_base_10_to_base_b(stoll(x), b);}
ll from_base_b_to_base_10(str x, ll b) {ll o = 0, pw = 1; for (int q = x.size() - 1; q >= 0; --q, pw *= b) o += (x[q] - '0') * pw; return o;}
str from_base_a_to_base_b(str x, ll a, ll b) {ll x10 = from_base_b_to_base_10(x, a); return from_base_10_to_base_b(x10, b);}
template<typename T> T binpow(T x, T k) {if (k < 0) return 0; T o = 1; for (; k; k >>= 1) {if (k & 1) o = o * x; x = x * x;} return o;}
template<typename T> T ar_prog_sum_fcl(T first, T cnt, T last) {return (first + last) * cnt / 2;}
template<typename T> T ar_prog_sum_fdc(T first, T diff, T cnt) {return (first * 2 + diff * (cnt - 1)) * cnt / 2;}
template<typename T> T ar_prog_sum_fdl(T first, T diff, T last) {return (first + last) * ((last - first) / diff + 1) / 2;}
template<typename T> T geom_prog_sum_fdl(T first, T diff, T last) {return (last * diff - first) / (diff - 1);}
template<typename T> T geom_prog_sum_fdc(T first, T diff, T cnt) {return (first * binpow(diff, cnt) - first) / (diff - 1);}
template<typename T> vec<vec<T>> transpose_matrix(vec<vec<T>> &m) {int a = m.size(), b = a ? m[0].size() : 0; vec<vec<T>> ans(b, vec<T>(a)); for (int q = 0; q < a; ++q) {for (int w = 0; w < b; ++w) {ans[w][q] = m[q][w];}} return ans;}
template<typename T> vec<vec<T>> rotate_matrix_cw(vec<vec<T>> &m) {int a = m.size(), b = a ? m[0].size() : 0; vec<vec<T>> ans(b, vec<T>(a)); for (int w = 0; w < b; ++w) for (int q = 0; q < a; ++q) ans[w][q] = m[a - 1 - q][w]; return ans;}
complex<ll> str_to_cmpl_ll(str t) {int ps = t.find('+'), sgn = 1; if (ps == string::npos) {ps = t.find('-'); sgn = -1; assert(ps != string::npos);} str t1 = t.substr(0, ps), t2 = t.substr(ps + 1); assert(t2.back() == 'i'); t2.pop_back(); return {stoll(t1), stoll(t2) * sgn};}
int time_to_minutes(int h, int m) {return h * 60 + m;}
int time_to_minutes(str s) {int ps = s.find(':'); assert(ps != string::npos); return time_to_minutes(stoi(s.substr(0, ps)), stoi(s.substr(ps + 1)));}
str minutes_to_time(int m, bool h0 = true, bool m0 = true) {int h = m / 60; m %= 60; str o; if (h0) o += (h < 10 ? "0" : ""); o += to_string(h); o += ':'; if (m0) o += (m < 10 ? "0" : ""); o += to_string(m); return o;}
ll lcm(ll x, ll y) {return x / __gcd(x, y) * y;}
bool is_vowel_lowercase(char c) {return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';}
bool is_consonant_lowercase(char c) {return !is_vowel_lowercase(c);}
uint leq_pow2(const uint x) {return 1u << __lg(x);}
ull leq_pow2ll(const ull x) {return 1ull << __lg(x);}
uint geq_pow2(const uint x) {return x & (x - 1) ? 2u << __lg(x) : x;}
ull geq_pow2ll(const ull x) {return x & (x - 1) ? 2ull << __lg(x) : x;}
ll sqd(const pll p1, const pll p2) {return (p1.F - p2.F) * (p1.F - p2.F) + (p1.S - p2.S) * (p1.S - p2.S);}
ll sqd(const ll x1, const ll y1, const ll x2, const ll y2) {return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);}
template<typename T> int sign(T x) {return x < 0 ? -1 : x > 0 ? 1 : 0;}
template<typename T_arr> auto array_cnt(T_arr m) {return array_cnt(all(m));}
template<typename I> bool is_B_subseq_A(I A_beg, I A_end, I B_beg, I B_end) {for (; A_beg != A_end && B_beg != B_end; ++A_beg) if (*A_beg == *B_beg) ++B_beg; return B_beg == B_end;}
vec<ll> get_divisors(ll x) {vec<ll> ans1, ans2; for (ll q = 1; q * q <= x; ++q) {if (x % q == 0) {ans1.pb(q); ans2.pb(x / q);}} if (ans1.back() == ans2.back()) ans1.pop_back(); reverse(all(ans2)); for (ll i : ans2) ans1.pb(i); return ans1;}
bool is_prime(ll c) {if (c < 2) return 0; if (c == 2 || c == 3) return 1; if (c % 2 == 0 || c % 3 == 0) return 0; const ll gr = sqrtl(c) + 1; for (ll q = 6; q <= gr; q += 6) {if (c % (q - 1) == 0) return 0; if (c % (q + 1) == 0) return 0;} return 1;}
vec<str> split(str &s, char c, bool ignore_empty = false) {vec<str> o; str u; for (int q = 0; q < s.size(); q++) {if (s[q] == c) {if (!u.empty() || !ignore_empty) o.pb(u); u.clear();} else u += s[q];} if (!u.empty() || !ignore_empty) o.pb(u); return o;}
int replace(str &s, str from, str to) {str t = from; t.pb(0); t += s; int a = t.size(); vec<int> m(a); for (int q = 1; q < a; ++q) {for (int w = m[q - 1]; w && !m[q]; w = m[w - 1]) {if (t[q] == t[w]) m[q] = w + 1;} m[q] += !m[q] && t[q] == t[0];} int szf = from.size(), lst = szf; for (int q = szf; q < t.size(); ++q) {if (m[q] == szf && q - lst >= szf) {m[q - szf + 1] = -1; lst = q;}} str ans; int o = 0; for (int q = szf + 1; q < t.size(); ++q) {if (m[q] != -1) ans += t[q]; else ans += to, q += szf - 1, ++o;} s = ans; return o;}
template<typename T> T mul_threshold(T a, T b, T threshold) {if (!a || !b || !threshold) return 0; assert(a > 0 && b > 0); T max_b = threshold / a; return b <= max_b ? a * b : threshold;}
template<typename T> T count_set_bits_pref(T n, int b) {assert(0 <= n); T pw = (T)(1) << b; if (pw > n) return 0; T period = pw * 2; T full = (n + 1) / period; T rem = (n + 1) & (period - 1); return full * pw + (rem < pw ? 0 : rem - pw);}
template<typename T> T count_set_bits_seg(T l, T r, int b) {assert(0 <= l && l <= r); return count_set_bits_pref(r, b) - (l ? count_set_bits_pref(l - 1, b) : 0);}
template<typename T> T integral_tersearch_argmin(auto f, T l, T r) {static_assert(is_integral_v<decltype(l)>); using U = decltype(f(l)); const ld FI = 1.6180339887498948482045868343656381177203; T p1 = l + (r - l) / (FI + 1), p2 = r - (r - l) / (FI + 1); U v1 = f(p1), v2 = f(p2); while (r - l > 7) {if (v1 < v2) {r = p2; p2 = p1, v2 = v1; p1 = l + (r - l) / (FI + 1), v1 = f(p1);} else {l = p1; p1 = p2, v1 = v2; p2 = r - (r - l) / (FI + 1), v2 = f(p2);}} T best_arg = l; U best_val = f(l), prv = best_val; while (++l <= r) {U tyt = l == p1 ? v1 : l == p2 ? v2 : f(l); if (tyt > prv) break; if (chmin(best_val, tyt)) best_arg = l; prv = tyt;} return best_arg;};
template<typename T> T integral_binary_search_last_when_true(auto f, T l, T r) {static_assert(is_same<decltype(l), decltype(r)>::value); while (l + 1 < r) {T md = l + (r - l) / 2; if (f(md))l = md; else r = md;} return l;};
template<typename T> T integral_binary_search_last_when_true(auto f, T l) {T d = 1; while (f(l + d)) d *= 2; d /= 2; for (T u = d; u; u /= 2) if (f(l + d + u)) d += u; return l + d;};

template<typename K>
class treap {
    struct Node {
        Node* l = 0;
        Node* r = 0;
        int y;
        size_t sz;

        K key;
        K mnk;
        K mxk;
        K smk;

        Node(K k): y(rnd()), sz(1) {
            key = k;
            mnk = k;
            mxk = k;
            smk = k;
        }
    };
    Node* root = 0;

    K last_erased_key;

    K gmnk(Node* n) const {return n ? n->mnk : std::numeric_limits<K>::max();}
    K gmxk(Node* n) const {return n ? n->mxk : std::numeric_limits<K>::min();}
    K gsmk(Node* n) const {return n ? n->smk : 0;}

    size_t gsz(Node* n) const {return n ? n->sz : 0;}

    //Write, if need
    void apply_push(Node* n) {
        if (!n) return;
    }
    void push(Node* n) {
        if (!n) return;
    }

    void upd(Node* n) {
        if (!n) return;
        n->mnk = min({gmnk(n->l), n->key, gmnk(n->r)});
        n->mxk = max({gmxk(n->l), n->key, gmxk(n->r)});
        n->smk = gsmk(n->l) + n->key + gsmk(n->r);

        n->sz = gsz(n->l) + 1 + gsz(n->r);
    }

    Node* merge(Node* l, Node* r) {
        if (!l || !r) return l ? l : r;
        if (l->y > r->y) {
            push(l);
            l->r = merge(l->r, r); upd(l);
            return l;
        }
        push(r);
        r->l = merge(l, r->l); upd(r);
        return r;
    }

    array<Node*, 2> split_size(Node* n, size_t k) {
        if (!n) return {0, 0};
        push(n);
        if (k <= gsz(n->l)) {
            array<Node*, 2> p = split_size(n->l, k);
            n->l = p[1]; upd(n);
            p[1] = n;
            return p;
        }
        array<Node*, 2> p = split_size(n->r, k - gsz(n->l) - 1);
        n->r = p[0]; upd(n);
        p[0] = n;
        return p;
    }

    array<Node*, 2> split_key(Node* n, K key) {
        if (!n) return {0, 0};
        push(n);
        if (key < n->key) {
            array<Node*, 2> p = split_key(n->l, key);
            n->l = p[1]; upd(n);
            p[1] = n;
            return p;
        }
        array<Node*, 2> p = split_key(n->r, key);
        n->r = p[0]; upd(n);
        p[0] = n;
        return p;
    }

    template<typename I>
    Node* build(I f_key, I l_key) {
        if (f_key >= l_key) return 0;
        I md = f_key + (l_key - f_key) / 2;
        Node* n = new Node(*md);
        n->l = build(f_key, md);
        n->r = build(md + 1, l_key);
        upd(n);
        return n;
    }

    void update_key_at_pos(Node* n, size_t pos, K new_key) {
        push(n);
        if (pos == gsz(n->l)) {n->key = new_key; upd(n); return;}
        if (pos < gsz(n->l)) update_key_at_pos(n->l, pos, new_key);
        else update_key_at_pos(n->r, pos - gsz(n->l) - 1, new_key);
        upd(n);
    }

    Node* erase_pos(Node* n, size_t pos) {
        push(n);
        if (gsz(n->l) == pos) {
            last_erased_key = n->key;
            Node* l = n->l, *r = n->r;
            delete n;
            return merge(l, r);
        }
        if (pos < gsz(n->l)) n->l = erase_pos(n->l, pos);
        else n->r = erase_pos(n->r, pos - gsz(n->l) - 1);
        upd(n);
        return n;
    }

    Node* insert_node(Node* n, Node* nw) {
        push(n);
        if (!n || nw->y > n->y) {
            auto [lf, rg] = split_key(n, nw->key);
            nw->l = lf;
            nw->r = rg;
            upd(nw);
            return nw;
        }
        if (nw->key < n->key) n->l = insert_node(n->l, nw);
        else n->r = insert_node(n->r, nw);
        upd(n);
        return n;
    }

    Node* erase_one_key(Node* n, K key) {
        if (!n) return 0;
        push(n);
        if (n->key == key) {
            Node* l = n->l, *r = n->r;
            delete n;
            return merge(l, r);
        }
        if (key < n->key) n->l = erase_one_key(n->l, key);
        else n->r = erase_one_key(n->r, key);
        upd(n);
        return n;
    }

    void get_keys_on_subsegment(Node* n, size_t l, size_t& len, vector<K>& res) {
        if (!n || !len) return;
        push(n);
        if (l < gsz(n->l)) get_keys_on_subsegment(n->l, l, len, res);
        if (l <= gsz(n->l) && len) res.push_back(n->key), --len;
        if (l > gsz(n->l) + 1) get_keys_on_subsegment(n->r, l - gsz(n->l) - 1, len, res);
    }

    K kth_elem(Node* n, size_t k) {
        assert(0 <= k && k < gsz(n));
        while (n) {
            push(n);
            const size_t szl = gsz(n->l);
            if (k == szl) return n->key;
            if (k < szl) n = n->l;
            else k -= szl + 1, n = n->r;
        }
        assert(0);
        return K();
    }

    size_t pos_of_leftest_good(Node* n, auto has_good, auto is_good) {
        size_t ans = 0;
        while (n) {
            push(n);
            if (has_good(n->l)) n = n->l;
            else if (is_good(n)) return ans + gsz(n->l);
            else ans += gsz(n->l) + 1, n = n->r;
        }
        return ans;
    }

    size_t pos_of_rightest_good(Node* n, auto has_good, auto is_good) {
        size_t ans = 0;
        while (n) {
            push(n);
            if (has_good(n->r)) ans += gsz(n->l) + 1, n = n->r;
            else if (is_good(n)) return ans + gsz(n->l);
            else n = n->l;
        }
        return ans;
    }

    size_t pos_of_closest_from_right_good(Node* n, size_t pos, auto has_good, auto is_good) {
        size_t szr = gsz(n);
        if (pos >= szr || !has_good(n)) return szr;
        size_t ans = 0, pos_to_ret = szr;
        Node* u = 0;
        while (n) {
            push(n);
            if (pos >= gsz(n->l)) {
                if (pos == gsz(n->l) && is_good(n)) return ans + gsz(n->l);
                ans += gsz(n->l) + 1;
                pos -= min(pos, gsz(n->l) + 1);
                n = n->r;
            } else {
                if (is_good(n)) pos_to_ret = ans + gsz(n->l), u = 0;
                else if (has_good(n->r)) pos_to_ret = ans + gsz(n->l) + 1, u = n->r;
                n = n->l;
            }
        }
        return pos_to_ret + (u ? pos_of_leftest_good(u, has_good, is_good) : 0);
    }

    size_t pos_of_closest_from_left_good(Node* n, size_t pos, auto has_good, auto is_good) {
        size_t szr = gsz(n);
        if (!has_good(n)) return szr;
        pos = min(pos, szr - 1);
        pos = szr - 1 - pos;
        size_t ans = 0, pos_to_ret = szr;
        Node* u = 0;
        while (n) {
            push(n);
            if (pos >= gsz(n->r)) {
                if (pos == gsz(n->r) && is_good(n)) return szr - 1 - (ans + gsz(n->r));
                ans += gsz(n->r) + 1;
                pos -= min(pos, gsz(n->r) + 1);
                n = n->l;
            } else {
                if (is_good(n)) pos_to_ret = ans + gsz(n->r), u = 0;
                else if (has_good(n->l)) pos_to_ret = ans + gsz(n->r) + 1, u = n->l;
                n = n->r;
            }
        }
        if (pos_to_ret == szr) return szr;
        pos_to_ret = szr - 1 - pos_to_ret;
        return pos_to_ret - (u ? gsz(u) - 1 - pos_of_rightest_good(u, has_good, is_good) : 0);
    }

    size_t pos_of_leftest_min_key(Node* n) {
        K mnk = gmnk(n);
        return pos_of_leftest_good(n, 
            [&](Node* n){return gmnk(n) == mnk;},
            [&](Node* n){return n->key == mnk;});
    }

    size_t pos_of_rightest_min_key(Node* n) {
        K mnk = gmnk(n);
        return pos_of_rightest_good(n, 
            [&](Node* n){return gmnk(n) == mnk;},
            [&](Node* n){return n->key == mnk;});
    }

    size_t pos_of_leftest_key_leq(Node* n, K key) {
        return pos_of_leftest_good(n, 
            [&](Node* n){return gmnk(n) <= key;},
            [&](Node* n){return n->key <= key;});
    }

    size_t pos_of_closest_from_left_key_leq(Node* n, size_t pos, K key) {
        return pos_of_closest_from_left_good(n, pos,
            [&](Node* n){return gmnk(n) <= key;},
            [&](Node* n){return n->key <= key;});
    }

    size_t pos_of_closest_from_right_key_leq(Node* n, size_t pos, K key) {
        return pos_of_closest_from_right_good(n, pos,
            [&](Node* n){return gmnk(n) <= key;},
            [&](Node* n){return n->key <= key;});
    }

    void print_keys(Node* n) {if (!n) return; push(n); print_keys(n->l); cout << n->key << ' '; print_keys(n->r);}

    void delete_subtree(Node* n) {if (!n) return; push(n); delete_subtree(n->l); delete_subtree(n->r); delete n;}

    void cyclic_shift_left(Node*& n, int shift) {if (shift < 0) cyclic_shift_right(-shift); else {if (gsz(n) == 0) return; if (shift >= gsz(n)) shift %= gsz(n); auto [lf, rg] = split_size(n, shift); n = merge(rg, lf);}}
    void cyclic_shift_right(Node*& n, int shift) {if (shift < 0) cyclic_shift_left(-shift); else {if (gsz(n) == 0) return; if (shift >= gsz(n)) shift %= gsz(n); auto [lf, rg] = split_size(n, gsz(n) - shift); n = merge(rg, lf);}}

public:
    treap() = default;
    template<typename I> treap(I f_key, I l_key) {root = build(f_key, l_key);}
    ~treap() {delete_subtree(root);}

    size_t size() const {return gsz(root);}
    bool empty() const {return root == 0;}

    template<typename I> void insert_array_at_pos(size_t pos, I first, I last) {auto [lf, rg] = split_size(root, pos); root = merge(merge(lf, build(first, last)), rg);}
    template<typename T> void insert_array_at_pos(size_t pos, initializer_list<T> il) {auto [lf, rg] = split_size(root, pos); root = merge(merge(lf, build(il.begin(), il.end())), rg);}
    void insert_key_at_pos(size_t pos, K key) {auto [lf, rg] = split_size(root, pos); root = merge(merge(lf, new Node(key)), rg);}
    void insert_key(K key) {root = insert_node(root, new Node(key));}

    void update_key_at_pos(size_t pos, K new_key) {update_key_at_pos(root, pos, new_key);}

    void erase_pos(size_t pos) {root = erase_pos(root, pos);}
    void erase_one_key(K key) {root = erase_one_key(root, key);}
    void erase_seg(size_t l, size_t len) {auto [lf, tmp] = split_size(root, l); auto [md, rg] = split_size(tmp, len); root = merge(lf, rg);}

    K extract_pos(size_t pos) {erase_pos(pos); return last_erased_key;}

    K operator[](size_t pos) {return kth_elem(root, pos);}
    
    bool contains(K key) {Node* n = root; while (n) {push(n); if (key == n->key) return true; n = key < n->key ? n->l : n->r;} return false;}
    size_t get_leftest_pos_of_key(K key) {Node* n = root; size_t pos = 0, o = size(); while (n) {push(n); if (key == n->key) o = min(o, pos + gsz(n->l)), n = n->l; else if (key < n->key) n = n->l; else pos += gsz(n->l) + 1, n = n->r;} assert(o < size() && "No such key"); return o;}

    size_t count_keys_leq(K key) {Node* n = root; size_t o = 0; while (n) {push(n); if (n->key <= key) o += gsz(n->l) + 1, n = n->r; else n = n->l;} return o;}
    size_t count_keys_less(K key) {Node* n = root; size_t o = 0; while (n) {push(n); if (n->key < key) o += gsz(n->l) + 1, n = n->r; else n = n->l;} return o;}
    size_t count_keys_in_seg(K l, K r) {return l > r ? 0 : count_keys_leq(r) - count_keys_less(l);}
    size_t count_keys_geq(K key) {return gsz(root) - count_keys_less(key);}
    size_t count_keys_greater(K key) {return gsz(root) - count_keys_leq(key);}
    size_t count_keys_eq(K key) {return count_keys_leq(key) - count_keys_less(key);}

    K pref_sumkey(size_t p) {Node* n = root; K sm = 0; while (n) {push(n); if (gsz(n->l) == p) return sm + gsmk(n->l) + n->key; if (gsz(n->l) < p) sm += gsmk(n->l) + n->key, p -= gsz(n->l) + 1, n = n->r; else n = n->l;} assert(0); return sm;}
    K seg_sumkey_fast(size_t l, size_t r) {return pref_sumkey(r) - (l ? pref_sumkey(l - 1) : 0);}
    K seg_sumkey_slow(size_t l, size_t r) {auto [lf, tmp] = split_size(root, l); auto [mid, rg] = split_size(tmp, r - l + 1); K ans = gsmk(mid); root = merge(merge(lf, mid), rg); return ans;}

    //If no such pos exists, these functions will return size()
    size_t get_pos_of_leftest_key_leq(K key) {return pos_of_leftest_key_leq(root, key);}
    size_t get_pos_of_closest_from_left_leq(size_t pos, K key) {return pos_of_closest_from_left_key_leq(root, pos, key);}
    size_t get_pos_of_closest_from_right_leq(size_t pos, K key) {return pos_of_closest_from_right_key_leq(root, pos, key);}

    size_t get_pos_of_leftest_min_key() {return pos_of_leftest_min_key(root);}
    size_t get_pos_of_rightest_min_key() {return pos_of_rightest_min_key(root);}

    void cyclic_shift_left(int shift) {cyclic_shift_left(root, shift);}
    void cyclic_shift_right(int shift) {cyclic_shift_right(root, shift);}
    void seg_cyclic_shift_left(size_t l, size_t r, int shift) {auto [lf, tmp] = split_size(root, l); auto [mid, rg] = split_size(tmp, r - l + 1); cyclic_shift_left(mid, shift); root = merge(merge(lf, mid), rg);}
    void seg_cyclic_shift_right(size_t l, size_t r, int shift) {auto [lf, tmp] = split_size(root, l); auto [mid, rg] = split_size(tmp, r - l + 1); cyclic_shift_right(mid, shift); root = merge(merge(lf, mid), rg);}

    void print_keys(string end_string = "") {print_keys(root); cout << end_string;}
    vector<K> get_keys_from_seg(size_t l, size_t len) {vector<K> res; get_keys_on_subsegment(root, l, len, res); return res;}
};

class Solution {
public:
    long long minimumCost(vector<int>& m, int k, int dist) {
        --k;
        treap<ll> t;
        ll mn = 1e18;
        ll a = m.size();
        for (int l = 1, r = 0; l + dist < a; t.erase_one_key(m[l]), ++l) {
            while (r != l + dist) t.insert_key(m[++r]);
            assert(t.size() >= k);
            chmin(mn, t.pref_sumkey(k - 1));
        }
        return m[0] + mn;
    }
};