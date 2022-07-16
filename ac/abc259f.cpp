#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;

// this code doesnt work

int main() {
    int n;
    cin >> n;
    vi d(n);
    // unordered_map<unordered_map<int>> m;
    for (int i = 0;i < n;i++) {
        cin >> d[i];
    }
    vector<tuple<int, int, int>> v(n);
    for (int i = 0;i < n-1;i++) {
        int u,x,w;
        cin >> u >> x >> w;
        u--;
        x--;
        v.push_back({w,u,x});
    }
    sort(v.begin(), v.end());
    ll ret = 0;
    for (int i = v.size()-1;i >= 0;i--) {
        if (get<0>(v[i]) <= 0) break;
        int a = get<1>(v[i]);
        int b = get<2>(v[i]);
        if (d[a] && d[b]) {
            d[a]--;d[b]--;
            ret += get<0>(v[i]);
        }
    }
    cout << ret << endl;

    return 0;
}