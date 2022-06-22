#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;

int main() {
    int n;
    cin >> n;
    vi locks(n);
    ll min_time = 0;
    ll c = 0;
    for (int i = 0;i < n;i++) {
        cin >> locks[i];
        c += locks[i];
        min_time = max(min_time, (c+i)/(ll)(i+1));
    }
    // cout << min_time << endl;
    int q;
    cin >> q;
    for (int i = 0;i < q;i++) {
        int x;
        cin >> x;
        if (x < min_time) {
            cout << -1 << endl;
            continue;
        }
        cout << (c + x - 1) / x << endl;
    }
    return 0;
}