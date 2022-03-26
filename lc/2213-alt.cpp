#include <bits/stdc++.h>

using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;


const int MM = 1e5 + 5;
struct node {
    int l, r, pfx, sfx, mx;
    bool same;
    char pfx_c, sfx_c;
} seg[4 * MM];
void pushup(int rt) {
    if (seg[rt].l == seg[rt].r) return;
    int lc = 2 * rt, rc = 2 * rt + 1;
    if (seg[lc].sfx_c == seg[rc].pfx_c) {
        if (seg[lc].same && seg[rc].same) {
            //cout << "BOTH\n";
            //cout << seg[lc].l << " " << seg[lc].r << "\n";
            seg[rt].same = 1; seg[rt].pfx = seg[rt].sfx = seg[lc].pfx + seg[rc].pfx;
            seg[rt].mx = seg[rt].sfx;
            seg[rt].pfx_c = seg[rt].sfx_c = seg[lc].pfx_c;
        }
        else if (seg[lc].same) {
            //cout << "LEFT SAME" << "\n";
            //cout << seg[lc].l << " " << seg[lc].r << "\n";
            seg[rt].same = 0;
            seg[rt].pfx = seg[lc].pfx + seg[rc].pfx; seg[rt].pfx_c = seg[lc].pfx_c;
            seg[rt].sfx = seg[rc].sfx; seg[rt].sfx_c = seg[rc].sfx_c;
            seg[rt].mx = max(max(seg[lc].mx, seg[rc].mx), max(seg[rt].pfx, seg[rt].sfx));
        }
        else if (seg[rc].same) {
           //cout << "RIGHT\n";
            //cout << seg[lc].l << " " << seg[lc].r << "\n";
            seg[rt].same = 0;
            seg[rt].pfx = seg[lc].pfx; seg[rt].pfx_c = seg[lc].pfx_c;
            seg[rt].sfx = seg[rc].sfx + seg[lc].sfx; seg[rt].sfx_c = seg[rc].sfx_c;
            seg[rt].mx = max(max(seg[lc].mx, seg[rc].mx), max(seg[rt].pfx, seg[rt].sfx));
        }
        else {
            //we have a middle part with sfx_c and pfx_c:
            //cout << "MIDDLE\n";
            //cout << seg[lc].l << " " << seg[lc].r << "\n";
            seg[rt].same = 0;
            seg[rt].pfx = seg[lc].pfx; seg[rt].pfx_c = seg[lc].pfx_c;
            seg[rt].sfx = seg[rc].sfx; seg[rt].sfx_c = seg[rc].sfx_c;
            seg[rt].mx = max(max(max(seg[lc].mx, seg[lc].sfx + seg[rc].pfx), seg[rc].mx), max(seg[rt].pfx, seg[rt].sfx));
        }
    }
    else {
        //cout << "NONE\n";
        //cout << seg[lc].sfx_c << " " << seg[rc].pfx_c << "\n";
        //cout << seg[lc].l << " " << seg[lc].r << "\n";
        seg[rt].pfx_c = seg[lc].pfx_c, seg[rt].pfx = seg[lc].pfx; 
        seg[rt].same = 0;
        seg[rt].sfx_c = seg[rc].sfx_c, seg[rt].sfx = seg[rc].sfx;
        seg[rt].mx = max(seg[lc].mx, seg[rc].mx);
    }
}
void build(int rt, int l, int r, string& s) {
    seg[rt].l = l, seg[rt].r = r;
    if (l == r) {
        seg[rt].pfx_c = seg[rt].sfx_c = s[l - 1];
        seg[rt].same = seg[rt].pfx = seg[rt].sfx = seg[rt].mx = 1;
        return;
    }
    int mid = (l + r) / 2;
    build(2 * rt, l, mid, s), build(2 * rt + 1, mid + 1, r, s);
    pushup(rt);
}
void update(int rt, int idx, char ch) {
    if (seg[rt].l > idx || seg[rt].r < idx) return;
    if (seg[rt].l == idx && seg[rt].r == idx) {
        seg[rt].pfx_c = seg[rt].sfx_c = ch;
        //cout << "CHANGE " << ch << "\n";
        seg[rt].same = seg[rt].pfx = seg[rt].sfx = seg[rt].mx = 1;
        return;
    }
    update(2 * rt, idx, ch); update(2 * rt + 1, idx, ch);
    pushup(rt);
}
void prop(int rt) {
    if (seg[rt].l == seg[rt].r) {
        return;
    }
    //cout << seg[rt].l << " " << seg[rt].r << "\n";
    //cout << seg[rt].mx << " " << seg[rt].same << "MX\n";
    prop(2 * rt); prop(2 * rt + 1);
}

class Solution {
public:
    vector<int> longestRepeating(string s, string queryCharacters, vector<int>& queryIndices) {
        //how do you maintain the longest contiguous subarray of characters?
        //the left or right character must be the same as the middle character to expand?
        build(1, 1, s.size(), s);
        vector<int> ret;
        for (int i = 0; i < queryIndices.size(); i++) {
            update(1, queryIndices[i] + 1, queryCharacters[i]);
            ret.push_back(seg[1].mx);
        }
        return ret;
    }
};