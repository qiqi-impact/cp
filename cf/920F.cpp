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

const int MAXN = 3e5 + 1;
struct node {
    ll sm = 0;
    int ptr = 0, l, r, mx;
};
node seg[MAXN*4];

void pull(int i) {
    seg[i].sm = seg[2*i].sm + seg[2*i+1].sm;
    seg[i].mx = max(seg[2*i].mx, seg[2*i+1].mx);
}

void build(int i, int l, int r, vi &v) {
    node &c = seg[i];
    c.l = l;
    c.r = r;
    if (l == r) {
        c.sm = c.mx = v[l];
    } else {
        int m = (l+r)/2;
        build(2*i, l, m, v);
        build(2*i+1, m+1, r, v);
        pull(i);
    }
    // for (auto &x: cur.values) {
    //     cout << x << " ";
    // }
    // cout << endl;
}

void replace(int i, int l, int r, vi &fac) {
    node &c = seg[i];
    if (c.mx <= 2) return;
    if (c.l > r || c.r < l) return;
    if (c.l == c.r) {
        c.sm = c.mx = fac[c.mx];
    } else {
        replace(2*i, l, r, fac);
        replace(2*i+1, l, r, fac);
        pull(i);
    }
}

ll query(int i, int l, int r) {
    node &c = seg[i];
    if (c.l > r || c.r < l) return 0;
    ll ret;
    if (c.l >= l && c.r <= r) {
        ret = c.sm;
        // cout << i << l << r << " " << ret << endl;
    } else {
        ret = query(2*i, l, r) + query(2*i+1, l, r);
    }
    return ret;
}

int main() {
    const int MXV = 1e6 + 1;
    fast_cin();
    // freopen("input.txt", "r", stdin);
	// freopen("output.txt", "w", stdout);
    vi fac(MXV, 0);
    for (int i = 1;i < MXV;i++) {
        for (int j = i;j < MXV;j += i) {
            fac[j]++;
        }
    }
    // for (int i = 1;i < 11;i++) cout << fac[i] << " ";
    // cout << endl;
    // return 0;
    
    int n, m;
    cin >> n >> m;
    vi v;
    int x, l, r;
    for (int i = 0;i < n;i++) {
        cin >> x;
        v.pb(x);
    }
    build(1, 0, n-1, v);
    for (int i = 0;i < m;i++) {
        cin >> x >> l >> r;
        l--; r--;
        if (x == 1) {
            replace(1, l, r, fac);
        } else {
            cout << query(1, l, r) << endl;
        }
    }
    
    return 0;
}