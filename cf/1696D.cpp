#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;

vi p, pmn, pmx, smn, smx;
int n;

int left_min_moves(int r, int find_min) {
    if (r == 0) return 0;
    int idx;
    if (find_min) {
        idx = pmn[r];
    } else {
        idx = pmx[r];
    }
    return 1 + left_min_moves(idx, 1-find_min);
}

int right_min_moves(int l, int find_min) {
    if (l == n-1) return 0;
    int idx;
    if (find_min) {
        idx = smn[l];
    } else {
        idx = smx[l];
    }
    if (idx == n-1) return 1;
    return 1 + right_min_moves(idx, 1-find_min);
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        cin >> n;
        // vi p(n), pmn(n), pmx(n), smn(n), smn(n);
        p = vi(n);
        pmn = vi(n);
        pmx = vi(n);
        smn = vi(n);
        smx = vi(n);
        int pivot;
        for (int i = 0;i < n;i++) {
            cin >> p[i];
            if (i == 0) {
                pmn[i] = pmx[i] = i;
            } else {
                pmn[i] = pmn[i-1];
                pmx[i] = pmx[i-1];
                if (p[i] < p[pmn[i-1]]) pmn[i] = i;
                if (p[i] > p[pmx[i-1]]) pmx[i] = i;
            }
            if (p[i] == n) pivot = i;
        }
        for (int i = n-1;i >= 0;i--) {
            if (i == n-1) {
                smn[i] = smx[i] = i;
            } else {
                smn[i] = smn[i+1];
                smx[i] = smx[i+1];
                if (p[i] < p[smn[i+1]]) smn[i] = i;
                if (p[i] > p[smx[i+1]]) smx[i] = i;
            }
        }
        cout << (left_min_moves(pivot, 1) + right_min_moves(pivot, 1)) << endl;
    }
    return 0;
}