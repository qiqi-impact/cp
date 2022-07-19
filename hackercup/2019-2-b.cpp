#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

void root(int a, vi& cc) {
    if (cc[a] != a) {
        cc[a]
    }
}

void join(int a, int b, vi& cc) {
    int ra = root(a, cc);
    int rb = root(b, cc);
    if (ra != rb) {
        cc[ra] = rb;
    }
}

void solve() {
    int m, n;
    cin >> n >> m;
    vvi reqs = vvi(m, vi(2, 0));
    vi cc = vi(n);
    for (int i = 0;i < n;i++) {
        cc[i] = i;
    }
    for (int i = 0;i < m;i++) {
        cin >> reqs[i][0] >> reqs[i][1];
        reqs[i][0]--;
        reqs[i][1]--;
    }

}


int main() {
    int t;
    cin >> t;
    for (int i = 0;i < t;i++) {
        cout << "Case #" << t+1 << ": " << solve();
    }
    return 0;
}