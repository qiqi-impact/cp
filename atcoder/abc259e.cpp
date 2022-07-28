#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;

#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;

int main() {
    int n;
    cin >> n;
    unordered_map<int, int> pm;
    unordered_map<int, unordered_set<int>> pe;

    for (int i = 0;i < n;i++) {
        int m;
        cin >> m;
        for (int j = 0;j < m;j++) {
            int p, e;
            cin >> p >> e;
            if (e > pm[p]) {
                pm[p] = e;
                pe[p].clear();
                pe[p].insert(i);
            } else if (e == pm[p]) {
                pe[p].insert(i);
            }
        }
    }

    unordered_set<int> opts;
    for (auto [k, v] : pe) {
        if (v.size() == 1) {
            opts.insert(*(v.begin()));
        }
    }

    cout << (min(n, (int)opts.size() + 1)) << endl;

    return 0;
}