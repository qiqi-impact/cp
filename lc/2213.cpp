#include <bits/stdc++.h>

using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

struct SegTree {
    static const maxn = 1e5 + 1;

    struct Node {
        int lo, hi;
        int pre = 0, suf = 0, ans = 0;
    };

    Node node[maxn << 2];

    

struct Node {
	Node *l = 0, *r = 0;
	int lo, hi;
    
	Node(int lo,int hi):lo(lo),hi(hi){
        if (lo!=hi) {
            int mid = (lo+hi)/2;
            l = new Node(lo, mid);
            r = new Node(mid+1, hi);
            pull();
        }
    }
	int query(int L, int R) {
		if (R < lo || hi < L) return 0;
		if (L <= lo && hi <= R) return ans;
		push();
        l->query(L,R);
        r->query(L,R);
        pull();
		return ans;
	}
    void pull() {
        ans = max(l->ans, r->ans);
        ans = max(ans, l->suf + r->pre);
        pre = l->pre;
        suf = r->suf;
        if (l->pre == l->hi - l->lo + 1) pre += r->pre;
        if (r->suf == r->hi - r->lo + 1) suf += l->suf;
    }
	void set(int L, int R, int x) {
		if (R < lo || hi < L) return;
		if (L <= lo && hi <= R) ans = suf = pre = x;
		else {
			push(), l->set(L, R, x), r->set(L, R, x);
            pull();
		}
	}
	void push() {
	}
};

Node tr[26];

vector<int> longestRepeating(string s, string qc, vector<int> &qi) {
    vector<Node> tr(26, Node(0, 0));
    rep(i, 0, 26) tr[i] = Node(0, sz(s));
    rep(i, 0, sz(s)) {
        tr[s[i]-'a'].set(i,i,1);
    }
    vi ans(sz(qc));
    rep(i, 0, sz(qc)) {
        int pos = qi[i], nch = qc[i];
        tr[s[pos]-'a'].set(pos, pos, 0);
        s[pos] = nch;
        tr[s[pos]-'a'].set(pos, pos, 1);
        rep(j, 0, 26) {
            ans[i] = max(ans[i], tr[j].query(0, sz(s)));
        }
    }
    return ans;
}

int main() {
    string s = "boogietime";
    string qc = "oot";
    vi qi = {3, 4, 3};
    for (auto x : longestRepeating(s, qc, qi)) {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}