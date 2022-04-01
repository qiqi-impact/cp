#include <bits/stdc++.h>
#include <complex>
#include <queue>
#include <set>
#include <unordered_set>
#include <list>
#include <chrono>
#include <random>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <stack>
#include <iomanip>
#include <fstream>
using namespace std;
 
using ll = long long;
using vi = vector<int>;

// vectors
// oops size(x), rbegin(x), rend(x) need C++17
#define sz(x) int((x).size())
#define pb push_back

#define fast_cin() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)

const int MAXN = 1e5 + 1;
struct node {
    vi ct = vi(26, 0);
    int l, r, mx_op = -1, lst_op = -1, srt = 0;
};
node seg[MAXN*4];

void pull(int i) {
    seg[i].mx_op = max(seg[2*i].mx_op, seg[2*i+1].mx_op);
    for(int j = 0;j < 26;j++) {
        seg[i].ct[j] = seg[2*i].ct[j] + seg[2*i+1].ct[j];
    }
}

void build(int i, int l, int r, string s) {
    node &c = seg[i];
    c.l = l;
    c.r = r;
    if (l == r) {
        c.ct[s[l]-'a'] = 1;
    } else {
        node &lc = seg[2*i], &rc = seg[2*i+1];
        int m = (l+r)/2;
        build(2*i, l, m, s);
        build(2*i+1, m+1, r, s);
        pull(i);
    }
}

void nullout(int i, int l, int r, vi &ct) {
    node &c = seg[i];
    if (c.l > r || c.r < l) return;
    if (l <= c.l && c.r <= r) {
        for(int j = 0;j < 26;j++) {
            ct[j] += c.ct[j];
            c.ct[j] = 0;
        }
    } else {
        nullout(2*i, l, r, ct);
        nullout(2*i+1, l, r, ct);
        pull(i);
    }
}

void apply(int i, int l, int r, int chi, int opidx, int srt) {
    node &c = seg[i];
    if (c.l > r || c.r < l) return;
    if (l <= c.l && c.r <= r) {
        c.ct[chi] = r-l+1;
        c.lst_op = c.mx_op = opidx;
        c.srt = srt;
    } else {
        apply(2*i, l, r, chi, opidx, srt);
        apply(2*i+1, l, r, chi, opidx, srt);
        pull(i);
    }
}

void operate(int l, int r, int op, int opidx) {
    vi ct(26, 0);
    nullout(1, l, r, ct);
    for (int j = 0;j < 26;j++) {
        int chi = (op == 1 ? j : 25-j);
        apply(1, l, l+ct[chi]-1, chi, opidx, op ? -1 : 1);
        l += ct[chi];
    }
}

void prt(int i, string s) {
    if (seg[i].mx_op == seg[i].lst_op) {
        if (seg[i].srt == 0) {
            for (int j = seg[i].l;j <= seg[i].r;j++) {
                cout << s[j];
            }
        } else {
            for (int j = 0; j < 26; j++) {
                int ci = (seg[i].srt == 1 ? j : 25-j);
                char c = 'a' + ci;
                for (int k = 0;k < seg[i].ct[j];k++) {
                    cout << c;
                }
            }
        }
    } else {
        prt(2*i, s);
        prt(2*i+1, s);
    }
}

int main() {
    fast_cin();
    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    
    int n, m;
    cin >> n >> m;
    vi v;
    int l, r, x;
    string s;

    cin >> s;
    build(1, 0, s.length()-1, s);
    prt(1, s);
    cout << endl;
    for (int i = 0;i < m;i++) {
        cin >> l >> r >> x;
        l--; r--;
        operate(l, r, x, i);
        prt(1, s);
        cout << endl;
    }
    
    cout << endl;
    
    return 0;
}