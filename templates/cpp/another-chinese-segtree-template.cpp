template <class S>
struct SegTree {
  static S op(S a, S b) { return a + b; }
  static S e() { return S(); }

  int n;
  vector<S> seg;

  SegTree(int n): n(n) {
    seg.assign(n * 4, e());
  }

  SegTree(const vector<S> &a): SegTree(a.size() - 1) {
    auto build = [&](auto build, int u, int l, int r) {
      if (l == r) {
        seg[u] = a[l];
        return;
      }
      int mid = (l + r) / 2;
      build(build, u << 1, l, mid);
      build(build, u << 1 | 1, mid + 1, r);
      seg[u] = op(seg[u<<1], seg[u<<1|1]);
    };
    build(build, 1, 1, n);
  }

  void set(int p, S x) {
    auto update = [&](auto update, int u, int l, int r) {
      if (l == r) {
        seg[u] = x;
        return;
      }
      int mid = (l + r) / 2;
      if (p <= mid) update(update, u << 1, l, mid);
      else update(update, u << 1 | 1, mid + 1, r);
      seg[u] = op(seg[u<<1], seg[u<<1|1]);
    };
    update(update, 1, 1, n);
  }

  S get(int p) const {
    auto query = [&](auto query, int u, int l, int r) {
      if (l == r) return seg[u];
      int mid = (l + r) / 2;
      return p <= mid?
        query(query, u << 1, l, mid): query(query, u << 1 | 1, mid + 1, r);
    };
    return query(query, 1, 1, n);
  }

  S prod(int s, int t) const {
    auto query = [&](auto query, int u, int l, int r) {
      if (s <= l && r <= t) return seg[u];
      int mid = (l + r) / 2;
      if (t <= mid) return query(query, u << 1, l, mid);
      if (s > mid) return query(query, u << 1 | 1, mid + 1, r);
      return op(query(query, u << 1, l, mid), query(query, u << 1 | 1, mid + 1, r));
    };
    return query(query, 1, 1, n);
  }

  int max_right(int s, function<bool(S)> f) const {
    S pre = e();
    auto query = [&](auto query, int u, int l, int r) {
      if (s <= l && f(op(pre, seg[u]))) {
        pre = op(pre, seg[u]);
        return r;
      }
      if (l == r) return l - 1;
      int mid = (l + r) / 2;
      if (s <= mid) {
        int t = query(query, u << 1, l, mid);
        if (t < mid) return t;
      }
      return query(query, u << 1 | 1, mid + 1, r);
    };
    return query(query, 1, 1, n);
  }

  int min_left(int t, function<bool(S)> f) const {
    S suf = e();
    auto query = [&](auto query, int u, int l, int r) {
      if (r <= t && f(op(seg[u], suf))) {
        suf = op(seg[u], suf);
        return l;
      }
      if (l == r) return r + 1;
      int mid = (l + r) / 2;
      if (t > mid) {
        int s = query(query, u << 1 | 1, mid + 1, r);
        if (s > mid + 1) return s;
      }
      return query(query, u << 1, l, mid);
    };
    return query(query, 1, 1, n);
  }
};

struct Info {
    int v, f, b, l;
    Info(int v = 0, int f = 0, int b = 0, int l = 0): v(v), f(f), b(b), l(l) {}
    Info operator+(const Info &o) const {
        return Info{
            max({v, o.v, b + o.f}),
            f == l? l + o.f: f,
            o.b == o.l? b + o.l: o.b,
            l + o.l
        };
    }
};

class Solution {
public:
    vector<bool> getResults(vector<vector<int>>& queries) {
        int n = queries.size() * 3;
        vector<Info> a(n + 1, Info(1, 1, 1, 1));
        SegTree<Info> sgt(a);
        vector<bool> ret;
        for (auto &q: queries) {
            if (q[0] == 1) {
                int x = q[1];
                auto s = sgt.get(x);
                s.b = 0;
                sgt.set(x, s);
                if (x + 1 <= n) {
                    auto s = sgt.get(x + 1);
                    s.f = 0;
                    sgt.set(x + 1, s);
                }
            } else {
                int x = q[1], sz = q[2];
                ret.emplace_back(sgt.prod(1, x).v >= sz);
            }
        }
        return ret;
    }
};