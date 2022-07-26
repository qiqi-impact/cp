#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;

int main() {
    int n, m;
    cin >> n >> m;
    vvi ab(n, vi(2));
    int mxa = -1e9;
    for (int i = 0;i < n;i++) {
        cin >> ab[i][0] >> ab[i][1];
        mxa = max(mxa, ab[i][0]);
    }
    sort(ab.begin(), ab.end());
    int p = 0;

    vi ret(m, 0);
    int mn = m, mx = 0;
    for (int i = 1;i <= m;i++) {
        while (p < ab.size() && ab[p][0] < i) {
            mn = min(mn, ab[p][1]);
            mx = max(mx, ab[p][1]);
            p++;
        }
        if (mn < i) break;
        int localmx = max(mxa, mx);
        ret[localmx - i]++;
        if (m - i + 1 < m) {
            ret[m - i + 1]--;
        }
    }
    cout << ret[0] << " ";
    for (int i = 1;i < m;i++) {
        ret[i] += ret[i-1];
        cout << ret[i] << " ";
    }
    cout << endl;
    return 0;
}