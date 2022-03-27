#include <bits/stdc++.h>

using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

struct SegTree {
    static const int maxn = 1e5 + 1;

    struct Node {
        int lo, hi, pre, suf, ans;
    };

    Node n[maxn << 2];

    int lson(int idx) { return 2 * idx; }
    int rson(int idx) { return 2 * idx + 1; }

    void build(int lb, int rb, int idx) {
        Node &c = n[idx];
        c.lo = lb;
        c.hi = rb;
        c.pre = c.suf = c.ans = 0;
        if (lb != rb) {
            int mi = (lb+rb)/2;
            push(idx);
            build(lb, mi, lson(idx));
            build(mi+1, rb, rson(idx));
            pull(idx);
        }
    }

    int query(int L, int R, int idx) {
        Node &c = n[idx];
		if (R < c.lo || c.hi < L) return 0;
		if (L <= c.lo && c.hi <= R) return c.ans;
		push(idx);
        query(L, R, lson(idx));
        query(L, R, rson(idx));
        pull(idx);
		return c.ans;
	}

    void push(int idx) {}

    void pull(int idx) {
        Node &c = n[idx];
        Node &l = n[lson(idx)];
        Node &r = n[rson(idx)];
        c.ans = max(l.ans, r.ans);
        c.ans = max(c.ans, l.suf + r.pre);
        c.pre = l.pre;
        c.suf = r.suf;
        if (l.pre == l.hi - l.lo + 1) c.pre += r.pre;
        if (r.suf == r.hi - r.lo + 1) c.suf += l.suf;
    }

    void set(int L, int R, int idx, int x) {
        Node &c = n[idx];
		if (R < c.lo || c.hi < L) return;
		if (L <= c.lo && c.hi <= R) c.ans = c.suf = c.pre = x;
		else {
			push(idx);
            set(L, R, lson(idx), x);
            set(L, R, rson(idx), x);
            pull(idx);
		}
	}
};

SegTree tr[26];

class Solution {
public:
    vector<int> longestRepeating(string s, string qc, vector<int> &qi) {
        rep(i, 0, 26) {
            tr[i].build(0, sz(s), 1);
        }
        rep(i, 0, sz(s)) {
            tr[s[i]-'a'].set(i,i,1,1);
        }
        vi ans(sz(qc));
        rep(i, 0, sz(qc)) {
            int pos = qi[i], nch = qc[i];
            tr[s[pos]-'a'].set(pos, pos, 1, 0);
            s[pos] = nch;
            tr[s[pos]-'a'].set(pos, pos, 1, 1);
            rep(j, 0, 26) {
                ans[i] = max(ans[i], tr[j].query(0, sz(s), 1));
            }
        }
        return ans;
    }
};

int main() {
    string s = "abyzz";
    string qc = "aa";
    vi qi = {2, 1};
    for (auto x : Solution().longestRepeating(s, qc, qi)) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}